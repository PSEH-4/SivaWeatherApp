from flask import Flask, render_template
from weatherapi import getAPIResponse
import os

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/my-link/')

def my_link():
    html_str = getAPIResponse()
    dirpath = os.getcwd()
    with open(dirpath + "/src/templates/weather.html", "w") as file:
        file.write(html_str)
    return render_template('weather.html')

if __name__ == "__main__":
    app.run()