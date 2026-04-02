from flask import Flask, request, jsonify
import psycopg2
import uuid
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# NeonDB connection
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

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
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO messages (message_id, name, email, message)
                VALUES (%s, %s, %s, %s)
            """, (message_id, name, email, message))
            conn.commit()
        return jsonify({"status": "success", "message_id": message_id})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
