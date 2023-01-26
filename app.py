from flask import Flask, jsonify
import gdown

app = Flask(__name__)


@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/1ewfDylbtVmWAkIHoTXqU44y0rPL_RfAZ', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
