import time
from tinydb import TinyDB, Query
from utils.Singleton import Singleton
import requests
import json

class DB_Pockemon(metaclass=Singleton):
    db = None
    def __init__(self):
        self.db = TinyDB('pockemon.json')

    def addPockemon(self, pockemon):
        return self.db.insert(pockemon)

    def getPockemons(self):
        pockemon = self.db.all()
        return pockemon

    def getPockemonAPI(self, number):
        solditems = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(number))  # (your url)
        dataRequest = solditems.json()
        sprites = dataRequest["sprites"]

        types = dataRequest["types"]
        subTypes = []
        for p in types:
            nameType = p['type']
            subTypes.append(nameType['name'])

        dictToSend = {
            'name': dataRequest["name"],
            'back_default': sprites["back_default"],
            'front_default': sprites["front_default"],
            'types': subTypes
        }

        print(dictToSend)
        self.addPockemon(dictToSend)