from flask import Flask
import random

app = Flask(__name__)

def gen_rand_num():
    return str(random.randint(1,99)).zfill(2)
    #return str(random.randint(1,10)).zfill(2)

@app.route("/get/num")
def get_num():
    return gen_rand_num()

if __name__ == "__main__":
    app.run(host="0.0.0.0")