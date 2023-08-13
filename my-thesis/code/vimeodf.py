import pandas as pd
import pickle
import learning_NoDef

#youtubecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_youtube.csv'
#facebookcsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_facebook.csv'
vimeocsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_vimeo.csv'
#rumblecsv_file_path = '/data/timothy.walsh/hayden_monitored_tor_rumble.csv'

# Read the CSV file into a pandas DataFrame
chunk_size = 10000
df = []
for chunk in pd.read_csv(vimeocsv_file_path, chunksize=chunk_size):
    df.append(chunk)
vimeodf = pd.concat(df, ignore_index=True)
#youtubedf = pd.read_csv(youtubecsv_file_path)
print("vimeo df.head is")
print(vimeodf.head)

num_columns = vimeodf.shape[1]
print(f"The DataFrame has {num_columns} columns.")


videoid = 'video_id'  # Specify the new column name

# Rename the 40007th column
vimeodf.rename(columns={vimeodf.columns[40006]: videoid}, inplace=True)

crawljob = 'crawl_identifier'  # Specify the new column name

# Rename the 40006th column
vimeodf.rename(columns={vimeodf.columns[40005]: crawljob}, inplace=True)

numpackets = 'num_of_packets'  # Specify the new column name

# Rename the 40005th column
vimeodf.rename(columns={vimeodf.columns[40004]: numpackets}, inplace=True)

genre = 'genre'  # Specify the new column name

# Rename the 40004th column
vimeodf.rename(columns={vimeodf.columns[40003]: genre}, inplace=True)


platform = 'platform'  # Specify the new column name

# Rename the 40003th column
vimeodf.rename(columns={vimeodf.columns[40002]: platform}, inplace=True)


entryrelay = 'entry_ip'  # Specify the new column name

# Rename the 40002th column
vimeodf.rename(columns={vimeodf.columns[40001]: entryrelay}, inplace=True)

region = 'region'  # Specify the new column name

# Rename the 40001th column
vimeodf.rename(columns={vimeodf.columns[40000]: region}, inplace=True)

# Print the DataFrame to see the results
print(vimeodf)


output_file_path = '/home/trevor.thomas/vimeodf.pkl' 

# Save the DataFrame to a pickle file
vimeodf.to_pickle(output_file_path)

print("DataFrame saved to pickle file.")


def main():


    learning_NoDef.learning(vimeodf)

main()
