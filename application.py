"""
    author: David Luby
    flask portfolio web application backend script
    deployed via aws elastic beanstalk cli in virtual environment
    ci/cd pipeline via git repository
"""


# package imports
from flask import Flask, render_template



# create new flask instance for eb called application
application = Flask(__name__)



# creating flask endpoints for site's pages

# home and resume pages
@application.route('/')
def home():
    return render_template('home.html')

@application.route('/resume.html')
def resume():
    return render_template('resume.html')



# software pages
@application.route('/big.html')
def big():
    return render_template('software/big.html')

@application.route('/fifo.html')
def fifo():
    return render_template('software/fifo.html')

@application.route('/four.html')
def four():
    return render_template('software/four.html')



# firmware pages
@application.route('/micro.html')
def firm():
    return render_template('firmware/micro.html')

@application.route('/timer.html')
def timer():
    return render_template('firmware/timer.html')



# mechanical pages
@application.route('/controls.html')
def ctrl():
    return render_template('mechanical/controls.html')

@application.route('/fea.html')
def fea():
    return render_template('mechanical/fea.html')



# introducing main module guard
if __name__ == 'main':
    # remove debug output for production deployment (maybe, no secrets here)
    #application.debug = True
    application.run()