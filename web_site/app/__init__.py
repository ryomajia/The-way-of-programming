from flask import Flask


app = Flask(__name__)

from app import crawled_item_web
