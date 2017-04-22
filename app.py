import tensorflow as tf
from flask import Flask

sess = tf.Session()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return str(sess.run(tf.abs(-1)))


if __name__ == '__main__':
    app.run()
