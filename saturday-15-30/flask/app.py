from flask import Flask, request
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="blog",
        user="postgres",
        password="qawsedrf")

app = Flask(__name__)

posts = [
        {
            "header": "Post 1",
            "body": "Hello world"
        },
        {
            "header": "Post 2",
            "body": "Hello world"
        }
]

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def create_post():
    posts.append(request.get_json())

    cur = conn.cursor()
    cur.execute("insert into posts (id, header, body) values (7, 'qwerty', 'qwerty');")

    conn.commit()
    cur.close()

    return "Success", 201


