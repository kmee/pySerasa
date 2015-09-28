# -*- coding: utf-8 -*-
from parserStringDados import ParserStringDados

dados = ('https://mqlinuxext.serasa.com.br/Homologa/consultahttps?p=4426006940'
         '302010        B49C      062173620000180JC     FI0001000000000000000N'
         '99SINIAN                              D             N               '
         '                             08053031000201                         '
         '                                                                    '
         '                                                                    '
         '                                                                    '
         '      P002RE02                                                      '
         '                                                     N00100PPX21P 0 '
         '                                                                    '
         '                                T999')
# Objeto que gerencia todas as funções de parsing
parser = ParserStringDados()

# Variavel que recebe o a string de retorno do Serasa
stringDados = parser.realizarBuscaSerasa(dados)

# Gera o arquivo parseado separando os blocos da string de retorno
# segundo o manual do Crednet do Serasa versão:06 de Janeiro/2014
arquivo = parser.parserStringDadosRetorno(stringDados)

print(arquivo.blocoN200_subtipo00().get_nome_bloco() + '\n')
print(u'Tipo do registro: ' + arquivo.blocoN200_subtipo00.tipoReg)
print(u'Subtipo: ' + arquivo.blocoN200_subtipo00.subtipo)
print(u'Nome razão: ' + arquivo.blocoN200_subtipo00.nomeRazao)
print(u'Data de nascimento ou fundação: ' +
      arquivo.blocoN200_subtipo00.dataNascFundacao)
print(u'Situação do documento: ' + arquivo.blocoN200_subtipo00.situacaoDoc)
print(u'Data da situação do documento: ' +
      arquivo.blocoN200_subtipo00.dataSituacaoDoc)

print(u'N230: ' + arquivo.blocoN230_subtipo99.msgR230)

print (u'B49C: ' + arquivo.blocoB49C.tipoPessoaConsultado)
