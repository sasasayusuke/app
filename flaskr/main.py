from flaskr import app
from flask import render_template, request, redirect, url_for
import random
import sqlite3
MASTER_DATABASE = "master.db"
TRUN_DATABASE = "trun.db"

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/master')
def master():
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute(
        """
        SELECT
            path,
            like,
            score
        FROM images;
        """
    ).fetchall()
    con.close()
    images = []
    for row in db_images:
        images.append({
            "path" : row[0],
            "like" : row[1],
            "score" : row[2],
        })
    return render_template(
        'master.html',
        images=images,
        height=320,
        width=400,
        transition=0.5,
        scale=1.75,
    )


@app.route("/play/<int:count>")
def play(count):
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute(f"SELECT id, path, like, score FROM images ORDER BY RANDOM() LIMIT {count};").fetchall()
    con.close()
    images = []
    for row in db_images:
        images.append({
            "id" : row[0],
            "path" : row[1],
            "like" : row[2],
            "score" : row[3],
        })
    return render_template(
        'play.html',
        session=random.randint(100000000, 999999999),
        count=count,
        images=images,
        height=500,
        transition=0.5,
        scale=1.5,
    )

@app.route("/winner", methods=["POST"])
def winner():
    winner = request.form["winner"]
    winner_score = request.form["winnerScore"]
    session = request.form["session"]
    count = request.form["count"]

    con = sqlite3.connect(TRUN_DATABASE)
    i = 0
    while (f"player{i}") in request.form:
        loser = request.form[f"player{i}"]
        loser_score = request.form[f"score{i}"]
        if (request.form["winner"] != request.form[f"player{i}"]):
            con.execute(f'INSERT INTO playLog(id, player_count, winner, loser, winner_score, loser_score) VALUES("{session}", "{count}", "{winner}", "{loser}", "{winner_score}", "{loser_score}")')
        i += 1

    con.commit()
    con.close()
    return redirect(url_for("play", count=count))
