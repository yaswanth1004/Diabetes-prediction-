import pickle

with open('Final_Forest.pkl', 'rb') as f:
    model = pickle.load(f)

print(model)
