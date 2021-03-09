from DB.db_pockemon import DB_Pockemon
import time


def test():
    db_places = DB_Pockemon()

    for i in range(568, 898):
        db_places.getPockemonAPI(i)
        time.sleep(0.02)


if __name__ == '__main__':
     #test()
    print("il test carica tuti i dati nel db")


