from flask import Flask, jsonify
from dotenv import dotenv_values

app = Flask(__name__)

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
    app.run(debug=True, port=5000)
