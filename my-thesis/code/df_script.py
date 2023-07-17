import os
import pandas as pd
from collections import OrderedDict

import learning_NoDef



def get_last_packet_time(file):
    ####################################################################
    # Returns the last packet time from one capture
    ####################################################################
    count = 0
    with open(file) as f:
        for line in f:
            count += 1
        if count > 10:
            last_packet_time = line.split()[0]
        else: last_packet_time = 0
    return last_packet_time

def read_stats_file(data_location):
    ####################################################################
    #   Each video set should utilize a stats.txt that contains a list
    #   of the length of each video. This function will read in the 
    #   the lengths of these videos into a list vlengths and also 
    #   create a videos list with the number of videos in the dataset
    ####################################################################
    genre = 0
    count = 0
    with open(data_location + 'stats.txt') as f:
        for line in f.readlines():
            if count == 0: # genre line
                genre = line.split()[1].strip()
                count += 1
        return genre
    
def get_genre_directories(data_location):
    ####################################################################
    # This function will return a list of genre directories (only top level)
    ####################################################################
    for directories in os.walk(data_location, topdown=True):
        data_directories = directories[1]
        break
    return data_directories

def parse_file(file):
    ####################################################################
    # This function will open and parse each capture file to retrieve time and directions
    ####################################################################
    t = []
    d = []

    with open(file, 'rb') as f:
        lines = f.readlines()
        for line in range(0, len(lines)):
            line = lines[line]                
            parts = line.strip().split()
            try:
                t.append(float(parts[0]))
                d.append(float(parts[1]))
            except IndexError:
                break # if there is an error reading file
    return t, d

def iterate_directories(data_location):
    ####################################################################
    # This function iterates through each genre fodler and adds to data frame 
    ####################################################################
    row = 0
    df_dict = {}
    data_directories = get_genre_directories(data_location)

    all_t = []
    all_d = []

    t_and_d_dict = {}
    
    shortest_len = 50000

    for genre_dir in data_directories:
        print("genre started")
        for root, cap_dir, files in os.walk(data_location + genre_dir + '/'):
            for file in files:
#                print(root, file)
                if file[0] == ".":          # ignores hidden git files
                    pass
                elif file == 'stats.txt':
                    genre = read_stats_file(data_location + genre_dir + '/')
                else:
                    v_id = int(file[2])
                    last_packet_time = get_last_packet_time(root + '/' + file)

                    times = []
                    directions = []
                    times, directions = parse_file(root + '/' + file)

                    #print(len(times))
                    if times: 
                        if times[-1] > 100:
                            #print("adding")
                            df_dict["row_"+str(row)] = [genre] + [v_id] + [last_packet_time]
                            t_and_d_dict["row_"+str(row)] = [times] + [directions]
                            row += 1
                            
                            all_t.append(times)
                            all_d.append(directions)
                            
                            if len(directions) < shortest_len:
                                shortest_len = len(directions)
        print("genre done")
    print("shortest trace is of length: ", shortest_len)
    return all_t, all_d, df_dict, t_and_d_dict

def extend_rows(t_and_d_dict, max_t, max_d):
#    print("max t:", max_t)
#    print("max d:", max_d)

    for x in t_and_d_dict.values():
        x[0].extend([float(0.0)] * max_t)
        x[0] = x[0][:max_t]

        x[1].extend([float(0.0)] * max_d)
        x[1] = x[1][:max_d]

def combine_dicts(df_dict, t_and_d_dict):
    for row in df_dict:
        df_dict[row].extend(t_and_d_dict[row][0])
        df_dict[row].extend(t_and_d_dict[row][1])

def make_df(all_t, all_d, df_dict, t_and_d_dict):
    # Make same length
    length_t = max(map(len, all_t))
    t=[xi+[None]*(length_t-len(xi)) for xi in all_t]
            
    length_d = max(map(len, all_d))
    d=[xi+[None]*(length_d-len(xi)) for xi in all_d]

    # Create column names
    t_names=[]
    d_names=[]

#    print("len of t_names:", len(t_names))
#    print("len of d_names:", len(d_names))
    
    for i in range(0,len(t[0])):
        t_names.append('t'+str(i))
        d_names.append('d'+str(i))
    
    extend_rows(t_and_d_dict, length_t, length_d)
    combine_dicts(df_dict, t_and_d_dict)

    df = pd.DataFrame.from_dict(df_dict, orient="index")
    df.columns = ['genre'] + ['v_id'] + ['last_packet_time'] + t_names + d_names
    return df


def print_df_genre(df, genre):
    # condition mask
    mask = df['genre'] == genre

    # new dataframe with selected rows
    df_new = pd.DataFrame(df[mask])
    print("PRINTING GENRE: ", genre)
    print(df_new)
    
def main():
    data_location = os.path.dirname(os.getcwd()) + "/data/"
    data_location = "/data/timothy.walsh/monitored_tor"
    #data_location = "/home/student/Documents/thesis/small_thesis_project/data/"
    print("Found data at: ", data_location)
    
    all_t, all_d, pd_dict, t_and_d_dict = iterate_directories(data_location)

    print("Length of df: ", len(pd_dict))

    df = make_df(all_t, all_d, pd_dict, t_and_d_dict)
    #print("DF Info:", df.info)
    
    print_df_genre(df, "0")
    print_df_genre(df, "1")
    print_df_genre(df, "2")
    print_df_genre(df, "3")

    learning_NoDef.learning(df)

main()