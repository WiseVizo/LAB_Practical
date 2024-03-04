
from flask import Flask, render_template
import os

# Create a Flask application
app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

# Define routes to serve frontend pages
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/student-cornner')
def student_cornner():
    return render_template('student_cornner.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


# Define other routes...

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)