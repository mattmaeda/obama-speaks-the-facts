import os

import requests
from flask import Flask, render_template, session
from bs4 import BeautifulSoup

APP = Flask(__name__)
URL = "http://talkobamato.me/synthesize.py"

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@APP.route('/')
def home():
    fact = get_fact()
    resp = requests.post(URL,
                         data={"input_text": fact},
                         allow_redirects=False)
    soup = BeautifulSoup(resp.content, "html.parser")
    link = soup.find_all("a")
    href = link[0]["href"]

    return render_template('obama.jinja2', href=href)


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 6787))
    APP.run(host='0.0.0.0', port=PORT)
