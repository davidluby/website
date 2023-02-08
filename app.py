"""
    author: David Luby
    flask portfolio web application backend script
    deployed via aws elastic beanstalk cli in virtual environment
    ci/cd pipeline via git repository
"""


# package imports
from flask import Flask, render_template



# create new flask instance for eb called application
app = Flask(__name__)



# creating flask endpoints for site's pages

# home and resume pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')



# software pages
@app.route('/big.html')
def big():
    return render_template('software/big.html')

@app.route('/fifo.html')
def fifo():
    return render_template('software/fifo.html')

@app.route('/fft.html')
def fft():
    return render_template('software/fft.html')



# firmware pages
@app.route('/micro.html')
def firm():
    return render_template('firmware/micro.html')

@app.route('/timer.html')
def timer():
    return render_template('firmware/timer.html')



# mechanical pages
@app.route('/controls.html')
def ctrl():
    return render_template('mechanical/controls.html')
@app.route('/fourier.html')
def four():
    return render_template('mechanical/fourier.html')
@app.route('/fea.html')
def fea():
    return render_template('mechanical/fea.html')



# introducing main module guard
if __name__ == 'main':
    # remove debug output for production deployment (maybe, no secrets here)
    #application.debug = True
    app.run()