import pandas as pd
import pickle
import learning_NoDef

#pickle_file_path = '/home/trevor.thomas/youtubedf.pkl'
#pickle_file_path = '/home/trevor.thomas/vimeodf.pkl'
#pickle_file_path = '/home/trevor.thomas/rumbledf.pkl'
pickle_file_path = '/home/trevor.thomas/facebookdf.pkl'
df = pd.read_pickle(pickle_file_path)
print(df)
def main():


    learning_NoDef.learning(df)

main()
