# -*- coding: utf-8 -*-
import re
import requests


class ParserStringDados(object):

    def gerar_string_envio(self, documento_consultado,
                           tipo_pessoa_busca, documento_consultor, uf_cliente,
                           login, senha):
        
        dados = 'https://sitenet43.serasa.com.br/Prod/consultahttps?p=' \
                + login + senha + '        B49C      ' + documento_consultado +\
                tipo_pessoa_busca + 'C     FI0001000000000000000N99SINIAN    ' \
                                    '                          D             ' \
                                    'N                                       ' \
                                    '     ' \
                + documento_consultor + '                                    ' \
                                        '                                    ' \
                                        '                                    ' \
                                        '                                    ' \
                                        '                                    ' \
                                        '                                    ' \
                                        '                   P002RE02         ' \
                                        '                                    ' \
                                        '                                    ' \
                                        '                          N00100PPX2' \
                                        '1P 0                                ' \
                                        '                                    ' \
                                        '                                 ' \
                                        'N00300                     ' \
                + uf_cliente + '                                             ' \
                               '                                         T999'

        return dados

    def realizar_busca_serasa(self, dados):
        request = requests.get(dados, verify=False)

        return request.text

    def montar_bloco(self, bloco, arquivo):
        nome = bloco[0:4]
        nome_classe = "bloco"+nome
        if bloco[0:4] != u'B49C' and bloco[0:4] != u'T999' \
                and bloco[0:4] != u'P002' and bloco[0:4] != u'N001' \
                and bloco[0:4] != u'N003' and bloco[0:4] != u'A900' \
                and bloco[0:4] != u'I105':
            nome_classe = nome_classe + "_subtipo" + bloco[4:6]
        mod_serializer = __import__('blocosDados', globals(), locals())
        func = getattr(mod_serializer, nome_classe)
        bloco_montado = func(nome, bloco)

        if nome == 'N230':
            arquivo.blocos[0].blocos.append(bloco_montado)
        elif nome == 'N240':
            arquivo.blocos[1].blocos.append(bloco_montado)
        elif nome == 'N250':
            arquivo.blocos[2].blocos.append(bloco_montado)
        elif nome == 'N270':
            arquivo.blocos[3].blocos.append(bloco_montado)
        else:
            arquivo.blocos.append(bloco_montado)

        return arquivo

    def parser_string_dados_retorno(self, string_dados_retorno, arquivo):
        string_dados_retorno = string_dados_retorno[
                               0:len(string_dados_retorno)-2] + 'T999'
        vetor_string_dados = re.findall(
            "([B,P,N,I,A]\d{2}.*?)(?=(?!I000)[B,P,N,I][0-9][0-9][0-9]|A900|T999)", string_dados_retorno)

        arquivo_crednet = self.montar_objeto_crednet(
            vetor_string_dados, arquivo)

        return arquivo_crednet

    def montar_objeto_crednet(self, vetor_string_dados, arquivo):

        for bloco in vetor_string_dados:
            arquivo = self.montar_bloco(bloco, arquivo)

        return arquivo
