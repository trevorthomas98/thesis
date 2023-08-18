from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
import os

def learning(df):

### Drop v_id, length, last_packet_time and all "t" columns
    #pickle_file_path = '/home/trevor.thomas/facebookdf.pkl'
    #pickle_file_path = '/home/trevor.thomas/rumbledf.pkl'
    #pickle_file_path = '/home/trevor.thomas/vimeodf.pkl'
    pickle_file_path = '/home/trevor.thomas/youtubedf.pkl'
    df = pd.read_pickle(pickle_file_path)

    #df = df.loc[:, ~df.columns.str.startswith('t')]

    print("Dropping columns such as region, crawl id etc")
    #X = df.drop(['v_id','length', 'last_packet_time'], axis=1)
    #df = df.drop(['video_id'], axis=1)
    df = df.drop(['region'], axis=1)
    df = df.drop(['num_of_packets'], axis=1)
    df = df.drop(['platform'], axis=1)
    df = df.drop(['entry_ip'], axis=1)
    df = df.drop(['crawl_identifier'], axis=1)
    df = df.drop(['genre'], axis=1)
    #df = pd.get_dummies(df, columns=['genre'])
    #column_name = 'genre'  # Replace this with the actual column name

    # Print the specified column
    #print(df[column_name])
    print(df.head())
    #X = df.drop(['genre'], axis=1)
    #X = df.drop(['video_id'], axis=1)
    X= df

    print(X.head())


    print("X df is: ")
    print(X)
    print(X.shape)
    
    #y = df[['v_id']]
    y = df[['video_id']]

    # Define a mapping of categorical values to numerical values for genre
    # video id is already a numerical value
    
    #genre_mapping = {
    #    'instruction': 0,
    #    'animated': 1,
    #    'orchestra': 2,
    #    'nature': 3,
    #    'sports': 4,
    #    'news': 5
    #}

    # Create a new column with the encoded values for genre
    #y['encoded_genre'] = y['genre'].map(genre_mapping)

    #video id mapping for youtube
    id_mapping = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,        
        '120': 10,
        '121': 11,
        '122': 12,
        '123': 13,
        '124': 14,
        '125': 15,
        '126': 16,
        '127': 17,
        '128': 18,
        '129': 19,
        '160': 20,
        '161': 21,
        '162': 22,
        '163': 23,
        '164': 24,
        '165': 25,
        '166': 26,
        '167': 27,
        '168': 28,
        '169': 29,
        '200': 30,
        '201': 31,
        '202': 32,
        '203': 33,
        '204': 34,
        '205': 35,
        '206': 36,
        '207': 37,
        '208': 38,
        '209': 39,
        '40': 40,
        '41': 41,
        '42': 42,
        '43': 43,
        '44': 44,
        '45': 45,
        '46': 46,
        '47': 47,
        '48': 48,
        '49': 49,
        '80': 50,
        '81': 51,
        '82': 52,
        '83': 53,
        '84': 54,
        '85': 55,
        '86': 56,
        '87': 57,
        '88': 58,
        '89': 59,
        
    }

    #video id mapping for vimeo
    # id_mapping = {
    #     '100': 0,
    #     '101': 1,
    #     '102': 2,
    #     '103': 3,
    #     '104': 4,
    #     '105': 5,
    #     '106': 6,
    #     '107': 7,
    #     '108': 8,
    #     '109': 9,        
    #     '140': 10,
    #     '141': 11,
    #     '142': 12,
    #     '143': 13,
    #     '144': 14,
    #     '145': 15,
    #     '146': 16,
    #     '147': 17,
    #     '148': 18,
    #     '149': 19,
    #     '180': 20,
    #     '181': 21,
    #     '182': 22,
    #     '183': 23,
    #     '184': 24,
    #     '185': 25,
    #     '186': 26,
    #     '187': 27,
    #     '188': 28,
    #     '189': 29,
    #     '20': 30,
    #     '21': 31,
    #     '22': 32,
    #     '23': 33,
    #     '24': 34,
    #     '25': 35,
    #     '26': 36,
    #     '27': 37,
    #     '28': 38,
    #     '29': 39,
    #     '220': 40,
    #     '221': 41,
    #     '222': 42,
    #     '223': 43,
    #     '224': 44,
    #     '225': 45,
    #     '226': 46,
    #     '227': 47,
    #     '228': 48,
    #     '229': 49,
    #     '60': 50,
    #     '61': 51,
    #     '62': 52,
    #     '63': 53,
    #     '64': 54,
    #     '65': 55,
    #     '66': 56,
    #     '67': 57,
    #     '68': 58,
    #     '69': 59,
        
    # }

    
    #video id mapping for rumble
    # id_mapping = {
    #     '110': 0,
    #     '111': 1,
    #     '112': 2,
    #     '113': 3,
    #     '114': 4,
    #     '115': 5,
    #     '116': 6,
    #     '117': 7,
    #     '118': 8,
    #     '119': 9,        
    #     '150': 10,
    #     '151': 11,
    #     '152': 12,
    #     '153': 13,
    #     '154': 14,
    #     '155': 15,
    #     '156': 16,
    #     '157': 17,
    #     '158': 18,
    #     '159': 19,
    #     '190': 20,
    #     '191': 21,
    #     '192': 22,
    #     '193': 23,
    #     '194': 24,
    #     '195': 25,
    #     '196': 26,
    #     '197': 27,
    #     '198': 28,
    #     '199': 29,
    #     '230': 30,
    #     '231': 31,
    #     '232': 32,
    #     '233': 33,
    #     '234': 34,
    #     '235': 35,
    #     '236': 36,
    #     '237': 37,
    #     '238': 38,
    #     '239': 39,
    #     '30': 40,
    #     '31': 41,
    #     '32': 42,
    #     '33': 43,
    #     '34': 44,
    #     '35': 45,
    #     '36': 46,
    #     '37': 47,
    #     '38': 48,
    #     '39': 49,
    #     '70': 50,
    #     '71': 51,
    #     '72': 52,
    #     '73': 53,
    #     '74': 54,
    #     '75': 55,
    #     '76': 56,
    #     '77': 57,
    #     '78': 58,
    #     '79': 59,
        
    # }

    #video id mapping for facebook
    # id_mapping = {
    #     '10': 0,
    #     '11': 1,
    #     '12': 2,
    #     '13': 3,
    #     '14': 4,
    #     '15': 5,
    #     '16': 6,
    #     '17': 7,
    #     '18': 8,
    #     '19': 9,        
    #     '130': 10,
    #     '131': 11,
    #     '132': 12,
    #     '133': 13,
    #     '134': 14,
    #     '135': 15,
    #     '136': 16,
    #     '137': 17,
    #     '138': 18,
    #     '139': 19,
    #     '170': 20,
    #     '171': 21,
    #     '172': 22,
    #     '173': 23,
    #     '174': 24,
    #     '175': 25,
    #     '176': 26,
    #     '177': 27,
    #     '178': 28,
    #     '179': 29,
    #     '210': 30,
    #     '211': 31,
    #     '212': 32,
    #     '213': 33,
    #     '214': 34,
    #     '215': 35,
    #     '216': 36,
    #     '217': 37,
    #     '218': 38,
    #     '219': 39,
    #     '50': 40,
    #     '51': 41,
    #     '52': 42,
    #     '53': 43,
    #     '54': 44,
    #     '55': 45,
    #     '56': 46,
    #     '57': 47,
    #     '58': 48,
    #     '59': 49,
    #     '90': 50,
    #     '91': 51,
    #     '92': 52,
    #     '93': 53,
    #     '94': 54,
    #     '95': 55,
    #     '96': 56,
    #     '97': 57,
    #     '98': 58,
    #     '99': 59,
        
    # }



    y['video_id'] = y['video_id'].astype(str)
    X['video_id'] = X['video_id'].astype(str)
    
    # Create a new column with the encoded values for genre
    y['encoded_videoid'] = y['video_id'].map(id_mapping)
    X['encoded_videoid'] = X['video_id'].map(id_mapping)
    # Display the resulting DataFrame
    print("y is",y)
    print("X is",X)
    
    y = y.drop(['video_id'], axis=1)
    X = df.drop(['video_id'], axis=1)


    #print("y df is just genre")
    print("y df is just video id")
    print(y)
    print(y.shape)

