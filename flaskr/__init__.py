from flask import Flask
app = Flask(__name__)
import flaskr.main
from flaskr import db

db.createImages()
db.insertImages()
db.createPlayLog()