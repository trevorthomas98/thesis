from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
import os

def learning(df):

### Drop v_id, length, last_packet_time and all "t" columns
    pickle_file_path = '/home/trevor.thomas/youtubedf.pkl'
    df = pd.read_pickle(pickle_file_path)
    #df = df.loc[:, ~df.columns.str.startswith('t')]

    print("Dropping columns such as video id etc")
    #X = df.drop(['v_id','length', 'last_packet_time'], axis=1)
    df = df.drop(['video_id'], axis=1)
    df = df.drop(['num_of_packets'], axis=1)
    df = df.drop(['platform'], axis=1)
    df = df.drop(['entry_ip'], axis=1)
    df = df.drop(['crawl_identifier'], axis=1)
    df = df.drop(['region'], axis=1)
    df = df.drop(['genre'], axis=1)
    X = df



    
    #X = df.drop(['video_id', 'num_of_packets', 'platform' , 'entry_ip' , 'crawl_identifier' ,  'region' , 'genre'], axis=1)

    X.drop(df.iloc[:, :4000], inplace=True, axis=1)
    X.drop(df.iloc[:, 9000:], inplace=True, axis=1)    
  
    
    print("X df is: ")
    print(X)
    print(X.shape)
    
    #y = df[['v_id']]
    y = df[['genre']]

    print("y df is just genre")
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
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

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
    
    no_def_dir = "/home/trevor.thomas/thesis/new/my-thesis/code/df/dataset/ClosedWorld/NoDef/"
    walkie_talkie_dir = "/home/trevor.thomas/thesis/new/my-thesis/code/df/dataset/ClosedWorld/WalkieTalkie/"
    wtf_pad_dir = "/home/trevor.thomas/thesis/new/my-thesis/code/df/dataset/ClosedWorld/WTFPAD/"
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
    with open(walkie_talkie_dir + 'X_train_WalkieTalkie.pkl', 'wb') as handle:
        pickle.dump(X_train, handle)
    #y_train_WalkieTalkie
    with open(walkie_talkie_dir + 'y_train_WalkieTalkie.pkl', 'wb') as handle:
        pickle.dump(y_train, handle)
    #X_train_WTFPAD
    with open(wtf_pad_dir + 'X_train_WTFPAD.pkl', 'wb') as handle:
        pickle.dump(X_train, handle)
    #y_train_WTFPAD
    with open(wtf_pad_dir + 'y_train_WTFPAD.pkl', 'wb') as handle:
        pickle.dump(y_train, handle)
        
        
## Validation
    #X_valid_NoDef
    with open(no_def_dir + 'X_valid_NoDef.pkl', 'wb') as handle:
        pickle.dump(X_valid, handle)
    #y_valid_NoDef    
    with open(no_def_dir + 'y_valid_NoDef.pkl', 'wb') as handle:
        pickle.dump(y_valid, handle)
    #X_valid_WalkieTalkie
    with open(walkie_talkie_dir + 'X_valid_WalkieTalkie.pkl', 'wb') as handle:
        pickle.dump(X_valid, handle)
    #y_valid_WalkieTalkie  
    with open(walkie_talkie_dir + 'y_valid_WalkieTalkie.pkl', 'wb') as handle:
        pickle.dump(y_valid, handle)
    #X_valid_WTFPAD
    with open(wtf_pad_dir + 'X_valid_WTFPAD.pkl', 'wb') as handle:
        pickle.dump(X_valid, handle)
    #y_valid_WTFPAD
    with open(wtf_pad_dir + 'y_valid_WTFPAD.pkl', 'wb') as handle:
        pickle.dump(y_valid, handle)
        
        
        
## Test
    #X_test_NoDef
    with open(no_def_dir + 'X_test_NoDef.pkl', 'wb') as handle:
        pickle.dump(X_test, handle)
    #y_test_NoDef    
    with open(no_def_dir + 'y_test_NoDef.pkl', 'wb') as handle:
        pickle.dump(y_test, handle)
    #X_test_WalkieTalkie
    with open(walkie_talkie_dir + 'X_test_WalkieTalkie.pkl', 'wb') as handle:
        pickle.dump(X_test, handle)
    #y_test_WalkieTalkie    
    with open(walkie_talkie_dir + 'y_test_WalkieTalkie.pkl', 'wb') as handle:
        pickle.dump(y_test, handle)
    #X_test_WTFPAD
    with open(wtf_pad_dir + 'X_test_WTFPAD.pkl', 'wb') as handle:
        pickle.dump(X_test, handle)
    #y_test_WTFPAD    
    with open(wtf_pad_dir + 'y_test_WTFPAD.pkl', 'wb') as handle:
        pickle.dump(y_test, handle)

    
    
    print("X_train", X_train.shape)
    print("y_train", y_train.shape)
    print("X_valid", X_valid.shape)
    print("y_valid", y_valid.shape)
    
    
    
    
    
    
    
    
    
