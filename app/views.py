from flask import render_template
import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello Pitchez'

    title = 'HOME - best pitch of the day'
    return render_template('index.html', message = message, title=title)