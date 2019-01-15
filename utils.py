import pickle

def save_pickle(filename, obj):
    with open(filename, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_pickle(filename):                    
    with open(filename, 'rb') as handle:
        b = pickle.load(handle)
    return b