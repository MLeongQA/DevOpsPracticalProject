from flask import Flask, request, jsonify
import random, string

app = Flask(__name__)

string_list = string.ascii_letters
#string_list = string.ascii_lowercase

@app.route("/post/string", methods=["POST"])
def post_string():
    pass_length = request.json
    return "".join(random.choice(string_list) for i in range(pass_length-2))

if __name__ == "__main__":
    app.run(host="0.0.0.0")


