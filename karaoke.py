#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import smallsmilhandler
from xml.sax import make_parser


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSmilHandler()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    lista = cHandler.get_tags()
    for diccionario in lista:
        print(diccionario['etiqueta'], end="\t")
        diccionario['etiqueta'] = 'etiqueta'
        for atributo, valor in diccionario.items():
            if atributo != diccionario['etiqueta'] and valor != "":
                print(atributo + '=' + '"' + valor + '"', end="\t")
        print()
