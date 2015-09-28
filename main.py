# -*- coding: utf-8 -*-
import re
from parserStringDados import ParserStringDados

stringDados = 'B49C      062173620000180JC     FI0001000000000000000N99SFIMAN                            ' \
              'SS              N                                            08053031000201  000000000    ' \
              '           00  2015092417151100000020    0021                                             ' \
              '                           0000                    3#                                     ' \
              '                                        P002RE02                                          ' \
              '                                                                 N00100PPX2PJN0    708439 ' \
              '                      CM                                                                  ' \
              'N20000SERASA S/A                                                            191019702 2008' \
              '2014                     N20001                                                           ' \
              '                                                  N21099NAO CONSTAM OCORRENCIAS           ' \
              '                                                                           N23099NAO CONST' \
              'AM OCORRENCIAS                                                                            ' \
              '          N2400028052013FINANCIAMENTO                 NR$ 0000000012547899897879878974522S' \
              'ERASA S/A                    SPO   N24001N                                                ' \
              '                            V0030188217                     N2400001012012ADIANT CONTA    ' \
              '              SR$ 00000000000165401              SERASA S/A                    SPO   N2400' \
              '1N                                                                            V0026548030 ' \
              '                    N2409000002012012052013000000001256443V                               ' \
              '                                             N2400012112013SENTENCA JUDICIAL             N' \
              'R$ 0000000000080004599            E.B.O.T.E. EMPRESA B                N24001N             ' \
              '                                                               50032468375                ' \
              '     N2400010052011CERT DIV EN 76                NR$ 000000000030000123456789       BAU   ' \
              '                        SPO   N24001N                                                     ' \
              '                       50019767719                     N2409000002052011112013000000000038' \
              '0005                                                                            N25099NAO ' \
              'CONSTAM OCORRENCIAS                                                                       ' \
              '               N27099NAO CONSTAM OCORRENCIAS                                              ' \
              '                                        N44099NAO CONSTAM INFORMACOES                     ' \
              '                                                                 T999000PROCESSO ENCERRADO' \
              ' NORMALMENTE                                                                             '

dados = 'https://mqlinuxext.serasa.com.br/Homologa/consultahttps?p=4426006940302010        B49C      062173620000180JC     FI0001000000000000000N99SINIAN                              D             N                                            08053031000201                                                                                                                                                                                                                                           P002RE02                                                                                                           N00100PPX21P 0                                                                                                     T999'
parser = ParserStringDados()

stringDados = parser.realizarBuscaSerasa(dados)

arquivo = parser.parserStringDadosRetorno(stringDados)

print(arquivo.blocoN200_subtipo00().get_nome_bloco()+'\n')
print(u'Tipo do registro: ' + arquivo.blocoN200_subtipo00.tipoReg)
print(u'Subtipo: ' + arquivo.blocoN200_subtipo00.subtipo)
print(u'Nome razão: ' + arquivo.blocoN200_subtipo00.nomeRazao)
print(u'Data de nascimento ou fundação: ' + arquivo.blocoN200_subtipo00.dataNascFundacao)
print(u'Situação do documento: ' + arquivo.blocoN200_subtipo00.situacaoDoc)
print(u'Data da situação do documento: ' + arquivo.blocoN200_subtipo00.dataSituacaoDoc)

print(u'N230: ' + arquivo.blocoN230_subtipo99.msgR230)
