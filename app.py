from flask import Flask, json, jsonify,request

from DB.db_pockemon import DB_Pockemon
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Pockemon back-end per sasi'


#ok
@app.route('/getPockemon')
def structures():
    db_pockemon = DB_Pockemon()
    result = db_pockemon.getPockemons()
    print(jsonify(result))
    return jsonify(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
