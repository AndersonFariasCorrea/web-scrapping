import classes.__init__
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def main():
    web = classes.web_scrappy.WebSearch()
    web.foo()


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
    main()

