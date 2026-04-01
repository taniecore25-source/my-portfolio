from flask import Flask, request, jsonify
import psycopg2
import uuid
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# NeonDB/Postgres connection details from environment variables
DB_HOST = os.getenv("DB_HOST", "your_neon_host")
DB_NAME = os.getenv("DB_NAME", "your_db_name")
DB_USER = os.getenv("DB_USER", "your_db_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_db_password")
DB_PORT = os.getenv("DB_PORT", "5432")

# Connect to NeonDB
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    message_id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
)
""")
conn.commit()


@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"message": "All fields are required"}), 400

    message_id = str(uuid.uuid4())

    try:
        cursor.execute(
            "INSERT INTO messages (message_id, name, email, message) VALUES (%s, %s, %s, %s)",
            (message_id, name, email, message)
        )
        conn.commit()
        return jsonify({"message": "Message sent and stored successfully!"})
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to store message"}), 500


if __name__ == "__main__":
    app.run(debug=True)
