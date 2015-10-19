# -*- coding: utf-8 -*-
import re
import requests


class ParserStringDados(object):

    def gerarStringEnvio(self, logon, senha, documentoConsultado, tipoPessoaBusca, documentoConsultor):
        dados = 'https://mqlinuxext.serasa.com.br/Homologa/consultahttps?p=' + logon + senha + '        B49C      ' + documentoConsultado + tipoPessoaBusca + 'C     FI0001000000000000000N99SINIAN                              D             N                                            ' + documentoConsultor + '                                                                                                                                                                                                                                           P002RE02                                                                                                           N00100PPX21P 0                                                                                                     T999'

        return dados

    def realizarBuscaSerasa(self, dados):
        request = requests.get(dados)

        return request.text


    def montarBloco(self, bloco, arquivo):
        nome = bloco[0:4]
        nomeClasse = "bloco"+nome
        if bloco[0:4] != u'B49C' and bloco[0:4] != u'T999' and bloco[0:4] != u'P002' and bloco[0:4] != u'N001' and bloco[0:4] != u'N003':
            nomeClasse = nomeClasse + "_subtipo" + bloco[4:6]
        mod_serializer = __import__('blocosDados', globals(), locals())
        func = getattr(mod_serializer, nomeClasse)
        # blocoMontado = globals()[nomeClasse](nome, bloco)
        blocoMontado = func(nome, bloco)

        if nome == 'N230':
            arquivo.blocos[0].blocos.append(blocoMontado)
        elif nome == 'N240':
            arquivo.blocos[1].blocos.append(blocoMontado)
        elif nome == 'N250':
            arquivo.blocos[2].blocos.append(blocoMontado)
        elif nome == 'N270':
            arquivo.blocos[3].blocos.append(blocoMontado)
        else:
            arquivo.blocos.append(blocoMontado)

        return arquivo

    def parserStringDadosRetorno(self, stringDadosRetorno, arquivo):
        stringDadosRetorno = stringDadosRetorno[0:len(stringDadosRetorno)-2] + 'T999'
        vetorStringDados = re.findall("([B,P,N,T]\d{2}.*?)(?=[B,P,N,T]\d{3})", stringDadosRetorno)

        arquivo = self.montarObjetoCrednet(vetorStringDados, arquivo)

        return arquivo

    def montarObjetoCrednet(self, vetorStringDados, arquivo):

        for bloco in vetorStringDados:
            # blocoCodigo = bloco[0:4]
            # Arquivo recebe as atualizações direto de cada função a partir do seu própio código
            # arquivo = self.__getattribute__(blocoCodigo)(bloco, arquivo)
            arquivo = self.montarBloco(bloco, arquivo)

        return arquivo
