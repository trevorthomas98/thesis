import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = '/home/trevor.thomas/df_monitored_tor.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)
print(df.head)

# Create separate dataframes for each hosting platform
rumble_df = df[df['hosting_platform'] == 'rumble'].copy()
youtube_df = df[df['hosting_platform'] == 'youtube'].copy()
vimeo_df = df[df['hosting_platform'] == 'vimeo'].copy()
facebook_df = df[df['hosting_platform'] == 'facebook'].copy()

# Now you have separate dataframes for each hosting platform.
# You can access and manipulate the data in each dataframe as needed.

# Example: Print the first 5 rows of the rumble dataframe
print("Data for Rumble Hosting Platform:")
print(rumble_df.head())

# Example: Save each dataframe to a separate CSV file
rumble_df.to_csv('rumble_data.csv', index=False)
youtube_df.to_csv('youtube_data.csv', index=False)
vimeo_df.to_csv('vimeo_data.csv', index=False)
facebook_df.to_csv('facebook_data.csv', index=False)

# You can perform further data analysis or operations on each dataframe as needed.
