import os
import numpy as np
import argparse

def get_args():
    parser = argparse.ArgumentParser("Python Script tot create trainvain.txt file")
    parser.add_argument("--path", type= str, default="data")
    args = parser.parse_args()
    return args

def generate_txt_files(opt):
    files = os.listdir(opt.path)
    train = open("train.txt", "w")
    train_val = open("trainval.txt", "w")
    val = open("val.txt", "w")

    size_train_set = int(len(files) * 0.6)
    size_train_val_set = int(len(files) * 0.2)
    size_val_set = int(len(files) * 0.2)

    train_files = np.random.choice(files, size=size_train_set, replace=False)
    for f in train_files:
        train.write(f.replace(".jpg", "") + "\n")
        files.remove(f)
    train.close()

    train_val_files = np.random.choice(files, size=size_train_val_set, replace=False)
    for f in train_val_files:
        train_val.write(f.replace(".jpg", "") + "\n")
        files.remove(f)
    train_val.close()

    val_files = np.random.choice(files, size=size_val_set, replace=False)
    for f in val_files:
        val.write(f.replace(".jpg", "") + " " + "\n")
        files.remove(f)
    val.close()
    print(len(files))

if __name__ == "__main__":
    opt = get_args()
    generate_txt_files(opt)
