import random
import pandas as pd

# Sample data
names = ["James", "Mary", "John", "Patricia", "Robert", "Linda"]
df = pd.read_csv('allnames.csv')
names = df.Name.tolist()

def pickandwin(n):
    random.seed(n)
    winner = random.choice(names)
    return(winner)
