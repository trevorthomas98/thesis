import pandas as pd

youtubecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_youtube.csv'
#facebookcsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_facebook.csv'
#vimeocsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_vimeo.csv'
#rumblecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_rumble.csv'

# Read the CSV file into a pandas DataFrame
chunk_size = 10000
df = []
for chunk in pd.read_csv(youtubecsv_file_path, chunksize=chunk_size):
    df.append(chunk)
youtubedf = pd.concat(df, ignore_index=True)
#youtubedf = pd.read_csv(youtubecsv_file_path)
print("Youtube df.head is")
print(youtubedf.head)

#facebookdf = pd.read_csv(facebookcsv_file_path)
#print("Facebook df.head is")
#print(Facebookdf.head)

#vimeodf = pd.read_csv(vimeocsv_file_path)
#print("Vimeo df.head is")
#print(Vimeodf.head)

#rumbledf = pd.read_csv(rumblecsv_file_path)
#print("Rumble df.head is")
#print(Rumbledf.head)

with open('X_train_NoDef.pkl', 'wb') as handle:
    pickle.dump(youtubedf)


