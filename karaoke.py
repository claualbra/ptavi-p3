#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import sys
import smallsmilhandler
from xml.sax import make_parser


if __name__ == "__main__":
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSmilHandler()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    lista = cHandler.get_tags()
    with open('karaoke.json', 'w') as file:
        json.dump(lista, file, indent=4)
    line_et = ''
    for diccionario in lista:
        line_et = diccionario['etiqueta']
        diccionario['etiqueta'] = 'etiqueta'
        for atributo, valor in diccionario.items():
            if valor.startswith('http://'):
                file_local = valor[valor.rfind('/'):]
                urllib.request.urlretrieve(valor, file_local[1:])
            if atributo != diccionario['etiqueta'] and valor != "":
                line_et += '\t'+'{0}="{1}"'.format(atributo, valor)
        print(line_et)
