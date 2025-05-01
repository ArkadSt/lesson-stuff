from flask import Flask, request
from flask_cors import CORS
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="blog",
        user="postgres",
        password="qawsedrf")


cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS posts ( \
    id SERIAL PRIMARY KEY,          \
    header VARCHAR(255) NOT NULL,   \
    body TEXT NOT NULL, \
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  \
);")
cur.close()
conn.commit()

app = Flask(__name__)
CORS(app)

@app.get("/posts")
def get_posts():
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts;")
    
    # Get column names from the cursor description
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    
    # Map each row to a dict using column names
    posts = [dict(zip(columns, row)) for row in rows]

    cur.close()
    return posts



@app.post("/posts")
def create_post():

    post = request.get_json()

    with conn.cursor() as cur:
        cur.execute("insert into posts (header, body) values (%s, %s);", (post["header"], post["body"]))

    conn.commit()

    return post, 201


