# -*- coding: utf-8 -*-
from campos import Campo
import locale

class campoData(Campo):

     def __init__(self, indice, inicio, nome, bloco, tamanho):
        self._indice = indice
        self._nome = nome
        self._valor = self.mascaraData(bloco[inicio:inicio+tamanho])


     def mascaraData(self, valor):

        if len(valor) < 8:
            valor = valor[0:2] + "/" + valor[2:6]
        else:
            valor = valor[0:2] + "/" + valor[2:4] + "/" + valor[4:8]

        return valor


class campoDinheiro(Campo):

    def __init__(self, indice, inicio, nome, bloco, tamanho):
        self._indice = indice
        self._nome = nome
        self._valor = self.mascaraDinheiro(bloco[inicio:inicio+tamanho])

    def mascaraDinheiro(self, valor):

        valor = valor[0:len(valor)-2] + "." + valor[len(valor)-2:len(valor)]
        valor = float(valor)

        return valor