import pickle


def loadData():
    # for reading also binary mode is important
    dbfile = open('../../data/dice.pickle', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

loadData()
