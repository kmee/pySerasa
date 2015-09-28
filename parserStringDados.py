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
            arquivo.blocoN002_subtipo01.tipoReg = bloco[0:4]
            arquivo.blocoN002_subtipo01.subtipo = bloco[4:6]
            arquivo.blocoN002_subtipo01.valorCheque = bloco[6:21]
            arquivo.blocoN002_subtipo01.dataVencimentoCheque = bloco[21:29]
            arquivo.blocoN002_subtipo01.filler = bloco[29:115]

        return arquivo

    def N003(self, bloco, arquivo):
        arquivo.blocoN003.tipoReg = bloco[0:4]
        arquivo.blocoN003.subtipo = bloco[4:6]
        arquivo.blocoN003.ddd = bloco[6:10]
        arquivo.blocoN003.telefone = bloco[10:18]
        arquivo.blocoN003.cep = bloco[18:27]
        arquivo.blocoN003.uf = bloco[27:29]
        arquivo.blocoN003.featScor = bloco[29:109]
        arquivo.blocoN003.filler = bloco[109:114]

        return arquivo

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
        arquivo.blocoN200_subtipo00.tipoReg = bloco[0:4]
        arquivo.blocoN200_subtipo00.subtipo = bloco[4:6]
        arquivo.blocoN200_subtipo00.nomeRaza = bloco[6:76]
        arquivo.blocoN200_subtipo00.dataNascFundacao = bloco[76:84]
        arquivo.blocoN200_subtipo00.situacaoDoc = bloco[84:86]
        arquivo.blocoN200_subtipo00.dataSituacaoDoc = bloco[86:94]
        arquivo.blocoN200_subtipo00.filler = bloco[94:115]

        return arquivo

    def N230(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN230_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN230_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN230_subtipo00.dataOcorrencia = bloco[6:14]
            arquivo.blocoN230_subtipo00.modalidade = bloco[14:44]
            arquivo.blocoN230_subtipo00.avalista = bloco[44:45]
            arquivo.blocoN230_subtipo00.tipoMoeda = bloco[45:48]
            arquivo.blocoN230_subtipo00.valor = bloco[48:63]
            arquivo.blocoN230_subtipo00.contrato = bloco[63:79]
            arquivo.blocoN230_subtipo00.origem = bloco[79:109]
            arquivo.blocoN230_subtipo00.siglaEmbratel = bloco[109:113]
            arquivo.blocoN230_subtipo00.filler = bloco[113:115]

        if bloco[4:6] == '90':
            arquivo.blocoN230_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN230_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN230_subtipo00.totalOcorrencias = bloco[6:11]
            arquivo.blocoN230_subtipo00.dataOcorrenciaAntiga = bloco[11:17]
            arquivo.blocoN230_subtipo00.dataOcorrenciaRecente = bloco[17:23]
            arquivo.blocoN230_subtipo00.valorTotal = bloco[23:38]
            arquivo.blocoN230_subtipo00.filler = bloco[38:114]
        
        if bloco[4:6] == '99':
            arquivo.blocoN230_subtipo99.tipoReg = bloco[0:4]
            arquivo.blocoN230_subtipo99.subtipo = bloco[4:6]
            arquivo.blocoN230_subtipo99.msgR230 = bloco[6:46]
            arquivo.blocoN230_subtipo99.filler = bloco[46:114]

        return arquivo

    def N240(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN240_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN240_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN240_subtipo00.dataOcorrencia = bloco[6:14]
            arquivo.blocoN240_subtipo00.modalidade = bloco[14:44]
            arquivo.blocoN240_subtipo00.avalista = bloco[44:45]
            arquivo.blocoN240_subtipo00.tipoMoeda = bloco[45:48]
            arquivo.blocoN240_subtipo00.valor = bloco[48:63]
            arquivo.blocoN240_subtipo00.contrato = bloco[63:79]
            arquivo.blocoN240_subtipo00.origem = bloco[79:109]
            arquivo.blocoN240_subtipo00.siglaEmbratel = bloco[109:113]
            arquivo.blocoN240_subtipo00.filler = bloco[113:115]

        if bloco[4:6] == '01':
            arquivo.blocoN240_subtipo01.tipoReg = bloco[0:4]
            arquivo.blocoN240_subtipo01.subtipo = bloco[4:6]
            arquivo.blocoN240_subtipo01.subjudice = bloco[6:7]
            arquivo.blocoN240_subtipo01.msgSubjudice = bloco[7:83]
            arquivo.blocoN240_subtipo01.tipoAnotacao = bloco[83:84]
            arquivo.blocoN240_subtipo01.codCadus = bloco[84:94]
            arquivo.blocoN240_subtipo01.filler = bloco[94:115]

        if bloco[4:6] == '90':
            arquivo.blocoN240_subtipo90.tipoReg = bloco[0:4]
            arquivo.blocoN240_subtipo90.subtipo = bloco[4:6]
            arquivo.blocoN240_subtipo90.totalOcorrencias = blocos[6:11]
            arquivo.blocoN240_subtipo90.dataOcorrenciaAntiga = blocos[11:17]
            arquivo.blocoN240_subtipo90.dataOcorrenciaRecente = blocos[17:23]
            arquivo.blocoN240_subtipo90.valorTotal = blocos[23:38]
            arquivo.blocoN240_subtipo90.tipoAnotacao = blocos[38:39]
            arquivo.blocoN240_subtipo90.filler = blocos[39:114]

        if bloco[4:6] == '99':
            arquivo.blocoN240_subtipo99.tipoReg = bloco[0:4]
            arquivo.blocoN240_subtipo99.subtipo = bloco[4:6]
            arquivo.blocoN240_subtipo99.msgR240 = bloco[6:46]
            arquivo.blocoN240_subtipo99.filler = bloco[46:114]


        return arquivo

    def N250(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN250_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN250_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN250_subtipo00.dataOcorrencia = bloco[6:14]
            arquivo.blocoN250_subtipo00.tipoMoeda = bloco[14:17]
            arquivo.blocoN250_subtipo00.valor = bloco[17:32]
            arquivo.blocoN250_subtipo00.cartorio = bloco[32:34]
            arquivo.blocoN250_subtipo00.cidade = bloco[34:64]
            arquivo.blocoN250_subtipo00.uf = bloco[64:66]
            arquivo.blocoN250_subtipo00.filler = bloco[66:114]

        if bloco[4:6] == '01':
            arquivo.blocoN250_subtipo01.tipoReg = bloco[0:4]
            arquivo.blocoN250_subtipo01.subtipo = bloco[4:6]
            arquivo.blocoN250_subtipo01.subjudice = bloco[6:7]
            arquivo.blocoN250_subtipo01.msgSubjudice = bloco[7:83]
            arquivo.blocoN250_subtipo01.tipoAnotacao = bloco[83:84]
            arquivo.blocoN250_subtipo01.codCadus = bloco[84:94]
            arquivo.blocoN250_subtipo01.filler = bloco[94:115]

        if bloco[4:6] == '90':
            arquivo.blocoN250_subtipo90.tipoReg = bloco[0:4]
            arquivo.blocoN250_subtipo90.subtipo = bloco[4:6]
            arquivo.blocoN250_subtipo90.totalOcorrencias = bloco[6:11]
            arquivo.blocoN250_subtipo90.dataOcorrenciaAntiga = bloco[11:17]
            arquivo.blocoN250_subtipo90.dataOcorrenciaRecente = bloco[17:23]
            arquivo.blocoN250_subtipo90.moeda = bloco[23:26]
            arquivo.blocoN250_subtipo90.valorTotal = bloco[26:41]
            arquivo.blocoN250_subtipo90.filler = bloco[41:115]

        if bloco[4:6] == '99':
            arquivo.blocoN250_subtipo99.tipoReg = bloco[0:4]
            arquivo.blocoN250_subtipo99.subtipo = bloco[4:6]
            arquivo.blocoN250_subtipo99.msgR250 = bloco[6:46]
            arquivo.blocoN250_subtipo99.filler = bloco[46:114]

        return arquivo

    def N270(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN270_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN270_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN270_subtipo00.dataOcorrencia = bloco[6:14]
            arquivo.blocoN270_subtipo00.cheque = bloco[14:24]
            arquivo.blocoN270_subtipo00.alinea = bloco[24:29]
            arquivo.blocoN270_subtipo00.quantidade = bloco[29:34]
            arquivo.blocoN270_subtipo00.valor = bloco[34:49]
            arquivo.blocoN270_subtipo00.numBanco = bloco[49:52]
            arquivo.blocoN270_subtipo00.nomeBanco = bloco[52:66]
            arquivo.blocoN270_subtipo00.agencia = bloco[66:70]
            arquivo.blocoN270_subtipo00.cidade = bloco[70:100]
            arquivo.blocoN270_subtipo00.uf = bloco[100:102]
            arquivo.blocoN270_subtipo00.codCadus = bloco[102:112]
            arquivo.blocoN270_subtipo00.filler = bloco[112:115]

        if bloco[4:6] == '90':
            arquivo.blocoN270_subtipo90.tipoReg = bloco[0:4]
            arquivo.blocoN270_subtipo90.subtipo = bloco[4:6]
            arquivo.blocoN270_subtipo90.totalOcorrencias = bloco[6:11]
            arquivo.blocoN270_subtipo90.dataOcorrenciaAntiga = bloco[11:19]
            arquivo.blocoN270_subtipo90.dataOcorrenciaRecente = bloco[19:27]
            arquivo.blocoN270_subtipo90.banco = bloco[27:30]
            arquivo.blocoN270_subtipo90.agencia = bloco[30:34]
            arquivo.blocoN270_subtipo90.nomeFantasiaBanco = bloco[34:46]
            arquivo.blocoN270_subtipo90.filler = bloco[46:114]

        if bloco[4:6] == '99':
            arquivo.blocoN270_subtipo99.tipoReg = bloco[0:4]
            arquivo.blocoN270_subtipo99.subtipo = bloco[4:6]
            arquivo.blocoN270_subtipo99.msgR270 = bloco[6:46]
            arquivo.blocoN270_subtipo99.filler = bloco[46:114]

        return arquivo

    def N440(self, bloco, arquivo):
        if bloco[4:6] == '00':
            arquivo.blocoN440_subtipo00.tipoReg = bloco[0:4]
            arquivo.blocoN440_subtipo00.subtipo = bloco[4:6]
            arquivo.blocoN440_subtipo00.dataEmissaoPrimeiroChequeVista = bloco[6:10]
            arquivo.blocoN440_subtipo00.dataEmissaoUltimoChequeVista = bloco[10:14]
            arquivo.blocoN440_subtipo00.totalChequesUltimos15DiasPrazo = bloco[14:17]
            arquivo.blocoN440_subtipo00.totalChequesUltimos30DiasPrazo = bloco[17:19]
            arquivo.blocoN440_subtipo00.totalChequesUltimos60DiasPrazo = bloco[19:21]
            arquivo.blocoN440_subtipo00.totalChequesUltimos90DiasPrazo = bloco[21:23]
            arquivo.blocoN440_subtipo00.totalChequesPrazo = bloco[23:26]
            arquivo.blocoN440_subtipo00.filler = bloco[26:114]

        if bloco[4:6] == '01':
            arquivo.blocoN440_subtipo01.tipoReg = bloco[0:4]
            arquivo.blocoN440_subtipo01.subtipo = bloco[4:6]
            arquivo.blocoN440_subtipo01.dataEmissaoPrimeiroChequeVista = bloco[6:10]
            arquivo.blocoN440_subtipo01.dataEmissaoUltimoChequeVista = bloco[10:14]
            arquivo.blocoN440_subtipo01.totalChequesUltimos15DiasPrazo = bloco[14:17]
            arquivo.blocoN440_subtipo01.totalChequesUltimos30DiasPrazo = bloco[17:19]
            arquivo.blocoN440_subtipo01.totalChequesUltimos60DiasPrazo = bloco[19:21]
            arquivo.blocoN440_subtipo01.totalChequesUltimos90DiasPrazo = bloco[21:23]
            arquivo.blocoN440_subtipo01.totalChequesPrazo = bloco[23:26]
            arquivo.blocoN440_subtipo01.filler = bloco[26:114]
            tipoReg = None

        if bloco[4:6] == '02':
            arquivo.blocoN440_subtipo02.tipoReg = bloco[0:4]
            arquivo.blocoN440_subtipo02.subtipo = bloco[4:6]
            arquivo.blocoN440_subtipo02.PrimeiroRecenteNomeEmpr = bloco[6:31]
            arquivo.blocoN440_subtipo02.PrimeiroRecenteData = bloco[31:35]
            arquivo.blocoN440_subtipo02.SegundoRecenteNomeEmpr = bloco[35:60]
            arquivo.blocoN440_subtipo02.SegundoRecenteData = bloco[60:64]
            arquivo.blocoN440_subtipo02.TericeiroRecenteNomeEmpr = bloco[64:89]
            arquivo.blocoN440_subtipo02.TericeiroRecenteData = bloco[89:93]
            arquivo.blocoN440_subtipo02.filler = bloco[93:114]

        if bloco[4:6] == '03':
            arquivo.blocoN440_subtipo03.tipoReg = bloco[0:4]
            arquivo.blocoN440_subtipo03.subtipo = bloco[4:6]
            arquivo.blocoN440_subtipo03.qtdConsultaUltimos15Dias = bloco[6:9]
            arquivo.blocoN440_subtipo03.qtdConsultaUltimos30Dias = bloco[9:12]
            arquivo.blocoN440_subtipo03.qtdConsultaUltimos60Dias = bloco[12:15]
            arquivo.blocoN440_subtipo03.qtdConsultaUltimos90Dias = bloco[15:18]
            arquivo.blocoN440_subtipo03.filler = bloco[18:114]

        if bloco[4:6] == '99':
            arquivo.blocoN440_subtipo99.tipoReg = bloco[0:4]
            arquivo.blocoN440_subtipo99.subtipo = bloco[4:6]
            arquivo.blocoN440_subtipo99.msgR440 = bloco[6:46]
            arquivo.blocoN440_subtipo99.filler = bloco[46:114]

        return arquivo
        
    def T999(self, bloco, arquivo):
        arquivo.blocoT999.tipoReg = bloco[0:4]
        arquivo.blocoT999.codigo = bloco[4:7]
        arquivo.blocoT999.mensagem = bloco[7:77]
        arquivo.blocoT999.filler = bloco[77:114]

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
            arquivo = self.N003(bloco, arquivo)
        elif blocoCodigo == 'N200':
            arquivo = self.N200(bloco, arquivo)
        elif blocoCodigo == 'N210':
            arquivo = self.N210(bloco, arquivo)
        elif blocoCodigo == 'N220':
            arquivo = self.N220(bloco, arquivo)
        elif blocoCodigo == 'N230':
            arquivo = self.N230(bloco, arquivo)
        elif blocoCodigo == 'N240':
            arquivo = self.N240(bloco, arquivo)
        elif blocoCodigo == 'N250':
            arquivo = self.N250(bloco, arquivo)
        elif blocoCodigo == 'N270':
            arquivo = self.N270(bloco, arquivo)
        elif blocoCodigo == 'N440':
            arquivo = self.N440(bloco, arquivo)
        elif blocoCodigo == 'T999':
            arquivo = self.T999(bloco, arquivo)

        return arquivo

    def parserStringDadosRetorno(self, stringDadosRetorno):
        stringDadosRetorno = stringDadosRetorno + 'T999'
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