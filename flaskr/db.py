import sqlite3
import pathlib
from flaskr import common, setting

MASTER_DATABASE = "master.db"
TRUN_DATABASE = "trun.db"


def createImages():
    con = sqlite3.connect(MASTER_DATABASE)
    con.execute("""
        CREATE TABLE IF NOT EXISTS
            images (
                id integer primary key autoincrement,
                path,
                `like` int,
                score int,
                message text
            )
    """)
    con.commit()
    con.close

def createPlayLog():
    con = sqlite3.connect(TRUN_DATABASE)
    con.execute("""
        CREATE TABLE IF NOT EXISTS
            playLog (
                session_id int not null,
                player_count int,
                winner int,
                loser int,
                winner_score int,
                loser_score int
            )
    """)
    con.commit()
    con.close

def insertImages():
    con = sqlite3.connect(MASTER_DATABASE)
    db_paths = con.execute("""
        SELECT
            path
        FROM images
    """).fetchall()
    paths = [item[0] for item in db_paths]

    extensions = ["png", "jpg", "jpeg", "webp", "gif", "jfif"]
    cur = pathlib.Path.joinpath(pathlib.Path(__file__).parent, setting.PATH)
    allFIle = []

    for ext in extensions:
        allFIle.extend(common.getFiles(cur, ext))
    for file in allFIle:
        path = file.split(setting.APPNAME)[1]
        if (path not in paths):
            con.execute(f"""
                INSERT INTO
                    images(
                        path,
                        score,
                        like
                    ) VALUES (
                        "{path}",
                        "99",
                        "0"
                    )
            """)
    con.commit()
    con.close

def insertPlayLogs(playLogs):

    con = sqlite3.connect(TRUN_DATABASE)
    for log in playLogs:
        con.execute(f"""
            INSERT INTO
                playLog(
                    id,
                    player_count,
                    winner,
                    loser,
                    winner_score,
                    loser_score
                ) VALUES (
                    "{log['session']}",
                    "{log['count']}",
                    "{log['winner']}",
                    "{log['loser']}",
                    "{log['winner_score']}",
                    "{log['loser_score']}")
        """)
    con.commit()
    con.close

def selectImages():
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute("""
        SELECT
            path,
            like,
            score
        FROM images
        ORDER BY score desc
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
        ORDER BY RANDOM() LIMIT {count}
    """).fetchall()
    con.close()
    return db_images