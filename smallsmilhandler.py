#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):
    def __init__(self):
        self.lista = []
        self.dicc_ka = {'root-layout': ['width', 'height', 'background-color'],
                        'region': ['id', 'top', 'bottom', 'left', 'right'],
                        'img': ['src', 'region', 'begin', 'dur'],
                        'audio': ['src', 'begin', 'dur'],
                        'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        diccionario = {}
        if name in self.dicc_ka:
            diccionario['etiqueta'] = name
            for atributo in self.dicc_ka[name]:
                diccionario[atributo] = attrs.get(atributo, '')
            self.lista.append(diccionario)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    lista = cHandler.get_tags()
    print(lista)
