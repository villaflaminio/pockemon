from DB.db_pokemon import DB_Pokemon
import time


def test():
    db_places = DB_Pokemon()

    for i in range(568, 898):
        db_places.getPokemonAPI(i)
        time.sleep(0.02)


if __name__ == '__main__':
     #test()
    print("il test carica tuti i dati nel db")


