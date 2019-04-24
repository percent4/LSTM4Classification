# -*- coding: utf-8 -*-

import os

with open('./sent_train.csv', 'w', encoding='utf-8') as g:
    g.write('eq,label\n')
    for file in os.listdir('.'):
        if file.endswith('txt'):
            with open(file, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    line = line.strip().replace(',', '，')
                    g.write(line+','+file.replace('.txt', '')+'\n')

