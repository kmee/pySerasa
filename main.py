# -*- coding: utf-8 -*-

from parserStringDados import ParserStringDados
from crednet import Crednet

logon = '32629955'

senha = '10203040'

documentoConsultado = '062173620000180'

tipoPessoaBusca = 'J'

documentoConsultor = '08053031000201'


# Objeto que gerencia todas as funções de parsing
parser = ParserStringDados()

# Variavel que recebe o a string de retorno do Serasa
stringDados = parser.realizarBuscaSerasa(parser.gerarStringEnvio(logon, senha, documentoConsultado, tipoPessoaBusca,
                                                                 documentoConsultor))

arquivo = Crednet()

# Gera o arquivo parseado separando os blocos da string de retorno
# segundo o manual do Crednet do Serasa versão:06 de Janeiro/2014
arquivo = parser.parserStringDadosRetorno(stringDados, arquivo)

print arquivo.B49C.Protocolo
print arquivo.B49C.numDocumentoConsultado
print arquivo.B49C.tipoPessoaConsultado
print arquivo.N240_00.valor
print arquivo.N440_99.msgR440