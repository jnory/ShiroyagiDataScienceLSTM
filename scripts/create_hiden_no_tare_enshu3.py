import os

import numpy as np
import pandas as pd

np.random.seed(151)  # noqa

from keras.models import Sequential
from keras.layers import LSTM, TimeDistributed, Dense, Dropout, Masking, \
    Activation, Embedding
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.callbacks import LambdaCallback
import json


def load():
    base = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(
            base,
            "../notebooks/data/Gourmet.json",
    )) as fp:
        data = json.loads(fp.read())
    train = data["train"]

    wdic = {}
    wdic_inv = ["</s>"]
    wdic["</s>"] = 0

    count = 1
    for words in train:
        for w in words:
            if w not in wdic:
                wdic[w] = count
                wdic_inv.append(w)
                count += 1
    return train, wdic, wdic_inv


def to_ids(train, wdic):
    train_ids = []
    for words in train:
        ids = []
        for w in words:
            ids.append(wdic[w])
        ids.append(wdic["</s>"])
        train_ids.append(ids)

    train_ids = pad_sequences(
        train_ids, padding="post", value=wdic["</s>"])
    train_x = train_ids[:, :-1]
    train_y = to_categorical(train_ids[:, 1:]).reshape((train_ids.shape[0], train_ids.shape[1] - 1, -1))
    return train_x, train_y


def print_sample(epoch, logs, model, train, train_x, wdic_inv):
    if epoch == 0:
        print("*** Sample Sentence ***")
        print(" ".join(train[0]))

    if epoch % 20 != 0:
        return

    print("*** {} ***".format(epoch))
    print("Loss = {}".format(logs["loss"]))
    print("Val Loss = {}".format(logs["val_loss"]))
    print("Accuracy = {}".format(logs["acc"]))
    print("Val Accuracy = {}".format(logs["val_acc"]))

    pred = model.predict_classes(train_x[:1], verbose=0)[0]
    words = []
    for wid in pred:
        words.append(wdic_inv[wid])
        if len(words) >= len(train[0]):
            break
    print(" ".join(words))


def fit(train_x, train_y, train, wdic, wdic_inv):
    model = Sequential()
    model.add(Embedding(len(wdic)+1, 100, mask_zero=True))
    model.add(LSTM(output_dim=100, return_sequences=True))
    model.add(Dropout(0.5))
    model.add(Activation("tanh"))
    model.add(TimeDistributed(Dense(len(wdic), activation="softmax")))
    model.compile(
        loss="categorical_crossentropy",
        optimizer="adam", metrics=["accuracy"])

    def print_sample_sentence(epoch, logs):
        print_sample(epoch, logs, model, train, train_x, wdic_inv)

    lmd = LambdaCallback(on_epoch_end=print_sample_sentence)

    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "../notebooks/data/hiden_no_tare_enshu3")

    chk = ModelCheckpoint(
        filepath=path + ".h5", verbose=1, save_best_only=True)

    batch_size = 800
    logs = []
    for i in range(20):
        n_data = (i + 1) * train_x.shape[1] // 5
        history = model.fit(
            train_x[:n_data], train_y[:n_data], batch_size=batch_size,
            nb_epoch=200, verbose=0, callbacks=[lmd], validation_split=0.1)
        logs.append(history.history)

    history = model.fit(
        train_x, train_y, batch_size=batch_size,
        nb_epoch=10000, verbose=0, callbacks=[chk, lmd], validation_split=0.1)
    model.save(path + ".final.h5")
    logs.append(history.history)
    with open(path + ".json") as fp:
        fp.write(json.dumps(logs))


def main():
    train, wdic, wdic_inv = load()
    train_x, train_y = to_ids(train, wdic)
    fit(train_x, train_y, train, wdic, wdic_inv)

if __name__ == '__main__':
    main()
