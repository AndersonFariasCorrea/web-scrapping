from scrapping_core.__init__ import scrappingCore
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=['GET', 'POST'])
def api():
    model_search = request.args.get('busca')
    sites = request.args.get('sites')

    if not model_search:
        return jsonify({"status": 400, "msg": "formulário inválido"})

    if not sites:
        sites = ['Kabum', 'Pichau']

    web = scrappingCore.WebSearch(sites)

    res = web.search(model_search)
    if res[0].content:
        return jsonify(res[0].content)
    else:
        return jsonify({"status": 404, "msg": "not found"})


def main():
    pass


if __name__ == "__main__":
    # main()
    app.run(debug=True, port=5000, host='0.0.0.0')
