from flask import Flask, request, jsonify
import random, string

app = Flask(__name__)

@app.route("/post/string", methods=["POST"])
def post_string():
    pass_length = request.json
    return "".join(random.choice(string.ascii_letters) for i in range(pass_length-1))

if __name__ == "__main__":
    app.run(host="0.0.0.0")


