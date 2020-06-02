import pickle

data = {}
data["anubhav"] = 1
data["saikia"] = 2

with open('data.p', 'wb') as fp:
    pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)

new_data = {}

with open('data.p', 'rb') as fp:
    new_data = pickle.load(fp)

print(new_data["anubhav"])