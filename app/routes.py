from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    # user = {'username': 'CHEDDAR'}  
    return render_template('home.html')


@app.route('/pdftoword')
def pdftoword():
    # user = {'username': 'CHEDDAR'}  
    return render_template('pdftoword.html')

@app.route('/mp3downloader')
def mp3downloader():
    # user = {'username': 'CHEDDAR'}  
    return render_template('mp3downloader.html')