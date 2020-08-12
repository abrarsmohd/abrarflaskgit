from flask import flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return ("Hello World")

if __name__ == "__main__":
    app.run()