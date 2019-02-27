import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/jobs.sqlite'

app = Flask(__name__)
