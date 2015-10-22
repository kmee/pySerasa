# -*- coding: utf-8 -*-


class Campo(object):

    def __init__(self, indice, inicio, nome, bloco, tamanho):
        self._indice = indice
        self._nome = nome
        self._valor = bloco[inicio:inicio+tamanho]


