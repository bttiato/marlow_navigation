import os
uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
ROOT_DIR = uppath(__file__, 2)

import yaml
import csv

def parse_config(filename = "input.conf"):
    file_path = f'{ROOT_DIR}/config/{filename}'

    with open(file_path, "r") as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)

    return config

def parse_csv(filename= "data.csv"):
    file_path = f'{ROOT_DIR}/data/{filename}'

    with open(file_path, 'r') as f:
        data = [tuple(line) for line in csv.reader(f)][1:]
    return data