### Scale the features
    pipeline = Pipeline([
                    ('std_scaler', StandardScaler()),
                    ])

    df_scaled = pipeline.fit_transform(X)
    X = pd.DataFrame(df_scaled)
    
    
    print("RESULT AFTER FIT AND SCALE! (X)")
    print(X)
    
    
### Change ALL directions columns to "+1 and -1"
    #X[X<0] = -1
    #X[X>0] = 1
    
    print("DATAFRAME AFTER CHANGING DIRECTIONS!")
    print("X:")
    print(X)
    print("len of X before split", len(X))


    #split X df and y df into 0-6 and 7-9 same for 10-16 and 17-19 etc
    #70% to train set, 30% to test set
    #try X_train = larger X df, X_test = smaller X df (after I split and then drop video id)
    #print before dropping video id and then drop after and print again.
    #same for y


    ranges = [(7, 9), (17, 19), (27, 29), (37, 39), (47, 49), (57, 59)]

   # Create a new DataFrame with selected ranges
    selected_rows = X[X['encoded_videoid'].apply(lambda x: any(start <= x <= end for start, end in ranges))]

    # Create a new DataFrame with selected rows
    X_test = selected_rows.copy()

    # Drop selected rows from the original DataFrame
    X = X.drop(selected_rows.index)


    X_train = X



    print("X_test is:")
    print(X_test)
    print("\nOriginal DataFrame after dropping selected rows:")
    print(X_train)


    print("\n now dropping encoded video id from xtest and xtrain:")
    X_test = df.drop(['video_id'], axis=1)
    X_train = df.drop(['video_id'], axis=1)


    
    
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Should be 70/30 split of shape of X
    # Random State is used so samples remain same every run (train/test/split usually data in df)
    print("length of X_train", len(X_train))
    print("length of X_test", len(X_test))
    print("length of y_train", len(y_train))
    print("length of y_test", len(y_test))

    X_valid, X_test, y_valid, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
    print("length of X_valid", len(X_valid))
    print("length of X_test", len(X_test))
    print("length of y_valid", len(y_valid))
    print("length of y_test", len(y_test))
    
    no_def_dir = "/home/trevor.thomas/thesis/my-thesis/code/df/dataset/ClosedWorld/NoDef/"
    #walkie_talkie_dir = "/home/trevor.thomas/thesis/new/my-thesis/code/df/dataset/ClosedWorld/WalkieTalkie/"
    #wtf_pad_dir = "/home/trevor.thomas/thesis/new/my-thesis/code/df/dataset/ClosedWorld/WTFPAD/"
    #no_def_dir = "/home/student/Documents/thesis/small_thesis_project/code/df/dataset/ClosedWorld/NoDef/"
    print(no_def_dir)
