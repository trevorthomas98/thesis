import pandas as pd
import pickle
import learning_NoDef

#youtubecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_youtube.csv'
facebookcsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_facebook.csv'
#vimeocsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_vimeo.csv'
#rumblecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_rumble.csv'

# Read the CSV file into a pandas DataFrame
chunk_size = 10000
df = []
for chunk in pd.read_csv(facebookcsv_file_path, chunksize=chunk_size):
    df.append(chunk)
facebookdf = pd.concat(df, ignore_index=True)
#youtubedf = pd.read_csv(youtubecsv_file_path)
print("facebook df.head is")
print(facebookdf.head)

num_columns = facebookdf.shape[1]
print(f"The DataFrame has {num_columns} columns.")


videoid = 'video_id'  # Specify the new column name

# Rename the 40007th column
facebookdf.rename(columns={facebookdf.columns[40006]: videoid}, inplace=True)

crawljob = 'crawl_identifier'  # Specify the new column name

# Rename the 40006th column
facebookdf.rename(columns={facebookdf.columns[40005]: crawljob}, inplace=True)

numpackets = 'num_of_packets'  # Specify the new column name

# Rename the 40005th column
facebookdf.rename(columns={facebookdf.columns[40004]: numpackets}, inplace=True)

genre = 'genre'  # Specify the new column name

# Rename the 40004th column
facebookdf.rename(columns={facebookdf.columns[40003]: genre}, inplace=True)


platform = 'platform'  # Specify the new column name

# Rename the 40003th column
facebookdf.rename(columns={facebookdf.columns[40002]: platform}, inplace=True)


entryrelay = 'entry_ip'  # Specify the new column name

# Rename the 40002th column
facebookdf.rename(columns={facebookdf.columns[40001]: entryrelay}, inplace=True)

region = 'region'  # Specify the new column name

# Rename the 40001th column
facebookdf.rename(columns={facebookdf.columns[40000]: region}, inplace=True)

# Print the DataFrame to see the results
print(facebookdf)


output_file_path = '/home/trevor.thomas/facebookdf.pkl' 

# Save the DataFrame to a pickle file
facebookdf.to_pickle(output_file_path)

print("DataFrame saved to pickle file.")


def main():


    learning_NoDef.learning(facebookdf)

main()
