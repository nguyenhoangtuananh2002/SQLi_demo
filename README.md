# SQL Injection (SQLi) Demo - Flask Vulnerable Web App

## Overview
This is a simple Flask web application created to **demonstrate SQL Injection (SQLi) vulnerabilities** in a safe, educational environment.  
It allows students to practice **black-box testing** by interacting with a login form and trying to bypass authentication using SQL injection techniques.

---

## Features
- Vulnerable login page accepting username and password via GET parameters
- Backend uses raw SQL queries built with string concatenation (intentionally vulnerable)
- Sample SQLite database with one user (`admin` / `admin123`)
- Demonstrates how SQLi allows login bypass, data retrieval, and other attacks
- Bootstrap 5 styled frontend for clean UI


# SQL Injection Test Inputs (no valid password needed)

| Username           | Password  | Description                        |
|--------------------|-----------|----------------------------------|
| admin' --          | anything  | Bypass password, login as admin  |
| ' OR 1=1 --        | anything  | Login as first user in database  |
| ' OR 'a'='a' --    | anything  | Another common SQLi bypass        |

## Getting Started

### Prerequisites
- Python 3.7+
- Flask (`pip install flask`)

### Installation & Setup
1. Clone or download this repository.
2. (Optional) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

