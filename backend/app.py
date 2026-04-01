from flask import Flask, request, jsonify
import psycopg2
import uuid
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin
import requests  # for sending EmailJS requests

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# NeonDB connection
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

# EmailJS environment variables
EMAILJS_SERVICE_ID = os.getenv("EMAILJS_SERVICE_ID")
EMAILJS_TEMPLATE_ID = os.getenv("EMAILJS_TEMPLATE_ID")
EMAILJS_PUBLIC_KEY = os.getenv("EMAILJS_PUBLIC_KEY")
TO_EMAIL = os.getenv("TO_EMAIL")  # your email to receive messages

# Create table if not exists
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            message_id UUID PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()


@cross_origin()
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    message_id = str(uuid.uuid4())

    try:
        # Store message in NeonDB
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO messages (message_id, name, email, message)
                VALUES (%s, %s, %s, %s)
            """, (message_id, name, email, message))
            conn.commit()

        # Send message via EmailJS
        email_payload = {
            "service_id": EMAILJS_SERVICE_ID,
            "template_id": EMAILJS_TEMPLATE_ID,
            "user_id": EMAILJS_PUBLIC_KEY,
            "template_params": {
                "from_name": name,
                "from_email": email,
                "message": message,
                "to_email": TO_EMAIL
            }
        }

        r = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=email_payload)
        if r.status_code != 200:
            return jsonify({"status": "error", "error": f"Email sending failed: {r.text}"}), 500

        return jsonify({"status": "success", "message_id": message_id})

    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway sets PORT dynamically
    app.run(host='0.0.0.0', port=port, debug=True)
