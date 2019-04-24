# -*- coding: utf-8 -*-

import json

with open('lianshang_train.csv', 'w', encoding='utf-8') as g:
    g.write('eq,label\n')
    with open('fulldata', 'r', encoding='utf-8') as f:
        t = f.readlines()
        for line in t:
            product = json.loads(line.strip())
            if 'title' in product.keys() and 'cat1_name' in product.keys():
                eq = product['title']
                eq = eq.replace(',', '，')
                label = product['cat1_name']
                print(eq, label)
                g.write(eq+','+label+'\n')