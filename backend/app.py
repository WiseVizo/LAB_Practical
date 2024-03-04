
from flask import Flask, render_template
import os

# Create a Flask application
app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

# Define routes to serve frontend pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about1')
def about():
    return render_template('about.html')

# Define other routes...

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)