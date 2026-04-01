from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# Connect to NeonDB
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route("/save-message", methods=["POST"])
def save_message():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not (name and email and message):
        return jsonify({"status":"error", "message":"All fields are required"}), 400

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s) RETURNING message_id",
        (name, email, message)
    )
    message_id = cur.fetchone()[0]
    conn.commit()
    cur.close()

    return jsonify({
        "status": "success",
        "message_id": message_id
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