# PICKLE DATA
## Training    
    #X_train_NoDef
    with open(no_def_dir + 'X_train_NoDef.pkl', 'wb') as handle:
        pickle.dump(X_train, handle)
    #y_train_NoDef    
    with open(no_def_dir + 'y_train_NoDef.pkl', 'wb') as handle:
        pickle.dump(y_train, handle)
    #X_train_WalkieTalkie
    #with open(walkie_talkie_dir + 'X_train_WalkieTalkie.pkl', 'wb') as handle:
     #   pickle.dump(X_train, handle)
    #y_train_WalkieTalkie
    #with open(walkie_talkie_dir + 'y_train_WalkieTalkie.pkl', 'wb') as handle:
    #    pickle.dump(y_train, handle)
    #X_train_WTFPAD
    #with open(wtf_pad_dir + 'X_train_WTFPAD.pkl', 'wb') as handle:
    #    pickle.dump(X_train, handle)
    #y_train_WTFPAD
    #with open(wtf_pad_dir + 'y_train_WTFPAD.pkl', 'wb') as handle:
    #    pickle.dump(y_train, handle)
        
        
## Validation
    #X_valid_NoDef
    with open(no_def_dir + 'X_valid_NoDef.pkl', 'wb') as handle:
        pickle.dump(X_valid, handle)
    #y_valid_NoDef    
    with open(no_def_dir + 'y_valid_NoDef.pkl', 'wb') as handle:
        pickle.dump(y_valid, handle)
    #X_valid_WalkieTalkie
    #with open(walkie_talkie_dir + 'X_valid_WalkieTalkie.pkl', 'wb') as handle:
    #    pickle.dump(X_valid, handle)
    #y_valid_WalkieTalkie  
    #with open(walkie_talkie_dir + 'y_valid_WalkieTalkie.pkl', 'wb') as handle:
    #    pickle.dump(y_valid, handle)
    #X_valid_WTFPAD
    #with open(wtf_pad_dir + 'X_valid_WTFPAD.pkl', 'wb') as handle:
    #    pickle.dump(X_valid, handle)
    #y_valid_WTFPAD
    #with open(wtf_pad_dir + 'y_valid_WTFPAD.pkl', 'wb') as handle:
    #    pickle.dump(y_valid, handle)
        
        
        
## Test
    #X_test_NoDef
    with open(no_def_dir + 'X_test_NoDef.pkl', 'wb') as handle:
        pickle.dump(X_test, handle)
    #y_test_NoDef    
    with open(no_def_dir + 'y_test_NoDef.pkl', 'wb') as handle:
        pickle.dump(y_test, handle)
    #X_test_WalkieTalkie
    #with open(walkie_talkie_dir + 'X_test_WalkieTalkie.pkl', 'wb') as handle:
    #    pickle.dump(X_test, handle)
    #y_test_WalkieTalkie    
    #with open(walkie_talkie_dir + 'y_test_WalkieTalkie.pkl', 'wb') as handle:
    #    pickle.dump(y_test, handle)
    #X_test_WTFPAD
    #with open(wtf_pad_dir + 'X_test_WTFPAD.pkl', 'wb') as handle:
    #    pickle.dump(X_test, handle)
    #y_test_WTFPAD    
    #with open(wtf_pad_dir + 'y_test_WTFPAD.pkl', 'wb') as handle:
    #    pickle.dump(y_test, handle)

    
    
    print("X_train", X_train.shape)
    print("y_train", y_train.shape)
    print("X_valid", X_valid.shape)
    print("y_valid", y_valid.shape)
    
    
    
    
    
    
    
    
    
