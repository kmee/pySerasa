# -*- coding: utf-8 -*-
import re
from crednet import Crednet


class ParserStringDados(object):

    def B49C(self, bloco, arquivo):
        print "Bloco B49C"

    def P002(self, bloco, arquivo):
        arquivo.blocoP002.tipoReg = bloco[0:4]
        arquivo.blocoP002.cod1 = bloco[4:8]
        arquivo.blocoP002.chave1 = bloco[8:29]
        arquivo.blocoP002.cod2 = bloco[29:33]
        arquivo.blocoP002.chave2 = bloco[33:54]
        arquivo.blocoP002.cod3 = bloco[54:58]
        arquivo.blocoP002.chave3 = bloco[58:79]
        arquivo.blocoP002.cod4 = bloco[79:83]
        arquivo.blocoP002.chave4 = bloco[83:104]
        arquivo.blocoP002.filler = bloco[104:115]

        return arquivo

    def N001(self, bloco, arquivo):
        arquivo.blocoN001.tipoReg = bloco[0:4]
        arquivo.blocoN001.subtipo = bloco[4:6]
        arquivo.blocoN001.tipoConsulta = bloco[6:8]
        arquivo.blocoN001.transacaoConsulta = bloco[8:12]
        arquivo.blocoN001.solGrandeVarejo = bloco[12:13]
        arquivo.blocoN001.idCheque = bloco[13:14]
        arquivo.blocoN001.agrupa = bloco[14:15]
        arquivo.blocoN001.consultaSintetica = bloco[15:16]
        arquivo.blocoN001.reservado = bloco[16:17]
        arquivo.blocoN001.anotacoesResumo = bloco[17:18]
        arquivo.blocoN001.chaveConsulta = bloco[18:24]
        arquivo.blocoN001.fantasia = bloco[24:36]
        arquivo.blocoN001.statusBanco = bloco[36:37]
        arquivo.blocoN001.filler = bloco[37:50]
        arquivo.blocoN001.trataTel = bloco[50:51]

        return arquivo

    def N002(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN002_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN002_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN002_subtipo00.banco = bloco[6:9]
            arquivo.blocoN002_subtipo00.agencia = bloco[9:13]
            arquivo.blocoN002_subtipo00.contaCorrente = bloco[13:28]
            arquivo.blocoN002_subtipo00.chequeInicial = bloco[28:34]
            arquivo.blocoN002_subtipo00.digitoChequeInicial = bloco[34:35]
            arquivo.blocoN002_subtipo00.chequeFinal = bloco[35:41]
            arquivo.blocoN002_subtipo00.digitoChequeInicial = bloco[41:42]
            arquivo.blocoN002_subtipo00.cmc7Inicial = bloco[42:72]
            arquivo.blocoN002_subtipo00.cmc7Final = bloco[72:102]
            arquivo.blocoN002_subtipo00.filler = bloco[102:105]

        if bloco[4:6] == '01':
            arquivo.blocoN002_subtipo01 = bloco[0:4]
            arquivo.blocoN002_subtipo01 = bloco[4:6]
            arquivo.blocoN002_subtipo01 = bloco[6:21]
            arquivo.blocoN002_subtipo01 = bloco[21:29]
            arquivo.blocoN002_subtipo01 = bloco[29:115]

        return arquivo

    def N003(self, bloco, arquivo):
        print "Bloco N003"

    def N200(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN200_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN200_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN200_subtipo00.nomeRazao = bloco[6:76]
            arquivo.blocoN200_subtipo00.dataNascFundacao = bloco[76:84]
            arquivo.blocoN200_subtipo00.situacaoDoc = bloco[84:86]
            arquivo.blocoN200_subtipo00.dataSituacaoDoc = bloco[86:94]
            arquivo.blocoN200_subtipo00.filler = bloco[94:115]

        if bloco[4:6] == '01':
            arquivo.blocoN002_subtipo01.tipoReg = bloco[0:4]
            arquivo.blocoN200_subtipo01.subtipo = bloco[4:6]
            arquivo.blocoN200_subtipo01.nomeMae = bloco[6:46]
            arquivo.blocoN200_subtipo01.filler = bloco[46:115]

        return arquivo

    def N210(self, bloco, arquivo):
        if bloco[4:6] == '99':
            arquivo.blocoN210_subtipo99.tipoReg = bloco[0:4]
            arquivo.blocoN210_subtipo99.subtipo = bloco[4:6]
            arquivo.blocoN210_subtipo99.msgR210 = bloco[6:46]
            arquivo.blocoN210_subtipo99.filler = bloco[46:115]

    def N220(self, bloco, arquivo):
        print "Bloco N220"

    def N230(self, bloco, arquivo):
        print "Bloco N230"

    def N240(self, bloco, arquivo):
        print "Bloco N240"

    def N250(self, bloco, arquivo):
        print "Bloco N250"

    def N270(self, bloco, arquivo):
        print "Bloco N270"

    def N440(self, bloco, arquivo):
        print "Bloco N440"

    def T999(self, bloco, arquivo):
        print "Bloco T999"

    def case_default(self):
        print "Bloco não localizado!"

    def switch(self, bloco, blocoCodigo, arquivo):
        if blocoCodigo == 'B49C':
            self.B49C(bloco, arquivo)
        elif blocoCodigo == 'P002':
            arquivo = self.P002(bloco, arquivo)
        elif blocoCodigo == 'N001':
            arquivo = self.N001(bloco, arquivo)
        elif blocoCodigo == 'N002':
            arquivo = self.N002(bloco, arquivo)
        elif blocoCodigo == 'N003':
            self.N003(bloco, arquivo)
        elif blocoCodigo == 'N200':
            arquivo = self.N200(bloco, arquivo)
        elif blocoCodigo == 'N210':
            arquivo = self.N210(bloco, arquivo)
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

    def parserStringDadosRetorno(self, stringDadosRetorno):
        vetorStringDados = re.findall("([B,P,N,T]\d{2}.*?)(?=[P,N,T]\d{3})", stringDadosRetorno)
        # print vetorStringDados

        arquivoCrednet = self.montarObjetoCrednet(vetorStringDados)

        return arquivoCrednet

    def montarObjetoCrednet(self, vetorStringDados):
        arquivo = Crednet()

        for bloco in vetorStringDados:
            blocoCodigo = bloco[0:4]
            arquivo = self.switch(bloco, blocoCodigo, arquivo)

        return arquivo