import sqlite3
import hashlib
import secrets
import json
from datetime import datetime

DB_FILE = "resume_analyzer.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT,
        fullname TEXT,
        profile_skills TEXT,
        profile_summary TEXT
    )
    """)
    
    # Create reports table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        resume_name TEXT,
        job_description TEXT,
        score INTEGER,
        matched_skills TEXT,
        missing_skills TEXT,
        suggestions TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
    """)
    
    conn.commit()
    conn.close()

def hash_password(password):
    salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    )
    return f"{salt}${key.hex()}"

def verify_password(stored_password, provided_password):
    try:
        salt, hex_key = stored_password.split('$')
        key = hashlib.pbkdf2_hmac(
            'sha256',
            provided_password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return key.hex() == hex_key
    except Exception:
        return False

def create_user(username, password, email, fullname):
    conn = get_connection()
    cursor = conn.cursor()
    pwd_hash = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, email, fullname, profile_skills, profile_summary) VALUES (?, ?, ?, ?, ?, ?)",
            (username.lower().strip(), pwd_hash, email.strip(), fullname.strip(), "", "")
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username.lower().strip(),))
    user = cursor.fetchone()
    conn.close()
    
    if user and verify_password(user['password_hash'], password):
        return {
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'fullname': user['fullname'],
            'profile_skills': user['profile_skills'],
            'profile_summary': user['profile_summary']
        }
    return None

def update_user_profile(user_id, email, fullname, profile_skills, profile_summary):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET email = ?, fullname = ?, profile_skills = ?, profile_summary = ? WHERE id = ?",
        (email.strip(), fullname.strip(), profile_skills.strip(), profile_summary.strip(), user_id)
    )
    conn.commit()
    conn.close()

def get_user_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'fullname': user['fullname'],
            'profile_skills': user['profile_skills'],
            'profile_summary': user['profile_summary']
        }
    return None

def save_report(user_id, resume_name, job_description, score, matched_skills, missing_skills, suggestions):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reports (user_id, resume_name, job_description, score, matched_skills, missing_skills, suggestions) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            user_id,
            resume_name,
            job_description,
            score,
            json.dumps(matched_skills),
            json.dumps(missing_skills),
            json.dumps(suggestions)
        )
    )
    conn.commit()
    conn.close()

def get_user_reports(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    
    reports = []
    for r in rows:
        reports.append({
            'id': r['id'],
            'user_id': r['user_id'],
            'resume_name': r['resume_name'],
            'job_description': r['job_description'],
            'score': r['score'],
            'matched_skills': json.loads(r['matched_skills']),
            'missing_skills': json.loads(r['missing_skills']),
            'suggestions': json.loads(r['suggestions']),
            'created_at': r['created_at']
        })
    return reports

def delete_report(report_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reports WHERE id = ? AND user_id = ?", (report_id, user_id))
    conn.commit()
    conn.close()
