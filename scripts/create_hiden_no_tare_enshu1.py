import os

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, TimeDistributed, Dense


def load():
    base = os.path.dirname(os.path.abspath(__file__))
    train = pd.read_csv(
        os.path.join(base, "../notebooks/data/train_enshu1.csv"))

    train = pd.pivot_table(
        train, index="Date/Time", columns="Base", values="count")
    return train


def scale(train):
    diff_ma_train = train - train.rolling(7).mean()
    diff_ma_train.dropna(inplace=True)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    train_f = scaler.fit_transform(diff_ma_train.values.astype(np.float32))
    return train_f


def convert_to_keras_format(train_f):
    train_X = train_f[:-1].T.reshape((5, 146, 1))
    train_Y = train_f[1:].T.reshape((5, 146, 1))
    return train_X, train_Y


def fit(train_X, train_Y):
    model = Sequential()
    model.add(LSTM(input_dim=1, output_dim=10, return_sequences=True))
    model.add(TimeDistributed(Dense(1)))
    model.compile(loss="mean_squared_error", optimizer="adam")

    model.fit(train_X, train_Y, nb_epoch=100000, verbose=2)
    return model


def main():
    train = load()
    train_f = scale(train)
    train_X, train_Y = convert_to_keras_format(train_f)
    model = fit(train_X, train_Y)
    base = os.path.dirname(os.path.abspath(__file__))
    model.save(
        os.path.join(base, "../notebooks/data/hiden_no_tare_enshu1.h5"))


if __name__ == '__main__':
    main()
