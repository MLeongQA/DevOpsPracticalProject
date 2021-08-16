from flask import Flask, request, jsonify
from zxcvbn import zxcvbn
import string 

app = Flask(__name__)

char_list = list(string.ascii_letters) + [i for i in range (1,100)]

@app.route("/post/password", methods=["POST"])
def post_password():
    gen_pass = request.data.decode()

    results = zxcvbn(gen_pass, user_inputs=char_list)
    #return jsonify(5)
    return jsonify(results.get('score'))


if __name__ == "__main__":
    app.run(host="0.0.0.0")