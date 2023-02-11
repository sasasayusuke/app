import sqlite3
import pathlib
from flaskr import common

APP_NAME = "flaskr"
PATH = "static/img/i_ver1"

MASTER_DATABASE = "master.db"
TRUN_DATABASE = "trun.db"

def insertImages():
    con = sqlite3.connect(MASTER_DATABASE)
    db_paths = con.execute("SELECT path FROM images").fetchall()
    paths = [item[0] for item in db_paths]

    extensions = ["png", "jpg", "jpeg", "webp", "gif", "jfif"]
    cur = pathlib.Path.joinpath(pathlib.Path(__file__).parent, PATH)
    allFIle = []

    for ext in extensions:
        allFIle.extend(common.getFiles(cur, ext))
    for file in allFIle:
        path = file.split(APP_NAME)[1]
        if (path not in paths):
            con.execute(f'INSERT INTO images(path, score, like) VALUES("{path}", "102", "0")')
    con.commit()
    con.close

def insertPlayLogs(playLogs):

    con = sqlite3.connect(TRUN_DATABASE)
    for log in playLogs:
        con.execute(f'''
            INSERT INTO
                playLog(
                    id,
                    player_count,
                    winner,
                    loser,
                    winner_score,
                    loser_score
                ) VALUES(
                    "{log['session']}",
                    "{log['count']}",
                    "{log['winner']}",
                    "{log['loser']}",
                    "{log['winner_score']}",
                    "{log['loser_score']}")
        ''')
    con.commit()
    con.close

def selectImages():
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute("""
        SELECT
            path,
            like,
            score
        FROM images;
    """).fetchall()
    con.close()
    return db_images

def selectImagesCount(count):
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute(f"""
        SELECT
            id,
            path,
            like,
            score
        FROM images
        ORDER BY RANDOM() LIMIT {count};
    """).fetchall()
    con.close()
    return db_images