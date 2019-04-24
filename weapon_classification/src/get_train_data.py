# -*- coding: utf-8 -*-

import os
import json

def read_json(filepath):

    names = []
    types = []
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.readlines()

    for line in text:
        eq_dict = json.loads(line)
        name = eq_dict['name'][0]
        type = eq_dict['title'][0]
        names.append(name)
        types.append(type)

    return names, types


def write_file(project_dir):
    with open('./train.csv', 'w', encoding='utf-8') as f:
        f.write('eq,label\n')
        for file in os.listdir(project_dir):
            names, types = read_json(project_dir+'/'+file)
            for name, type in zip(names, types):
                name = name.replace(',', '，')
                f.write(name+','+type+'\n')

project_dir = '../data/weapons'
write_file(project_dir)