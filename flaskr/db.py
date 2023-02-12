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
    con.close()

def createUrls():
    con = sqlite3.connect(MASTER_DATABASE)
    con.execute("""
        CREATE TABLE IF NOT EXISTS
            urls (
                id integer primary key autoincrement,
                url unique,
                title
                delete_flg boolean
            );
    """)
    con.commit()
    con.close()

def createSrcs():
    con = sqlite3.connect(MASTER_DATABASE)
    con.execute("""
        CREATE TABLE IF NOT EXISTS
            srcs (
                id integer primary key autoincrement,
                url,
                src,
                datasrc,
                srcset,
                alt text,
                delete_flg boolean
            );
    """)
    con.commit()
    con.close()

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
    con.close()


def insertUrl(url, title):
    with sqlite3.connect(MASTER_DATABASE) as con:
        con.execute(f"""
            INSERT INTO
                urls(
                    url,
                    title
                ) VALUES (
                    "{url}",
                    "{title}"
                );
        """)
        con.commit()


def insertSrcs(url, srcs):
    with sqlite3.connect(MASTER_DATABASE) as con:
        for src in srcs:
            con.execute(f"""
                INSERT INTO
                    srcs(
                        url,
                        src,
                        datasrc,
                        srcset,
                        alt
                    ) VALUES (
                        "{url}",
                        '{ src["src"] if "src" in src else ""}',
                        '{ src["data-src"] if "data-src" in src else ""}',
                        '{ src["srcset"] if "srcset" in src else ""}',
                        '{ src["alt"] if "alt" in src else ""}'
                    );
            """)
        con.commit()

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
                        `like`
                    ) VALUES (
                        "{path}",
                        "99",
                        "0"
                    )
            """)
    con.commit()
    con.close()

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
    con.close()

def selectImages(pattern = ""):
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute(f"""
        SELECT
            path,
            `like`,
            score,
            message
        FROM images
        WHERE
            id  LIKE '%{pattern}%'
            OR path  LIKE '%{pattern}%'
            OR `like`  LIKE '%{pattern}%'
            OR score  LIKE '%{pattern}%'
        ORDER BY score desc
    """).fetchall()
    con.close()
    return db_images

def selectSrcs():
    con = sqlite3.connect(MASTER_DATABASE)
    db_srcs = con.execute(f"""
        SELECT
            id,
            url,
            src,
            datasrc,
            srcset,
            alt
        FROM srcs
        ORDER BY id desc
    """).fetchall()
    con.close()
    return db_srcs

def selectImagesCount(count):
    con = sqlite3.connect(MASTER_DATABASE)
    db_images = con.execute(f"""
        SELECT
            id,
            path,
            `like`,
            score
        FROM images
        ORDER BY RANDOM() LIMIT {count}
    """).fetchall()
    con.close()
    return db_images