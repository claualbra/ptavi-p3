#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.lista = []
        self.diccionario = {}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background-color', "")
            self.diccionario = {'etiqueta': 'root-layout',
                                'width': self.width, 'height': self.height,
                                'background-color': self.background_color}
            self.lista.append(self.diccionario)
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.diccionario = {'etiqueta': 'region', 'id': self.id,
                                'top': self.top, 'bottom': self.bottom,
                                'left': self.left, 'right': self.right}
            self.lista.append(self.diccionario)
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.diccionario = {'etiqueta': 'img', 'src': self.src,
                                'region': self.region, 'begin': self.begin,
                                'dur': self.dur}
            self.lista.append(self.diccionario)
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.diccionario = {'etiqueta': 'audio', 'src': self.src,
                                'begin': self.begin, 'dur': self.dur}
            self.lista.append(self.diccionario)
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.diccionario = {'etiqueta': 'textstream', 'src': self.src,
                                'region': self.region}
            self.lista.append(self.diccionario)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    lista = cHandler.get_tags()
    print(lista)
