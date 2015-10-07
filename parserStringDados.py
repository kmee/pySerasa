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

        return arquivo.blocos.append(blocoMontado)

    def P002(self, bloco, arquivo):
        nome = "P002"
        blocoMontado = blocoP002(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N001(self, bloco, arquivo):
        nome = "N001"
        blocoMontado = blocoN001(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N002(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N002_00"
            blocoMontado = blocoN002_subtipo00(nome, bloco)

            return arquivo.blocos.append(blocoMontado)

        if bloco[4:6] == '01':
            nome = "N002_00"
            blocoMontado = blocoN002_subtipo01(nome, bloco)

            return arquivo.blocos.append(blocoMontado)

        return arquivo

    def N003(self, bloco, arquivo):
        nome = "N003"
        blocoMontado = blocoN003(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N200(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N200_00"
            blocoMontado = blocoN200_subtipo00(nome, bloco)

        if bloco[4:6] == '01':
            nome = "N200_01"
            blocoMontado = blocoN200_subtipo01(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N210(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N210_00"
            blocoMontado = blocoN200_subtipo00(nome, bloco)

        if bloco[4:6] == '01':
            nome = "N210_01"
            blocoMontado = blocoN210_subtipo01(nome, bloco)

        if bloco[4:6] == '99':
            nome = "N210_99"
            blocoMontado = blocoN210_subtipo99(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N220(self, bloco, arquivo):
        nome = "N220"
        blocoMontado = blocoN220(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N230(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N230_00"
            blocoMontado = blocoN230_subtipo00(nome, bloco)

        if bloco[4:6] == '90':
            nome = "N230_90"
            blocoMontado = blocoN230_subtipo90(nome, bloco)
        
        if bloco[4:6] == '99':
            nome = "N230_99"
            blocoMontado = blocoN230_subtipo99(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N240(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N240_00"
            blocoMontado = blocoN240_subtipo00(nome, bloco)

        if bloco[4:6] == '01':
            nome = "N240_01"
            blocoMontado = blocoN240_subtipo01(nome, bloco)

        if bloco[4:6] == '90':
            nome = "N240_90"
            blocoMontado = blocoN240_subtipo90(nome, bloco)

        if bloco[4:6] == '99':
            nome = "N240_99"
            blocoMontado = blocoN240_subtipo99(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N250(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N250_00"
            blocoMontado = blocoN250_subtipo00(nome, bloco)

        if bloco[4:6] == '01':
            nome = "N250_01"
            blocoMontado = blocoN250_subtipo01(nome, bloco)

        if bloco[4:6] == '90':
            nome = "N250_90"
            blocoMontado = blocoN250_subtipo90(nome, bloco)

        if bloco[4:6] == '99':
            nome = "N250_99"
            blocoMontado = blocoN250_subtipo99(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N270(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N270_00"
            blocoMontado = blocoN270_subtipo00(nome, bloco)

        if bloco[4:6] == '90':
            nome = "N270_90"
            blocoMontado = blocoN270_subtipo90(nome, bloco)

        if bloco[4:6] == '99':
            nome = "N270_99"
            blocoMontado = blocoN270_subtipo99(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def N440(self, bloco, arquivo):
        if bloco[4:6] == '00':
            nome = "N440_00"
            blocoMontado = blocoN440_subtipo00(nome, bloco)

        if bloco[4:6] == '01':
            nome = "N440_01"
            blocoMontado = blocoN440_subtipo01(nome, bloco)

        if bloco[4:6] == '02':
            nome = "N440_02"
            blocoMontado = blocoN440_subtipo02(nome, bloco)

        if bloco[4:6] == '03':
            nome = "N440_03"
            blocoMontado = blocoN440_subtipo03(nome, bloco)

        if bloco[4:6] == '99':
            nome = "N440_99"
            blocoMontado = blocoN440_subtipo99(nome, bloco)

        return arquivo.blocos.append(blocoMontado)
        
    def T999(self, bloco, arquivo):
        nome = "T999"
        blocoMontado = blocoT999(nome, bloco)

        return arquivo.blocos.append(blocoMontado)

    def case_default(self):
        print "Bloco não localizado!"

    def switch(self, bloco, blocoCodigo, arquivo):
        if blocoCodigo == 'B49C':
            self.B49C(bloco, arquivo)
        elif blocoCodigo == 'P002':
            self.P002(bloco, arquivo)
        elif blocoCodigo == 'N001':
            self.N001(bloco, arquivo)
        elif blocoCodigo == 'N002':
            self.N002(bloco, arquivo)
        elif blocoCodigo == 'N003':
            self.N003(bloco, arquivo)
        elif blocoCodigo == 'N200':
            self.N200(bloco, arquivo)
        elif blocoCodigo == 'N210':
            self.N210(bloco, arquivo)
        elif blocoCodigo == 'N220':
            self.N220(bloco, arquivo)
        elif blocoCodigo == 'N230':
            self.N230(bloco, arquivo)
        elif blocoCodigo == 'N240':
            self.N240(bloco, arquivo)
        elif blocoCodigo == 'N250':
            self.N250(bloco, arquivo)
        elif blocoCodigo == 'N270':
            self.N270(bloco, arquivo)
        elif blocoCodigo == 'N440':
            self.N440(bloco, arquivo)
        elif blocoCodigo == 'T999':
            self.T999(bloco, arquivo)

        return arquivo

    def parserStringDadosRetorno(self, stringDadosRetorno, arquivo):
        stringDadosRetorno = stringDadosRetorno[0:len(stringDadosRetorno)-2] + 'T999'
        vetorStringDados = re.findall("([B,P,N,T]\d{2}.*?)(?=[B,P,N,T]\d{3})", stringDadosRetorno)

        arquivo = self.montarObjetoCrednet(vetorStringDados, arquivo)

        return arquivo

    def montarObjetoCrednet(self, vetorStringDados, arquivo):

        #self.switch(vetorStringDados[0], vetorStringDados[0][0:4], arquivo)

        for bloco in vetorStringDados:
            blocoCodigo = bloco[0:4]
            arquivo = self.switch(bloco, blocoCodigo, arquivo)

        return arquivo
