#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):
    def __init__(self):
        self.lista = []
        self.diccionario = {}

    def startElement(self, name, attrs):
        if name == 'root-layout':
            self.diccionario = {'etiqueta': name,
                                'width': attrs.get('width', ""),
                                'height': attrs.get('height', ""),
                                'background-color':
                                attrs.get('background-color', "")}
            self.lista.append(self.diccionario)
        elif name == 'region':
            self.diccionario = {'etiqueta': name, 'id': attrs.get('id', ""),
                                'top': attrs.get('top', ""),
                                'bottom': attrs.get('bottom', ""),
                                'left': attrs.get('left', ""),
                                'right': attrs.get('right', "")}
            self.lista.append(self.diccionario)
        elif name == 'img':
            self.diccionario = {'etiqueta': name, 'src': attrs.get('src', ""),
                                'region': attrs.get('region', ""),
                                'begin': attrs.get('begin', ""),
                                'dur': attrs.get('dur', "")}
            self.lista.append(self.diccionario)
        elif name == 'audio':
            self.diccionario = {'etiqueta': name, 'src': attrs.get('src', ""),
                                'begin': attrs.get('begin', ""),
                                'dur': attrs.get('dur', "")}
            self.lista.append(self.diccionario)
        elif name == 'textstream':
            self.diccionario = {'etiqueta': name, 'src': attrs.get('src', ""),
                                'region': attrs.get('region', "")}
            self.lista.append(self.diccionario)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    lista = cHandler.get_tags()
    print(lista)
