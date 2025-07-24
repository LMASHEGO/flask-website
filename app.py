from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["post"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]


    save_to_db(name, email, message)
    return redirect("/")

def save_to_db(name, email, message):
    conn = sqlite3.connect("message.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)" , (name, email, message))
    conn.commit()
    conn.close() 


@app.route("/projects")
def projects():
    projects_list = [
        {"title": "Student Donation App", "desc": "Helps students get resources"},
        {"title": "AI-Based IDS", "desc": "Research project on intrusion detection"},
    ]
    return render_template("projects.html", projects=projects_list)

if __name__ == "__main__":
    app.run(debug=True)




conn = sqlite3.connect("messages.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
""")
conn.commit()
conn.close()