from flask import Flask, jsonify, render_template
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

# PostgreSQL connection
db_host = os.getenv('DB_HOST', 'localhost')
db_name = os.getenv('DB_NAME', 'mydb')
db_user = os.getenv('DB_USER', 'user')
db_password = os.getenv('DB_PASSWORD', 'password')

def log_hello_message():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            message TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Insert log
        cursor.execute("INSERT INTO logs (message) VALUES (%s)", ("Hello from App 2!",))
        conn.commit()

        cursor.close()
        conn.close()
    except Exception as e:
        print("Database connection failed:", e)

@app.route('/')
def hello():
    log_hello_message()  # Log the message to the database
    return "Hello from the flask app. See <a href='./logs'>logs</a>"

@app.route('/logs')
def get_logs():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()

        # Fetch all logs from the database
        cursor.execute("SELECT id, message, timestamp FROM logs ORDER BY timestamp DESC")
        logs = cursor.fetchall()

        cursor.close()
        conn.close()

        # Convert logs to a list of dictionaries
        logs_list = []
        for log in logs:
            log_dict = {
                'id': log[0],
                'message': log[1],
                'timestamp': log[2].isoformat()
            }
            logs_list.append(log_dict)

        return jsonify(logs_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
