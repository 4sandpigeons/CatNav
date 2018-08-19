import requests
from flask import Flask, render_template, request

caturl = 'http://aws.random.cat/meow' #for later use

app = Flask(__name__)

@app.route('/')
def cat():
    varCat = requests.get(caturl)
    varCat = varCat.json()
    Cats = varCat['file']
    return render_template('cat.html', Cats = Cats)



if __name__ == '__main__':
    app.run(debug=True)
    cat()
