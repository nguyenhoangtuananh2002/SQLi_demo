from flask import Flask,request,render_template,redirect,url_for
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'demo.db'

def init_db():
    if os.path.exists(DB_NAME): 
        return
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )"""
    )
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('alice', 'alicepass')")
    conn.commit()
    conn.close()
@app.route('/')
def home(): 
    return render_template('login.html')

@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    query = f"SELECT * FROM users WHERE username = '{username}' AND password ='{password}'"
    print(f"Executing: {query}")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    result = cursor.execute(query).fetchone()
    conn.close()

    if result:
        # Render sqli_session.html first
        return render_template('sqli_session.html', query=query, username=username, password=password)
    else:
        return "<h2>Login failed!</h2>"


@app.route('/code-session', methods=['GET', 'POST'])
def code_session():
    if request.method == 'POST':
        fixed_code = request.form.get('fixed_code')
        # Render the template with user fix and all suggested solutions
        return render_template('code_session.html', 
                               show_solutions=True, 
                               fixed_code=fixed_code)

    # GET request: get username and password from query params
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    # Build the vulnerable query dynamically
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    full_querry = f"""
        {query}
        cursor = conn.cursor()
        result = cursor.execute(query).fetchone()
    """

    # Pass the query to the template for the code editor prefill
    return render_template('code_session.html', 
                           show_solutions=False, 
                           query=full_querry)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

