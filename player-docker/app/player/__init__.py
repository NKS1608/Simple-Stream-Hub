from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object('config')


from player.controllers import default
from player.controllers import player
from player.controllers import assistir