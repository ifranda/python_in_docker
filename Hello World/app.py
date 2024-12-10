# Import the flask python module
from flask import Flask

# Define the Flask constructor
app = Flask(__name__)

# The .route() function in flask is a decorator that tells the application what function to run when visiting certain URLs.
# This defines that when someone visits <URL>/ the hello_world application should run
@app.route('/')
def hello_world():
    return 'Hello World'

# Create the main driver function to run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0")