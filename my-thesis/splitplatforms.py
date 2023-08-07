import pandas as pd

youtubecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_youtube.csv'
facebookcsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_facebook.csv'
vimeocsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_vimeo.csv'
rumblecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_rumble.csv'

# Read the CSV file into a pandas DataFrame
youtubedf = pd.read_csv(youtubecsv_file_path)
print("Youtube df.head is")
print(youtubedf.head)

facebookdf = pd.read_csv(facebookcsv_file_path)
print("Facebook df.head is")
print(Facebookdf.head)

vimeodf = pd.read_csv(vimeocsv_file_path)
print("Vimeo df.head is")
print(Vimeodf.head)

rumbledf = pd.read_csv(rumblecsv_file_path)
print("Rumble df.head is")
print(Rumbledf.head)

youtubedf.to_csv('youtubedata.csv', index=False)
facebookdf.to_csv('facebookdata.csv', index=False)
vimeodf.to_csv('vimeodata.csv', index=False)
rumbledf.to_csv('rumbledata.csv', index=False)

