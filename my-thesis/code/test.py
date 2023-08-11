import pandas as pd
import pickle
import learning_5000

pickle_file_path = '/home/trevor.thomas/youtubedf.pkl'
df = pd.read_pickle(pickle_file_path)

def main():


    learning_5000.learning(df)

main()
