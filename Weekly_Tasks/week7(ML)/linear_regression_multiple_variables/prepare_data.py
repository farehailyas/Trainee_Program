
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
def get_data_frame():
    data = pd.read_csv("data/vehicle_price_prediction.csv")
    df = pd.DataFrame(data)
    print(df.shape[0])
    return df

def split_data(df):
    features = ['mileage' , 'engine_hp' , 'make' , 'body_type']
    target = 'price'

    X = df[features]
    Y = df[target]

    X_train , X_test, Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state=42)
    print(Y_train.head())
    print(Y_test.head())
    return X_train , X_test, Y_train , Y_test


def target_encoding(X_train , Y_train , X_test ):
    train = X_train.copy()
    train['price'] = Y_train
    # print (train.head)
    make_avg = train.groupby('make')['price'].mean()
    overall_average = Y_train.mean()
    X_train = X_train.copy()
    X_test = X_test.copy()
    X_train['make'] = X_train['make'].map(make_avg)

    X_test['make'] = X_test['make'].map(make_avg).fillna(overall_average)
    print(X_train.head())
    return X_train , X_test , make_avg

def one_hot_encoding(X_train , X_test):
    X_train = X_train.copy()
    X_test = X_test.copy()

    X_train = pd.get_dummies(X_train , columns = ['body_type'] , prefix = 'body').astype('int')
    X_test = pd.get_dummies(X_test , columns = ['body_type'] , prefix = 'body').astype('int')
    X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
    print(X_train.head())
    return X_train , X_test

def feature_scaling(X_train , X_test):
    scaler = StandardScaler()
    X_train = X_train.copy()
    X_test = X_test.copy()

    cols_to_scale = ['engine_hp' , 'mileage' , 'make']
    X_train[cols_to_scale] = scaler.fit_transform( X_train[cols_to_scale] )
    X_test[cols_to_scale] = scaler.transform( X_test[cols_to_scale] )

    return X_train , X_test , scaler

def preprocess_data():

    df = get_data_frame()
    print(df.head())
    X_train , X_test, Y_train , Y_test = split_data(df)
    X_train , X_test , make_avg = target_encoding(X_train, Y_train , X_test)
    X_train , X_test = one_hot_encoding(X_train , X_test )
    X_train , X_test , scaler = feature_scaling(X_train , X_test)

    return X_train , X_test, Y_train , Y_test
    