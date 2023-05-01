from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def start_function():
    print("hey")
    return render_template('index.html')





def home():
    print("hello1")

    print(app.template_folder)

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    print("Everything connected")
    cur = conn.cursor()
    db_name = os.getenv("POSTGRES_DB")
    print(db_name)
    cur.execute('SELECT * FROM public."CM_HAM_DO_AI1/Temp_value"')
    data = cur.fetchall()
    cur.close()
    conn.close()
    print("hello")
    print("hey", app.template_folder)
    return "hey"


app.run(host='0.0.0.0', port=8888, debug=True)