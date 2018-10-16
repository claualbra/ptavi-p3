#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import sys
import smallsmilhandler
from xml.sax import make_parser


class KaraokeLocal:
    def __init__(self, file):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSmilHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        self.lista = cHandler.get_tags()

    def __str__(self):
        line_etiqueta = ''
        for diccionario in self.lista:
            nom_etiqueta = diccionario['etiqueta']
            line_etiqueta += diccionario['etiqueta']
            diccionario['etiqueta'] = 'etiqueta'
            for atributo, valor in diccionario.items():
                if atributo != diccionario['etiqueta'] and valor != "":
                    line_etiqueta += '\t'+'{0}="{1}"'.format(atributo, valor)
            line_etiqueta += '\n'
            diccionario['etiqueta'] = nom_etiqueta
        return line_etiqueta

    def to_json(self, file):
        file_json = ''
        if file_json == '':
            file_json = file.replace('.smil', '.json')
        with open(file_json, 'w') as f:
            json.dump(self.lista, f, indent=4)

    def do_local(self):
        for diccionario in self.lista:
            for atributo, valor in diccionario.items():
                if atributo == 'src':
                    if valor.startswith('http://'):
                        file_local = valor[valor.rfind('/'):]
                        urllib.request.urlretrieve(valor, file_local[1:])
                        diccionario['src'] = file_local[1:]


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    karaoke = KaraokeLocal(file)
    print(karaoke)
    karaoke.to_json(file)
    karaoke.do_local()
    karaoke.to_json('local.smil')
    print(karaoke)
