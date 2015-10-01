# -*- coding: utf-8 -*-

from parserStringDados import ParserStringDados
from crednet import Crednet

logon = '32629955'

senha = '10203040'

documentoConsultado = '062173620000180'

tipoDeBusca = 'J'

documentoConsultor = '08053031000201'

dados = 'https://mqlinuxext.serasa.com.br/Homologa/consultahttps?p=' + logon + senha + '        B49C      ' + documentoConsultado + tipoDeBusca + 'C' \
        '     FI0001000000000000000N99SINIAN                              D             N                             ' \
        '               ' + documentoConsultor + '                                                                                ' \
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

#
# for bloco in arquivo._blocos:
#         for campo in bloco._campos:
#                 print (campo._nome + " : " + campo._valor)
#
#         print "\n"

print arquivo.B49C.Protocolo
print arquivo.P002.tipoReg
# print arquivo.N001.transacaoConsulta
print arquivo.T999.tipoReg + " : " + arquivo.T999.mensagem
