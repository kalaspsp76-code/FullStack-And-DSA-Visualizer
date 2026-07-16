import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def create_database():
    connection = sqlite3.connect("portfolio.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """
    )
    cursor.execute("SELECT COUNT(*) FROM projects")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO projects (title, description) VALUES ('My First CSE Project', 'This data is coming straight from my SQL DBMS database!')"
        )
        connection.commit()
    connection.close()


@app.route("/")
def home_page():
    connection = sqlite3.connect("portfolio.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description FROM projects")
    project = cursor.fetchone()
    connection.close()
    return render_template("index.html", title=project[0], description=project[1])


@app.route("/dsa")
def dsa_page():
    return render_template("dsa.html")


if __name__ == "__main__":
    create_database()
    app.run(debug=True)