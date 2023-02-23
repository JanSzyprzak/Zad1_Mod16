from flask import render_template
from Blog import app


@app.route('/')
def main():
    return render_template('base.html')