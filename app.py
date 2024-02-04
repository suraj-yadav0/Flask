from flask import Flask, request , jsonify

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def index():
    d={}
    d['Querry'] = str(request.args['Querry'])
    return jsonify(d)


if __name__ == "__main__":
    app.run(debug=True)