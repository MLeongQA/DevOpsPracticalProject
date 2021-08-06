from flask import Flask
import random, string

app = Flask(__name__)

pass_length = random.randint(1,10)
def gen_rand_string(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))

@app.route("/get/string")
def get_string():
    return gen_rand_string(pass_length-2)

if __name__ == "__main__":
    app.run(host="0.0.0.0")