from flask import Flask, jsonify, request
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__)

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})

def get_port() -> int:
    config = dotenv_values(".env")
    return int(config.get("PORT", 5000))

@app.route("/")
def server_info():
    return "My server"

@app.route("/author")
def author():
    author = {
        "name": "Gleb",
        "course": 2,
        "age": 19,
    }
    return jsonify(author)

if __name__ == "__main__":
    app.run(debug=True, port=get_port())
