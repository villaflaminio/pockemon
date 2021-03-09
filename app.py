from flask import Flask, json, jsonify,request

from DB.db_pokemon import DB_Pokemon
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Pokemon back-end per sasi'


#ok
@app.route('/getPokemon')
def structures():
    db_pokemon = DB_Pokemon()
    result = db_pokemon.getPokemons()
    print(jsonify(result))
    return jsonify(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
