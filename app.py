import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/meme/', methods=['GET', 'POST'])
def getMeme():
    resposta = requests.get('https://meme-api.herokuapp.com/gimme')
    meme = resposta.json()['url']
    return render_template('meme.html', image_meme=meme)


if __name__ == '__main__':
    app.run()
