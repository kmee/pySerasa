# -*- coding: utf-8 -*-
import re
from parserStringDados import ParserStringDados
from crednet import Crednet
from blocos import *

documentoConsultado = '062173620000180'

tipoDeBusca = 'J'

dados = 'https://mqlinuxext.serasa.com.br/Homologa/consultahttps?p=4426006940302010        B49C      ' + documentoConsultado + tipoDeBusca + 'C' \
        '     FI0001000000000000000N99SINIAN                              D             N                             ' \
        '               08053031000201                                                                                ' \
        '                                                                                                             ' \
        '                                              P002RE02                                                       ' \
        '                                                    N00100PPX21P 0                                           ' \
        '                                                          T999'
# Objeto que gerencia todas as funções de parsing
parser = ParserStringDados()

# Variavel que recebe o a string de retorno do Serasa
stringDados = parser.realizarBuscaSerasa(dados)

arquivo = Crednet()
# Gera o arquivo parseado separando os blocos da string de retorno
# segundo o manual do Crednet do Serasa versão:06 de Janeiro/2014
arquivo = parser.parserStringDadosRetorno(stringDados, arquivo)


for bloco in arquivo._blocos:
        for campo in bloco._campos:
                print (campo._nome + " : " + campo._valor)

        print "\n"

print arquivo._blocos[0]._campos[0]._nome