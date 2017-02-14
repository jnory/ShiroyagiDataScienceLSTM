import os

import numpy as np
import pandas as pd

np.random.seed(151)  # noqa

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, TimeDistributed, Dense, Dropout
from keras.callbacks import ModelCheckpoint
import json


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
    model.add(Dropout(0.5))
    model.add(TimeDistributed(Dense(1, activation="tanh")))
    model.compile(loss="mean_squared_error", optimizer="adam")

    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "../notebooks/data/hiden_no_tare_enshu1")

    callback = ModelCheckpoint(
        filepath=path + ".h5", verbose=1, save_best_only=True)

    history = model.fit(
        train_X, train_Y, nb_epoch=10000, verbose=2,
        validation_split=0.1, callbacks=[callback])
    with open(path + ".json", "w") as fp:
        fp.write(json.dumps(history.history))


def main():
    train = load()
    train_f = scale(train)
    train_X, train_Y = convert_to_keras_format(train_f)
    fit(train_X, train_Y)

if __name__ == '__main__':
    main()
