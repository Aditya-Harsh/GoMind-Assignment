from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db',check_same_thread=False)
c = conn.cursor()

# Create a table to store the form data
c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, college TEXT)''')
conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    college = request.form['college']

    # Insert the form data into the database
    c.execute("INSERT INTO students (name, college) VALUES (?, ?)", (name, college))
    conn.commit()

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
