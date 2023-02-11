from flaskr import app
from flask import render_template, request, redirect, url_for

from flaskr import common
from flaskr import db

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/master')
def master():
    db_images = db.selectImages()
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


@app.route("/random/<int:count>")
def random(count):
    session = common.getRandom()
    db_images = db.selectImagesCount(count)
    images = []
    for row in db_images:
        images.append({
            "id" : row[0],
            "path" : row[1],
            "like" : row[2],
            "score" : row[3],
        })
    return render_template(
        'random.html',
        session=session,
        count=count,
        images=images,
        height=500,
        transition=0.5,
        scale=1.5,
    )

@app.route("/send_winner", methods=["POST"])
def send_winner():
    playLogs = []
    winner = request.form["winner"]
    winner_score = request.form["winnerScore"]
    session = request.form["session"]
    count = request.form["count"]

    i = 0
    while (f"player{i}") in request.form:
        loser = request.form[f"player{i}"]
        loser_score = request.form[f"score{i}"]

        if (request.form["winner"] != request.form[f"player{i}"]):
            playLogs.append({
                "session" : session,
                "count" : count,
                "winner" : winner,
                "loser" : loser,
                "winner_score" : winner_score,
                "loser_score" : loser_score,
            })
        i += 1
    db.insertPlayLogs(playLogs)

    return redirect(url_for("random", count=count))
