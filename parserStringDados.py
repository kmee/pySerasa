# -*- coding: utf-8 -*-
import re
import requests
from blocosDados import *


class ParserStringDados(object):

    def gerarStringEnvio(self, logon, senha, documentoConsultado, tipoPessoaBusca, documentoConsultor):
        dados = 'https://mqlinuxext.serasa.com.br/Homologa/consultahttps?p=' + logon + senha + '        B49C      ' + documentoConsultado + tipoPessoaBusca + 'C     FI0001000000000000000N99SINIAN                              D             N                                            ' + documentoConsultor + '                                                                                                                                                                                                                                           P002RE02                                                                                                           N00100PPX21P 0                                                                                                     T999'

        return dados

    def realizarBuscaSerasa(self, dados):
        request = requests.get(dados)

        return request.text

    def B49C(self, bloco, arquivo):
        nome = "B49C"
        blocoMontado = blocoB49C(nome, bloco)
        arquivo.blocos.append(blocoMontado)

        return arquivo

    def P002(self, bloco, arquivo):
        nome = "P002"
        blocoMontado = blocoP002(nome, bloco)
        arquivo.blocos.append(blocoMontado)

        return arquivo

    def N001(self, bloco, arquivo):
        nome = "N001"
        blocoMontado = blocoN001(nome, bloco)
        arquivo.blocos.append(blocoMontado)

        return arquivo

    def N002(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N002_00"
            blocoMontado = blocoN002_subtipo00(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N002_00"
            blocoMontado = blocoN002_subtipo01(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        return arquivo

    def N003(self, bloco, arquivo):
        nome = "N003"
        blocoMontado = blocoN003(nome, bloco)
        arquivo.blocos.append(blocoMontado)

        return arquivo

    def N200(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N200_00"
            blocoMontado = blocoN200_subtipo00(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N200_01"
            blocoMontado = blocoN200_subtipo01(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        return arquivo

    def N210(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N210_00"
            blocoMontado = blocoN200_subtipo00(nome, bloco)
            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N210_01"
            blocoMontado = blocoN210_subtipo01(nome, bloco)
            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '99':
            nome = "N210_99"
            blocoMontado = blocoN210_subtipo99(nome, bloco)
            arquivo.blocos.append(blocoMontado)

        return arquivo

    def N220(self, bloco, arquivo):
        nome = "N220"
        blocoMontado = blocoN220(nome, bloco)
        arquivo.blocos.append(blocoMontado)

        return arquivo

    def N230(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N230_00"
            blocoMontado = blocoN230_subtipo00(nome, bloco)

            arquivo.blocos[0].blocos.append(blocoMontado)

        if bloco[4:6] == '90':
            nome = "N230_90"
            blocoMontado = blocoN230_subtipo90(nome, bloco)

            arquivo.blocos[0].blocos.append(blocoMontado)
        
        if bloco[4:6] == '99':
            nome = "N230_99"
            blocoMontado = blocoN230_subtipo99(nome, bloco)

            arquivo.blocos[0].blocos.append(blocoMontado)

        return arquivo

    def N240(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N240_00"
            blocoMontado = blocoN240_subtipo00(nome, bloco)

            arquivo.blocos[1].blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N240_01"
            blocoMontado = blocoN240_subtipo01(nome, bloco)

            arquivo.blocos[1].blocos.append(blocoMontado)

        if bloco[4:6] == '90':
            nome = "N240_90"
            blocoMontado = blocoN240_subtipo90(nome, bloco)

            arquivo.blocos[1].blocos.append(blocoMontado)

        if bloco[4:6] == '99':
            nome = "N240_99"
            blocoMontado = blocoN240_subtipo99(nome, bloco)

            arquivo.blocos[1].blocos.append(blocoMontado)

        return arquivo

    def N250(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N250_00"
            blocoMontado = blocoN250_subtipo00(nome, bloco)

            arquivo.blocos[2].blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N250_01"
            blocoMontado = blocoN250_subtipo01(nome, bloco)

            arquivo.blocos[2].blocos.append(blocoMontado)

        if bloco[4:6] == '90':
            nome = "N250_90"
            blocoMontado = blocoN250_subtipo90(nome, bloco)

            arquivo.blocos[2].blocos.append(blocoMontado)

        if bloco[4:6] == '99':
            nome = "N250_99"
            blocoMontado = blocoN250_subtipo99(nome, bloco)

            arquivo.blocos[2].blocos.append(blocoMontado)

        return arquivo

    def N270(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N270_00"
            blocoMontado = blocoN270_subtipo00(nome, bloco)

            arquivo.blocos[3].blocos.append(blocoMontado)


        if bloco[4:6] == '90':
            nome = "N270_90"
            blocoMontado = blocoN270_subtipo90(nome, bloco)

            arquivo.blocos[3].blocos.append(blocoMontado)

        if bloco[4:6] == '99':
            nome = "N270_99"
            blocoMontado = blocoN270_subtipo99(nome, bloco)

            arquivo.blocos[3].blocos.append(blocoMontado)

        return arquivo

    def N440(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N440_00"
            blocoMontado = blocoN440_subtipo00(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N440_01"
            blocoMontado = blocoN440_subtipo01(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '02':
            nome = "N440_02"
            blocoMontado = blocoN440_subtipo02(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '03':
            nome = "N440_03"
            blocoMontado = blocoN440_subtipo03(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '99':
            nome = "N440_99"
            blocoMontado = blocoN440_subtipo99(nome, bloco)

            arquivo.blocos.append(blocoMontado)

        return arquivo
        
    def T999(self, bloco, arquivo):
        nome = "T999"
        blocoMontado = blocoT999(nome, bloco)

        arquivo.blocos.append(blocoMontado)

        return arquivo

    def parserStringDadosRetorno(self, stringDadosRetorno, arquivo):
        stringDadosRetorno = stringDadosRetorno[0:len(stringDadosRetorno)-2] + 'T999'
        vetorStringDados = re.findall("([B,P,N,T]\d{2}.*?)(?=[B,P,N,T]\d{3})", stringDadosRetorno)

        arquivo = self.montarObjetoCrednet(vetorStringDados, arquivo)

        return arquivo

    def montarObjetoCrednet(self, vetorStringDados, arquivo):

        for bloco in vetorStringDados:
            blocoCodigo = bloco[0:4]
            # Arquivo recebe as atualizações direto de cada função a partir do seu própio código
            arquivo = self.__getattribute__(blocoCodigo)(bloco, arquivo)

        return arquivo
