# -*- coding: utf-8 -*-

from campos import Campo
from tiposCampos import campoData
from tiposCampos import campoDinheiro


class RegistrosB49C(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'protocolo', bloco, 4))
        self.campos.append(Campo(2, 4, 'codEstacaoChamadora', bloco, 6))
        self.campos.append(Campo(3, 10, 'numDocumentoConsultado', bloco, 15))
        self.campos.append(Campo(4, 25, 'tipoPessoaConsultado', bloco, 1))
        self.campos.append(Campo(5, 26, 'baseCons', bloco, 6))
        self.campos.append(Campo(6, 32, 'modalidade', bloco, 2))
        self.campos.append(Campo(7, 34, 'vlrConsul', bloco, 7))
        self.campos.append(Campo(8, 41, 'centroCusto', bloco, 12))
        self.campos.append(Campo(9, 53, 'codificado', bloco, 1))
        self.campos.append(Campo(10, 54, 'qtdRegistros', bloco, 2))
        self.campos.append(Campo(11, 56, 'conversa', bloco, 1))
        self.campos.append(Campo(12, 57, 'funcao', bloco, 3))
        self.campos.append(Campo(13, 60, 'tipoConsulta', bloco, 1))
        self.campos.append(Campo(14, 61, 'atualiza', bloco, 1))
        self.campos.append(Campo(15, 62, 'ident_term', bloco, 18))
        self.campos.append(Campo(16, 80, 'rescli', bloco, 10))
        self.campos.append(Campo(17, 90, 'delts', bloco, 1))
        self.campos.append(Campo(18, 91, 'cobra', bloco, 1))
        self.campos.append(Campo(19, 92, 'passa', bloco, 1))
        self.campos.append(Campo(20, 93, 'consCollec', bloco, 1))
        self.campos.append(Campo(21, 94, 'localizador', bloco, 1))
        self.campos.append(Campo(22, 95, 'docCredor', bloco, 9))
        self.campos.append(Campo(23, 104, 'qtdCheque', bloco, 2))
        self.campos.append(Campo(24, 106, 'endTel', bloco, 1))
        self.campos.append(Campo(25, 107, 'qtdCho1', bloco, 2))
        self.campos.append(Campo(26, 109, 'scoCho1', bloco, 1))
        self.campos.append(Campo(27, 110, 'tarCho1', bloco, 1))
        self.campos.append(Campo(28, 111, 'naoCobrarBureau', bloco, 1))
        self.campos.append(Campo(29, 112, 'autoPosit', bloco, 1))
        self.campos.append(Campo(30, 113, 'bureauViaSiteTransacional', bloco, 1))
        self.campos.append(Campo(31, 114, 'querTel9Digitos', bloco, 1))
        self.campos.append(Campo(32, 115, 'ctaCorrente', bloco, 10))
        self.campos.append(Campo(33, 125, 'dgCtaCorrente', bloco, 1))
        self.campos.append(Campo(34, 126, 'agencia', bloco, 4))
        self.campos.append(Campo(35, 130, 'alerta', bloco, 1))
        self.campos.append(Campo(36, 131, 'logon', bloco, 8))
        self.campos.append(Campo(37, 139, 'viaInternet', bloco, 1))
        self.campos.append(Campo(38, 140, 'resposta', bloco, 1))
        self.campos.append(Campo(39, 141, 'periodoCompro', bloco, 1))
        self.campos.append(Campo(40, 142, 'periodoEndereco', bloco, 1))
        self.campos.append(Campo(41, 143, 'backtest', bloco, 1))
        self.campos.append(Campo(42, 144, 'dtQuality', bloco, 1))
        self.campos.append(Campo(43, 145, 'prdOrigem', bloco, 2))
        self.campos.append(Campo(44, 147, 'trnOrigem', bloco, 4))
        self.campos.append(Campo(45, 151, 'consultante', bloco, 15))
        self.campos.append(Campo(46, 166, 'tpOr', bloco, 1))
        self.campos.append(Campo(47, 167, 'cnpjSoftware', bloco, 9))
        self.campos.append(Campo(48, 176, 'filler', bloco, 15))
        self.campos.append(Campo(49, 191, 'qtdCompr', bloco, 2))
        self.campos.append(Campo(50, 193, 'negativos', bloco, 1))
        self.campos.append(Campo(51, 194, 'cheque', bloco, 1))
        self.campos.append(campoData(52, 195, 'dataConsul', bloco, 8))
        self.campos.append(Campo(53, 203, 'horaConsul', bloco, 6))
        self.campos.append(Campo(54, 209, 'totalReg', bloco, 4))
        self.campos.append(Campo(55, 213, 'qtdReg1', bloco, 4))
        self.campos.append(Campo(56, 217, 'codTab', bloco, 4))
        self.campos.append(Campo(57, 221, 'itemTsDados', bloco, 4))
        self.campos.append(Campo(58, 225, 'tsDados', bloco, 16))
        self.campos.append(Campo(59, 241, 'tsScore1', bloco, 16))
        self.campos.append(Campo(60, 257, 'tsBp49', bloco, 16))
        self.campos.append(Campo(61, 273, 'tsAutor', bloco, 16))
        self.campos.append(Campo(62, 289, 'itemTsAutor', bloco, 4))
        self.campos.append(Campo(63, 293, 'itemTsScor1', bloco, 4))
        self.campos.append(Campo(64, 297, 'itemTsBp49', bloco, 4))
        self.campos.append(Campo(65, 301, 'itemTsDados2', bloco, 4))
        self.campos.append(Campo(66, 305, 'tsDados2', bloco, 16))
        self.campos.append(Campo(67, 321, 'fase1', bloco, 1))
        self.campos.append(Campo(68, 322, 'fase2', bloco, 1))
        self.campos.append(Campo(69, 323, 'dbTabela', bloco, 30))
        self.campos.append(Campo(70, 353, 'codAut', bloco, 1))
        self.campos.append(Campo(71, 354, 'operid', bloco, 3))
        self.campos.append(Campo(72, 357, 'reciCompr', bloco, 1))
        self.campos.append(Campo(73, 358, 'reciPagto', bloco, 1))
        self.campos.append(Campo(74, 359, 'filler2', bloco, 38))
        self.campos.append(Campo(75, 397, 'acessRechq', bloco, 1))
        self.campos.append(Campo(76, 398, 'temOcorrenciaRecheque', bloco, 1))
        self.campos.append(Campo(77, 399, 'reservado', bloco, 1))


class RegistrosP002(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'cod1', bloco, 4))
        self.campos.append(Campo(3, 8, 'chave1', bloco, 21))
        self.campos.append(Campo(4, 29, 'cod2', bloco, 4))
        self.campos.append(Campo(5, 33, 'chave2', bloco, 21))
        self.campos.append(Campo(6, 54, 'cod3', bloco, 4))
        self.campos.append(Campo(7, 58, 'chave3', bloco, 21))
        self.campos.append(Campo(8, 79, 'cod4', bloco, 4))
        self.campos.append(Campo(9, 83, 'chave4', bloco, 21))
        self.campos.append(Campo(10, 104, 'filler', bloco, 11))


class RegistrosN001(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subTipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoConsulta', bloco, 2))
        self.campos.append(Campo(4, 8, 'transacaoConsulta', bloco, 4))
        self.campos.append(Campo(5, 12, 'solGrandeVarejo', bloco, 1))
        self.campos.append(Campo(6, 13, 'idCheque', bloco, 1))
        self.campos.append(Campo(7, 14, 'agrupa', bloco, 1))
        self.campos.append(Campo(8, 15, 'consultaSintetica', bloco, 1))
        self.campos.append(Campo(9, 16, 'reservado', bloco, 1))
        self.campos.append(Campo(10, 17, 'anotacoesResumo', bloco, 1))
        self.campos.append(Campo(11, 18, 'chaveConsulta', bloco, 6))
        self.campos.append(Campo(12, 24, 'fantasia', bloco, 12))
        self.campos.append(Campo(13, 36, 'statusBanco', bloco, 1))
        self.campos.append(Campo(14, 37, 'filler', bloco, 13))
        self.campos.append(Campo(15, 50, 'trataTel', bloco, 1))
        self.campos.append(Campo(16, 51, 'filler', bloco, 64))


class RegistrosN002_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'banco', bloco, 3))
        self.campos.append(Campo(4, 9, 'agencia', bloco, 4))
        self.campos.append(Campo(5, 13, 'contaCorrente', bloco, 15))
        self.campos.append(Campo(6, 29, 'chequeInicial', bloco, 6))
        self.campos.append(Campo(7, 34, 'digitoChequeInicial', bloco, 1))
        self.campos.append(Campo(8, 35, 'chequeFinal', bloco, 6))
        self.campos.append(Campo(9, 41, 'digitoChequeFinal', bloco, 1))
        self.campos.append(Campo(10, 42, 'cmc7Inicial', bloco, 30))
        self.campos.append(Campo(11, 72, 'cmc7Final', bloco, 30))
        self.campos.append(Campo(12, 102, 'filler', bloco, 13))


class RegistrosN002_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoDinheiro(3, 6, 'valorCheque', bloco, 15))
        self.campos.append(campoData(4, 21, 'dataVencimentoCheque', bloco, 8))
        self.campos.append(Campo(5, 29, 'filler', bloco, 86))


class RegistrosN003(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 6))
        self.campos.append(Campo(3, 6, 'ddd', bloco, 3))
        self.campos.append(Campo(4, 9, 'telefone', bloco, 8))
        self.campos.append(Campo(5, 18, 'cep', bloco, 9))
        self.campos.append(Campo(6, 27, 'uf', bloco, 4))
        self.campos.append(Campo(7, 29, 'featScor', bloco, 80))
        self.campos.append(Campo(8, 109, 'filler', bloco, 6))


class RegistrosN200_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nomeRazao', bloco, 70))
        self.campos.append(campoData(4, 76, 'dataNascFundacao', bloco, 8))
        self.campos.append(Campo(5, 84, 'situacaoDoc', bloco, 2))
        self.campos.append(campoData(6, 86, 'dataSituacaoDoc', bloco, 8))
        self.campos.append(Campo(7, 94, 'filler', bloco, 21))


class RegistrosN200_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nomeMae', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN210_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'numMensagem', bloco, 2))
        self.campos.append(Campo(4, 8, 'totalMensagem', bloco, 2))
        self.campos.append(Campo(5, 10, 'tipoDoc', bloco, 6))
        self.campos.append(Campo(6, 16, 'numDoc', bloco, 20))
        self.campos.append(Campo(7, 36, 'motivo', bloco, 4))
        self.campos.append(campoData(8, 40, 'dataOcorrencia', bloco, 10))
        self.campos.append(Campo(9, 50, 'filler', bloco, 59))


class RegistrosN210_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 4))
        self.campos.append(Campo(3, 6, 'ddd1', bloco, 3))
        self.campos.append(Campo(4, 9, 'fone1', bloco, 8))
        self.campos.append(Campo(5, 17, 'ddd2', bloco, 3))
        self.campos.append(Campo(6, 21, 'fone2', bloco, 8))
        self.campos.append(Campo(7, 28, 'ddd3', bloco, 3))
        self.campos.append(Campo(8, 31, 'fone3', bloco, 8))
        self.campos.append(Campo(9, 39, 'filler', bloco, 76))


class RegistrosN210_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR210', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN220(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgNadaConsta', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN230_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'modalidade', bloco, 30))
        self.campos.append(Campo(5, 44, 'avalista', bloco, 1))
        self.campos.append(Campo(6, 45, 'tipoMoeda', bloco, 3))
        self.campos.append(campoDinheiro(7, 48, 'valor', bloco, 15))
        self.campos.append(Campo(8, 63, 'contrato', bloco, 16))
        self.campos.append(Campo(9, 79, 'origem', bloco, 30))
        self.campos.append(Campo(10, 109, 'siglaEmbratel', bloco, 4))
        self.campos.append(Campo(11, 113, 'filler', bloco, 2))


class RegistrosN230_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(campoData(4, 11, 'dataOcorrenciaAntiga', bloco, 6))
        self.campos.append(campoData(5, 17, 'dataOcorrenciaRecente', bloco, 6))
        self.campos.append(campoDinheiro(6, 23, 'valorTotal', bloco, 15))
        self.campos.append(Campo(7, 38, 'filler', bloco, 77))


class RegistrosN230_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR230', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN240_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'modalidade', bloco, 30))
        self.campos.append(Campo(5, 44, 'avalista', bloco, 1))
        self.campos.append(Campo(6, 45, 'tipoMoeda', bloco, 3))
        self.campos.append(campoDinheiro(7, 48, 'valor', bloco, 15))
        self.campos.append(Campo(8, 63, 'contrato', bloco, 16))
        self.campos.append(Campo(9, 79, 'origem', bloco, 30))
        self.campos.append(Campo(10, 109, 'siglaEmbratel', bloco, 4))
        self.campos.append(Campo(11, 113, 'filler', bloco, 2))


class RegistrosN240_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'subjudice', bloco, 1))
        self.campos.append(Campo(4, 7, 'msgSubjudice', bloco, 76))
        self.campos.append(Campo(5, 83, 'tipoAnotacao', bloco, 1))
        self.campos.append(Campo(6, 84, 'codCadus', bloco, 10))
        self.campos.append(Campo(7, 94, 'filler', bloco, 21))


class RegistrosN240_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(campoData(4, 11, 'dataOcorrenciaAntiga', bloco, 6))
        self.campos.append(campoData(5, 17, 'dataOcorrenciaRecente', bloco, 6))
        self.campos.append(campoDinheiro(6, 23, 'valorTotal', bloco, 15))
        self.campos.append(Campo(7, 38, 'tipoAnotacao', bloco, 1))
        self.campos.append(Campo(8, 39, 'filler', bloco, 16))


class RegistrosN240_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR240', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN250_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'tipoMoeda', bloco, 3))
        self.campos.append(campoDinheiro(5, 17, 'valor', bloco, 15))
        self.campos.append(Campo(6, 32, 'cartorio', bloco, 2))
        self.campos.append(Campo(7, 34, 'cidade', bloco, 30))
        self.campos.append(Campo(8, 64, 'uf', bloco, 2))


class RegistrosN250_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'subjudice', bloco, 1))
        self.campos.append(Campo(4, 7, 'msgSubjudice', bloco, 76))
        self.campos.append(Campo(5, 83, 'tipoAnotacao', bloco, 1))
        self.campos.append(Campo(6, 84, 'codCadus', bloco, 10))
        self.campos.append(Campo(7, 94, 'filler', bloco, 21))


class RegistrosN250_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(campoData(4, 11, 'dataOcorrenciaAntiga', bloco, 6))
        self.campos.append(campoData(5, 17, 'dataOcorrenciaRecente', bloco, 6))
        self.campos.append(Campo(6, 23, 'moeda', bloco, 3))
        self.campos.append(campoDinheiro(7, 26, 'valorTotal', bloco, 15))
        self.campos.append(Campo(8, 41, 'filler', bloco, 74))


class RegistrosN250_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR250', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN270_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'cheque', bloco, 10))
        self.campos.append(Campo(5, 24, 'alinea', bloco, 5))
        self.campos.append(Campo(6, 29, 'quantidade', bloco, 5))
        self.campos.append(Campo(7, 34, 'valor', bloco, 15))
        self.campos.append(Campo(8, 49, 'numBanco', bloco, 3))
        self.campos.append(Campo(9, 52, 'nomeBanco', bloco, 14))
        self.campos.append(Campo(10, 66, 'agencia', bloco, 4))
        self.campos.append(Campo(11, 70, 'cidade', bloco, 30))
        self.campos.append(Campo(12, 100, 'uf', bloco, 2))
        self.campos.append(Campo(13, 102, 'codCadus', bloco, 10))
        self.campos.append(Campo(14, 112, 'filler', bloco, 3))


class RegistrosN270_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(campoData(4, 11, 'dataOcorrenciaAntiga', bloco, 8))
        self.campos.append(campoData(5, 19, 'dataOcorrenciaRecente', bloco, 8))
        self.campos.append(Campo(6, 27, 'banco', bloco, 3))
        self.campos.append(Campo(7, 30, 'agencia', bloco, 4))
        self.campos.append(Campo(8, 34, 'nomeFantasiaBanco', bloco, 12))
        self.campos.append(Campo(9, 46, 'filler', bloco, 69))


class RegistrosN270_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR270', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN300_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 40))
        self.campos.append(campoData(4, 46, 'dataAbertura', bloco, 8))
        self.campos.append(Campo(5, 54, 'tipoPessoa', bloco, 1))
        self.campos.append(Campo(6, 55, 'numDoc', bloco, 15))
        self.campos.append(Campo(7, 70, 'nomeRazaoSocial', bloco, 40))
        self.campos.append(Campo(8, 110, 'filler', bloco, 5))


class RegistrosN300_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoDoc', bloco, 1))
        self.campos.append(Campo(4, 7, 'numDocIdentificacao', bloco, 15))
        self.campos.append(Campo(5, 22, 'orgaoEmissor', bloco, 5))
        self.campos.append(Campo(6, 27, 'ufDocIdentificacao', bloco, 2))
        self.campos.append(campoData(7, 29, 'dataEmissaoDocumento', bloco, 8))
        self.campos.append(Campo(8, 37, 'filler', bloco, 78))


class RegistrosN300_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'banco', bloco, 3))
        self.campos.append(Campo(4, 9, 'indicadorParticipacao', bloco, 1))
        self.campos.append(Campo(5, 10, 'msgR300', bloco, 36))
        self.campos.append(Campo(6, 46, 'filler', bloco, 69))


class RegistrosN310_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'banco', bloco, 3))
        self.campos.append(Campo(4, 9, 'agencia', bloco, 4))
        self.campos.append(Campo(5, 13, 'conta', bloco, 10))
        self.campos.append(Campo(6, 23, 'chequeInicial', bloco, 6))
        self.campos.append(Campo(7, 29, 'chequeFinal', bloco, 6))
        self.campos.append(Campo(8, 35, 'motivo', bloco, 12))
        self.campos.append(campoData(9, 47, 'dataCadastramento', bloco, 8))
        self.campos.append(Campo(10, 55, 'horaCadastramento', bloco, 4))
        self.campos.append(Campo(11, 59, 'codFonte', bloco, 4))
        self.campos.append(Campo(12, 63, 'filler', bloco, 52))


class RegistrosN310_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR310', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN320_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'banco', bloco, 3))
        self.campos.append(Campo(4, 9, 'agencia', bloco, 4))
        self.campos.append(Campo(5, 13, 'conta', bloco, 10))
        self.campos.append(Campo(6, 23, 'chequeInicial', bloco, 6))
        self.campos.append(Campo(7, 29, 'chequeFinal', bloco, 6))
        self.campos.append(Campo(8, 35, 'motivo', bloco, 12))
        self.campos.append(campoData(9, 47, 'dataCadastro', bloco, 8))
        self.campos.append(Campo(10, 55, 'codFonte', bloco, 4))
        self.campos.append(Campo(11, 59, 'filler', bloco, 56))


class RegistrosN320_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(campoData(4, 11, 'dataOcorAntiga', bloco, 8))
        self.campos.append(campoData(5, 19, 'dataOcorRecente', bloco, 8))
        self.campos.append(Campo(6, 27, 'filler', bloco, 88))


class RegistrosN320_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR320', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN330_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'primeiraVerificacao', bloco, 1))
        self.campos.append(Campo(4, 7, 'numCheque', bloco, 6))
        self.campos.append(Campo(5, 13, 'qtdConsultasCheque', bloco, 3))
        self.campos.append(campoData(6, 16, 'dataAntiga', bloco, 8))
        self.campos.append(campoData(7, 24, 'dataRecente', bloco, 8))
        self.campos.append(Campo(8, 32, 'nomeEmpresa', bloco, 20))
        self.campos.append(Campo(9, 52, 'totalRegSegundaVerificacao', bloco, 3))
        self.campos.append(Campo(10, 55, 'totalRegContaCorrente', bloco, 3))
        self.campos.append(Campo(11, 58, 'filler', bloco, 57))


class RegistrosN330_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoDoc', bloco, 1))
        self.campos.append(Campo(4, 7, 'numDoc', bloco, 15))
        self.campos.append(Campo(5, 22, 'nomeRazao', bloco, 40))
        self.campos.append(Campo(6, 62, 'qtdConsultas', bloco, 3))
        self.campos.append(campoData(7, 65, 'dataOcorrenciaAntiga', bloco, 8))
        self.campos.append(campoData(8, 73, 'dataOcorrenciaRecente', bloco, 8))
        self.campos.append(Campo(9, 81, 'nomeEmpresaConsultante', bloco, 20))
        self.campos.append(Campo(10, 101, 'filler', bloco, 14))


class RegistrosN330_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoDoc', bloco, 1))
        self.campos.append(Campo(4, 7, 'numDoc', bloco, 15))
        self.campos.append(Campo(5, 22, 'nomeRazao', bloco, 40))
        self.campos.append(Campo(6, 62, 'qtdConsultas', bloco, 3))
        self.campos.append(Campo(7, 65, 'numUltimoCheque', bloco, 6))
        self.campos.append(campoData(8, 71, 'dataOcorrenciaAntiga', bloco, 8))
        self.campos.append(campoData(9, 79, 'dataOcorrenciaRecente', bloco, 8))
        self.campos.append(Campo(10, 87, 'filler', bloco, 28))


class RegistrosN330_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR330', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN400_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nomeAgencia', bloco, 70))
        self.campos.append(Campo(4, 76, 'dataUltimaAtualizacao', bloco, 8))
        self.campos.append(Campo(5, 84, 'dddFone', bloco, 4))
        self.campos.append(Campo(6, 88, 'numFone', bloco, 8))
        self.campos.append(Campo(7, 96, 'dddFax', bloco, 4))
        self.campos.append(Campo(8, 100, 'numFax', bloco, 8))
        self.campos.append(Campo(9, 108, 'filler', bloco, 7))


class RegistrosN400_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'endAgencia', bloco, 70))
        self.campos.append(Campo(4, 76, 'cidade', bloco, 30))
        self.campos.append(Campo(5, 106, 'uf', bloco, 2))
        self.campos.append(Campo(6, 108, 'filler', bloco, 7))


class RegistrosN400_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR400', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN410_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'enderecoCep', bloco, 70))
        self.campos.append(Campo(4, 76, 'bairro', bloco, 30))
        self.campos.append(Campo(5, 106, 'filler', bloco, 9))


class RegistrosN410_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'cidade', bloco, 30))
        self.campos.append(Campo(4, 36, 'uf', bloco, 2))
        self.campos.append(Campo(5, 38, 'cepGenerico', bloco, 1))
        self.campos.append(Campo(6, 39, 'filler', bloco, 76))


class RegistrosN410_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR410', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN420_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 4))
        self.campos.append(Campo(3, 6, 'docConfere', bloco, 4))
        self.campos.append(Campo(4, 7, 'nomeAssinante', bloco, 4))
        self.campos.append(Campo(5, 77, 'tipoDocAssinante', bloco, 4))
        self.campos.append(Campo(6, 78, 'classeAssinante', bloco, 4))
        self.campos.append(campoData(7, 79, 'dataInstalacao', bloco, 4))
        self.campos.append(Campo(8, 87, 'filler', bloco, 4))


class RegistrosN420_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'logradouroAssinante', bloco, 70))
        self.campos.append(Campo(4, 76, 'bairroAssinante', bloco, 30))
        self.campos.append(Campo(5, 106, 'filler', bloco, 9))


class RegistrosN420_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'cidadeAssinante', bloco, 30))
        self.campos.append(Campo(4, 36, 'cepAssinante', bloco, 8))
        self.campos.append(Campo(5, 44, 'filler', bloco, 71))


class RegistrosN420_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'indicadorPesquisa', bloco, 1))
        self.campos.append(Campo(4, 7, 'msgR420', bloco, 40))
        self.campos.append(Campo(5, 47, 'filler', bloco, 68))


class RegistrosN430_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'ddd1', bloco, 3))
        self.campos.append(Campo(4, 9, 'fone1', bloco, 8))
        self.campos.append(Campo(5, 17, 'ddd2', bloco, 3))
        self.campos.append(Campo(6, 20, 'fone2', bloco, 8))
        self.campos.append(Campo(7, 28, 'ddd3', bloco, 3))
        self.campos.append(Campo(8, 31, 'fone3', bloco, 8))
        self.campos.append(Campo(9, 39, 'ddd4', bloco, 3))
        self.campos.append(Campo(10, 42, 'fone4', bloco, 8))
        self.campos.append(Campo(11, 50, 'ddd5', bloco, 3))
        self.campos.append(Campo(12, 53, 'fone5', bloco, 8))
        self.campos.append(Campo(13, 61, 'filler', bloco, 54))


class RegistrosN430_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR430', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN440_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataEmissaoPrimeiroChequeVista', bloco, 4))
        self.campos.append(campoData(4, 10, 'dataEmissaoUltimoChequeVista', bloco, 4))
        self.campos.append(Campo(5, 14, 'totalChequesUltimos15DiasPrazo', bloco, 3))
        self.campos.append(Campo(6, 17, 'totalChequesUltimos30DiasPrazo', bloco, 2))
        self.campos.append(Campo(7, 19, 'totalChequesUltimos60DiasPrazo', bloco, 2))
        self.campos.append(Campo(8, 21, 'totalChequesUltimos90DiasPrazo', bloco, 2))
        self.campos.append(Campo(9, 23, 'totalChequesPrazo', bloco, 3))
        self.campos.append(Campo(10, 26, 'filler', bloco, 89))


class RegistrosN440_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataEmissaoPrimeiroChequeVista', bloco, 4))
        self.campos.append(campoData(4, 10, 'dataEmissaoUltimoChequeVista', bloco, 4))
        self.campos.append(Campo(5, 14, 'totalChequesUltimos15DiasPrazo', bloco, 3))
        self.campos.append(Campo(6, 17, 'totalChequesUltimos30DiasPrazo', bloco, 2))
        self.campos.append(Campo(7, 19, 'totalChequesUltimos60DiasPrazo', bloco, 2))
        self.campos.append(Campo(8, 21, 'totalChequesUltimos90DiasPrazo', bloco, 2))
        self.campos.append(Campo(9, 23, 'totalChequesPrazo', bloco, 3))
        self.campos.append(Campo(10, 26, 'filler', bloco, 89))


class RegistrosN440_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'PrimeiroRecenteNomeEmpr', bloco, 25))
        self.campos.append(campoData(4, 31, 'PrimeiroRecenteData', bloco, 4))
        self.campos.append(Campo(5, 35, 'SegundoRecenteNomeEmpr', bloco, 25))
        self.campos.append(campoData(6, 60, 'SegundoRecenteData', bloco, 4))
        self.campos.append(Campo(7, 64, 'TericeiroRecenteNomeEmpr', bloco, 25))
        self.campos.append(campoData(8, 89, 'TericeiroRecenteData', bloco, 4))
        self.campos.append(Campo(9, 93, 'filler', bloco, 22))


class RegistrosN440_subtipo03(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'qtdConsultaUltimos15Dias', bloco, 3))
        self.campos.append(Campo(4, 9, 'qtdConsultaUltimos30Dias', bloco, 3))
        self.campos.append(Campo(5, 12, 'qtdConsultaUltimos60Dias', bloco, 3))
        self.campos.append(Campo(6, 15, 'qtdConsultaUltimos90Dias', bloco, 33))
        self.campos.append(Campo(7, 18, 'filler', bloco, 97))


class RegistrosN440_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR440', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN460_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'varaCivel', bloco, 4))
        self.campos.append(Campo(5, 18, 'numDistribuidor', bloco, 4))
        self.campos.append(Campo(6, 22, 'codNatureza', bloco, 3))
        self.campos.append(campoDinheiro(7, 25, 'valorAcao', bloco, 15))
        self.campos.append(Campo(8, 40, 'praca', bloco, 4))
        self.campos.append(Campo(9, 44, 'uf', bloco, 2))
        self.campos.append(Campo(10, 46, 'cidade', bloco, 30))
        self.campos.append(Campo(11, 76, 'principal', bloco, 1))
        self.campos.append(Campo(12, 77, 'subJudice', bloco, 1))
        self.campos.append(Campo(13, 78, 'filial', bloco, 4))
        self.campos.append(Campo(14, 82, 'digito', bloco, 2))
        self.campos.append(campoData(15, 84, 'dataInclusaoAnotacao', bloco, 8))
        self.campos.append(Campo(16, 92, 'horaInclusaoAnotacao', bloco, 6))
        self.campos.append(Campo(17, 98, 'chaveCadus', bloco, 10))
        self.campos.append(Campo(18, 108, 'filler', bloco, 7))


class RegistrosN460_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'descNatureza', bloco, 30))
        self.campos.append(Campo(4, 36, 'filler', bloco, 79))


class RegistrosN460_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'praca', bloco, 4))
        self.campos.append(Campo(4, 10, 'distribuidor', bloco, 2))
        self.campos.append(Campo(5, 12, 'vara', bloco, 2))
        self.campos.append(campoData(6, 14, 'data', bloco, 8))
        self.campos.append(Campo(7, 22, 'processo', bloco, 16))
        self.campos.append(Campo(8, 38, 'filler', bloco, 77))


class RegistrosN460_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataInicio', bloco, 8))
        self.campos.append(campoData(4, 14, 'dataFinal', bloco, 8))
        self.campos.append(Campo(5, 22, 'qtdTotal', bloco, 9))
        self.campos.append(campoDinheiro(6, 31, 'valorTotal', bloco, 15))
        self.campos.append(Campo(7, 46, 'filler', bloco, 69))


class RegistrosN460_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR460', bloco, 70))
        self.campos.append(Campo(4, 76, 'filler', bloco, 39))


class RegistrosN470_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'natureza', bloco, 2))
        self.campos.append(Campo(5, 16, 'vara', bloco, 4))
        self.campos.append(Campo(6, 20, 'praca', bloco, 4))
        self.campos.append(Campo(7, 24, 'uf', bloco, 2))
        self.campos.append(Campo(8, 26, 'cidade', bloco, 30))
        self.campos.append(Campo(9, 56, 'filial', bloco, 4))
        self.campos.append(Campo(10, 60, 'digito', bloco, 2))
        self.campos.append(campoData(11, 62, 'dataInclusao', bloco, 8))
        self.campos.append(Campo(12, 70, 'horaInclusao', bloco, 6))
        self.campos.append(Campo(13, 76, 'cadus', bloco, 10))
        self.campos.append(Campo(14, 86, 'descricaoNatureza', bloco, 29))


class RegistrosN470_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(campoData(3, 6, 'dataInicio', bloco, 8))
        self.campos.append(campoData(4, 14, 'dataFinal', bloco, 8))
        self.campos.append(Campo(5, 22, 'qtdTotal', bloco, 9))
        self.campos.append(campoDinheiro(6, 31, 'valorTotal', bloco, 15))
        self.campos.append(Campo(7, 46, 'filler', bloco, 69))


class RegistrosN470_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR470', bloco, 70))
        self.campos.append(Campo(4, 76, 'filler', bloco, 39))


class RegistrosN480_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'natureza', bloco, 2))
        self.campos.append(Campo(5, 16, 'qualificacao', bloco, 3))
        self.campos.append(Campo(6, 19, 'vara', bloco, 4))
        self.campos.append(Campo(7, 23, 'cnpj', bloco, 9))
        self.campos.append(Campo(8, 32, 'nomeEmpresa', bloco, 50))
        self.campos.append(Campo(9, 82, 'filial', bloco, 4))
        self.campos.append(Campo(10, 86, 'digito', bloco, 2))
        self.campos.append(Campo(11, 88, 'dataInclusao', bloco, 8))
        self.campos.append(Campo(12, 96, 'horaInclusao', bloco, 6))
        self.campos.append(Campo(13, 102, 'cadus', bloco, 10))
        self.campos.append(Campo(14, 112, 'filler', bloco, 3))


class RegistrosN480_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'descNatureza', bloco, 30))
        self.campos.append(Campo(4, 36, 'filler', bloco, 79))


class RegistrosN480_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 4))
        self.campos.append(campoData(3, 6, 'dataInicial', bloco, 4))
        self.campos.append(campoData(4, 14, 'dataFinal', bloco, 4))
        self.campos.append(Campo(5, 22, 'qtdTotal', bloco, 4))
        self.campos.append(campoDinheiro(6, 31, 'valorTotal', bloco, 4))
        self.campos.append(Campo(7, 46, 'filler', bloco, 4))


class RegistrosN480_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR480', bloco, 70))
        self.campos.append(Campo(4, 76, 'filler', bloco, 39))


class RegistrosN500_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 4))
        self.campos.append(Campo(3, 6, 'codScore', bloco, 4))
        self.campos.append(Campo(4, 10, 'scoreCalculado', bloco, 4))
        self.campos.append(Campo(5, 11, 'pontuacao', bloco, 4))
        self.campos.append(Campo(6, 17, 'msgR500', bloco, 4))
        self.campos.append(Campo(7, 87, 'delinRate', bloco, 4))
        self.campos.append(Campo(8, 92, 'range', bloco, 4))
        self.campos.append(Campo(9, 98, 'codMsg', bloco, 4))
        self.campos.append(Campo(10, 104, 'filler', bloco, 4))


class RegistrosN505_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'sequencia', bloco, 4))
        self.campos.append(Campo(4, 10, 'mensagem', bloco, 100))
        self.campos.append(Campo(5, 110, 'filler', bloco, 5))


class RegistrosN505_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'codScore', bloco, 2))
        self.campos.append(Campo(4, 8, 'mensagem', bloco, 100))
        self.campos.append(Campo(5, 108, 'filler', bloco, 7))


class RegistrosN505_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'codScore', bloco, 4))
        self.campos.append(Campo(4, 10, 'mensagem', bloco, 100))
        self.campos.append(Campo(5, 110, 'filler', bloco, 5))


class RegistrosN600_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'indicativoValCli', bloco, 1))
        self.campos.append(Campo(4, 7, 'valCliente', bloco, 15))
        self.campos.append(Campo(5, 22, 'valCheque', bloco, 15))
        self.campos.append(Campo(6, 37, 'indValorVista', bloco, 1))
        self.campos.append(Campo(7, 38, 'valorVista', bloco, 15))
        self.campos.append(Campo(8, 53, 'indValorPrazo', bloco, 1))
        self.campos.append(Campo(9, 54, 'valorPrazo', bloco, 15))
        self.campos.append(Campo(10, 69, 'indDataBloqueio', bloco, 1))
        self.campos.append(Campo(11, 70, 'dataBloqueio', bloco, 8))
        self.campos.append(Campo(12, 78, 'indLimiteIndividual', bloco, 1))
        self.campos.append(Campo(13, 79, 'indDataVip', bloco, 1))
        self.campos.append(Campo(14, 80, 'dataVip', bloco, 8))
        self.campos.append(Campo(15, 88, 'indCheques', bloco, 1))
        self.campos.append(Campo(16, 89, 'indFraude', bloco, 1))
        self.campos.append(Campo(17, 90, 'filler', bloco, 25))


class RegistrosN600_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataVencimento', bloco, 8))
        self.campos.append(Campo(4, 14, 'indCheque', bloco, 1))
        self.campos.append(Campo(5, 15, 'valorCheque', bloco, 15))
        self.campos.append(Campo(6, 30, 'dataCompra', bloco, 8))
        self.campos.append(Campo(7, 38, 'banco', bloco, 3))
        self.campos.append(Campo(8, 41, 'numCheque', bloco, 6))
        self.campos.append(Campo(9, 47, 'nomeCredor', bloco, 23))
        self.campos.append(Campo(10, 70, 'loja', bloco, 4))
        self.campos.append(Campo(11, 74, 'tipoDoc', bloco, 1))
        self.campos.append(Campo(12, 75, 'numDoc', bloco, 15))
        self.campos.append(Campo(13, 90, 'filler', bloco, 25))


class RegistrosN600_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'indValores', bloco, 1))
        self.campos.append(Campo(4, 7, 'mesano', bloco, 4))
        self.campos.append(Campo(5, 11, 'indValorVencer', bloco, 1))
        self.campos.append(campoDinheiro(6, 12, 'valorVencer', bloco, 15))
        self.campos.append(Campo(7, 27, 'indValorSaldo', bloco, 1))
        self.campos.append(campoDinheiro(8, 28, 'valorSaldo', bloco, 15))
        self.campos.append(Campo(9, 43, 'indValorLimite', bloco, 1))
        self.campos.append(campoDinheiro(10, 44, 'valorLimite', bloco, 15))
        self.campos.append(Campo(11, 59, 'indValorExcedente', bloco, 1))
        self.campos.append(campoDinheiro(12, 60, 'valorExcedente', bloco, 15))
        self.campos.append(Campo(13, 75, 'filler', bloco, 40))


class RegistrosN600_subtipo03(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 0, 'subtipo', bloco, 4))
        self.campos.append(Campo(3, 0, 'indTotalVencer', bloco, 4))
        self.campos.append(Campo(4, 0, 'totalVencer', bloco, 4))
        self.campos.append(Campo(5, 0, 'indSaldoVencer', bloco, 4))
        self.campos.append(Campo(6, 0, 'totalSaldoVencer', bloco, 4))
        self.campos.append(Campo(7, 0, 'indExcedenteVencer', bloco, 4))
        self.campos.append(Campo(8, 0, 'totalExcedenteVencer', bloco, 4))
        self.campos.append(Campo(9, 0, 'filler', bloco, 4))


class RegistrosN600_subtipo04(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'tipoReg', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoReg', bloco, 1))
        self.campos.append(Campo(4, 7, 'tipoReg', bloco, 15))
        self.campos.append(Campo(5, 22, 'tipoReg', bloco, 1))
        self.campos.append(Campo(6, 23, 'tipoReg', bloco, 15))
        self.campos.append(Campo(7, 38, 'tipoReg', bloco, 1))
        self.campos.append(Campo(8, 39, 'tipoReg', bloco, 15))
        self.campos.append(Campo(9, 54, 'tipoReg', bloco, 61))


class RegistrosN600_subtipo05(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'indTotalPrazo', bloco, 1))
        self.campos.append(Campo(4, 7, 'totalPrazo', bloco, 15))
        self.campos.append(Campo(5, 22, 'indSaldoPrazo', bloco, 1))
        self.campos.append(Campo(6, 23, 'totalSaldoPrazo', bloco, 15))
        self.campos.append(Campo(7, 38, 'indExcedentePrazo', bloco, 1))
        self.campos.append(Campo(8, 39, 'totalExcedentePrazo', bloco, 15))
        self.campos.append(Campo(9, 54, 'filler', bloco, 61))


class RegistrosN610_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'codScore', bloco, 4))
        self.campos.append(Campo(4, 10, 'pontuacao', bloco, 4))
        self.campos.append(Campo(5, 14, 'inadimplencia', bloco, 7))
        self.campos.append(Campo(6, 21, 'mensagem', bloco, 80))
        self.campos.append(Campo(7, 101, 'filler', bloco, 14))


class RegistrosN610_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 29))


class RegistrosN620_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'valorLimite', bloco, 13))
        self.campos.append(Campo(4, 19, 'filler', bloco, 96))


class RegistrosN620_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 30))


class RegistrosN620_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 30))


class RegistrosN630_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'classe', bloco, 1))
        self.campos.append(Campo(4, 7, 'pontuacao', bloco, 4))
        self.campos.append(Campo(5, 11, 'mensagem', bloco, 80))
        self.campos.append(Campo(6, 91, 'filler', bloco, 24))


class RegistrosN630_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR630', bloco, 40))
        self.campos.append(Campo(4, 46, 'tipoReg', bloco, 29))


class RegistrosN640_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'valor', bloco, 18))
        self.campos.append(Campo(4, 24, 'filler', bloco, 90))


class RegistrosN640_subtipo90(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 100))
        self.campos.append(Campo(4, 106, 'filler', bloco, 8))


class RegistrosN640_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 80))
        self.campos.append(Campo(4, 46, 'filler', bloco, 29))


class RegistrosN650_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'logradouro', bloco, 60))
        self.campos.append(Campo(4, 66, 'numero', bloco, 6))
        self.campos.append(Campo(5, 72, 'filler', bloco, 43))


class RegistrosN650_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'complemento', bloco, 40))
        self.campos.append(Campo(4, 66, 'bairro', bloco, 30))
        self.campos.append(Campo(5, 96, 'filler', bloco, 39))


class RegistrosN650_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'municipio', bloco, 30))
        self.campos.append(Campo(4, 36, 'cep', bloco, 8))
        self.campos.append(Campo(5, 44, 'uf', bloco, 2))
        self.campos.append(Campo(6, 48, 'ddd', bloco, 4))
        self.campos.append(Campo(7, 52, 'telefone', bloco, 9))
        self.campos.append(Campo(8, 61, 'filler', bloco, 56))


class RegistrosN650_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 4))
        self.campos.append(Campo(3, 6, 'tipoReg', bloco, 4))
        self.campos.append(Campo(4, 86, 'tipoReg', bloco, 4))


class RegistrosN660_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'renda', bloco, 9))
        self.campos.append(Campo(4, 15, 'mensagem', bloco, 80))
        self.campos.append(Campo(5, 95, 'filler', bloco, 20))


class RegistrosN660_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 80))
        self.campos.append(Campo(4, 86, 'filler', bloco, 29))


class RegistrosN670_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'data', bloco, 8))
        self.campos.append(Campo(4, 14, 'filler', bloco, 101))


class RegistrosN670_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 80))
        self.campos.append(Campo(4, 86, 'filler', bloco, 29))


class RegistrosN680_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'faixa', bloco, 2))
        self.campos.append(Campo(4, 8, 'mensagem', bloco, 72))
        self.campos.append(Campo(5, 80, 'filler', bloco, 35))


class RegistrosN680_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 80))
        self.campos.append(Campo(4, 86, 'filler', bloco, 29))


class RegistrosN690_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nome', bloco, 40))
        self.campos.append(Campo(4, 46, 'cnpj', bloco, 14))
        self.campos.append(Campo(5, 60, 'participacao', bloco, 5))
        self.campos.append(Campo(6, 65, 'uf', bloco, 2))
        self.campos.append(Campo(7, 67, 'dataInicio', bloco, 8))
        self.campos.append(Campo(8, 75, 'dataAtualizacao', bloco, 8))
        self.campos.append(Campo(9, 83, 'filler', bloco, 32))


class RegistrosN690_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'mensagem', bloco, 80))
        self.campos.append(Campo(4, 87, 'filler', bloco, 29))


class RegistrosN700_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoPessoa', bloco, 1))
        self.campos.append(Campo(4, 7, 'docSocioAcionista', bloco, 14))
        self.campos.append(Campo(5, 21, 'nome', bloco, 60))
        self.campos.append(Campo(6, 81, 'capital', bloco, 4))
        self.campos.append(Campo(7, 85, 'filler', bloco, 30))


class RegistrosN700_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(1, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(1, 6, 'mensagem', bloco, 80))
        self.campos.append(Campo(1, 86, 'filler', bloco, 29))


class RegistrosN705_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoPessoa', bloco, 1))
        self.campos.append(Campo(4, 7, 'docAdministrador', bloco, 14))
        self.campos.append(Campo(5, 21, 'nome', bloco, 60))
        self.campos.append(Campo(6, 81, 'cargo', bloco, 20))
        self.campos.append(Campo(7, 85, 'filler', bloco, 14))


class RegistrosN705_subtipo99(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'tipoReg', bloco, 2))
        self.campos.append(Campo(3, 6, 'tipoReg', bloco, 80))
        self.campos.append(Campo(4, 86, 'tipoReg', bloco, 29))


class RegistrosI001_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'filler_1', bloco, 1))
        self.campos.append(Campo(4, 7, 'filler_2', bloco, 1))
        self.campos.append(Campo(5, 8, 'filler_3', bloco, 1))
        self.campos.append(Campo(6, 9, 'filler_4', bloco, 1))
        self.campos.append(Campo(7, 10, 'filler_5', bloco, 4))
        self.campos.append(Campo(8, 14, 'filler_6', bloco, 1))
        self.campos.append(Campo(9, 15, 'filler_7', bloco, 4))
        self.campos.append(Campo(10, 19, 'filler_8', bloco, 10))
        self.campos.append(Campo(11, 29, 'filler_9', bloco, 1))
        self.campos.append(Campo(12, 30, 'filler_10', bloco, 1))
        self.campos.append(Campo(13, 31, 'filler_11', bloco, 2))
        self.campos.append(Campo(14, 33, 'filler_12', bloco, 1))
        self.campos.append(Campo(15, 34, 'filler_13', bloco, 1))
        self.campos.append(Campo(16, 35, 'filler_14', bloco, 1))
        self.campos.append(Campo(17, 36, 'filler_15', bloco, 2))
        self.campos.append(Campo(18, 38, 'filler_16', bloco, 2))
        self.campos.append(Campo(19, 40, 'filler_17', bloco, 2))
        self.campos.append(Campo(20, 42, 'filler_18', bloco, 2))
        self.campos.append(Campo(21, 44, 'filler_19', bloco, 2))
        self.campos.append(Campo(22, 46, 'filler_20', bloco, 1))
        self.campos.append(Campo(23, 47, 'filler_21', bloco, 1))
        self.campos.append(Campo(24, 48, 'filler_22', bloco, 1))
        self.campos.append(Campo(25, 49, 'filler_23', bloco, 1))
        self.campos.append(Campo(26, 50, 'filler_24', bloco, 1))
        self.campos.append(Campo(27, 51, 'filler_25', bloco, 1))
        self.campos.append(Campo(28, 52, 'filler_26', bloco, 4))
        self.campos.append(Campo(29, 56, 'filler_27', bloco, 4))
        self.campos.append(Campo(30, 60, 'filler_28', bloco, 1))
        self.campos.append(Campo(31, 61, 'filler_29', bloco, 1))
        self.campos.append(Campo(32, 62, 'filler_30', bloco, 5))
        self.campos.append(Campo(33, 67, 'filler_31', bloco, 47))
        self.campos.append(Campo(34, 114, 'filler_32', bloco, 1))


class RegistrosI105(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nome', bloco, 70))
        self.campos.append(Campo(4, 76, 'filler', bloco, 39))


class RegistrosI110_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'data_inicial', bloco, 8))
        self.campos.append(Campo(4, 14, 'data_final', bloco, 8))
        self.campos.append(Campo(5, 22, 'qtd_total', bloco, 9))
        self.campos.append(Campo(6, 31, 'valor', bloco, 15))
        self.campos.append(Campo(7, 46, 'origem', bloco, 30))
        self.campos.append(Campo(8, 76, 'filler', bloco, 39))


class RegistrosI110_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'data_ocorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'numero_cartorio', bloco, 4))
        self.campos.append(Campo(5, 18, 'natureza', bloco, 3))
        self.campos.append(Campo(6, 21, 'valor', bloco, 15))
        self.campos.append(Campo(7, 36, 'praca', bloco, 4))
        self.campos.append(Campo(8, 40, 'uf', bloco, 2))
        self.campos.append(Campo(9, 42, 'cidade', bloco, 30))
        self.campos.append(Campo(10, 72, 'sub_judice', bloco, 1))
        self.campos.append(Campo(11, 73, 'data_carta', bloco, 8))
        self.campos.append(Campo(12, 81, 'filial_cnpj', bloco, 4))
        self.campos.append(Campo(13, 85, 'digito_doc', bloco, 2))
        self.campos.append(Campo(14, 87, 'data_inclusao', bloco, 8))
        self.campos.append(Campo(15, 95, 'hora_inclusao', bloco, 6))
        self.campos.append(Campo(16, 101, 'chv_cadus', bloco, 10))
        self.campos.append(Campo(17, 111, 'filler', bloco, 4))


class RegistrosI220_subtipo00(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'data_inicial', bloco, 8))
        self.campos.append(Campo(4, 14, 'data_final', bloco, 8))
        self.campos.append(Campo(5, 22, 'qtd_total', bloco, 9))
        self.campos.append(Campo(6, 31, 'valor', bloco, 15))
        self.campos.append(Campo(7, 46, 'tipo_ocorrencia', bloco, 1))
        self.campos.append(Campo(8, 47, 'origem', bloco, 16))
        self.campos.append(Campo(9, 63, 'filler', bloco, 52))


class RegistrosI220_subtipo01(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'data_ocorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'natureza', bloco, 3))
        self.campos.append(Campo(5, 17, 'valor', bloco, 15))
        self.campos.append(Campo(6, 32, 'praca', bloco, 4))
        self.campos.append(Campo(7, 36, 'filler_1', bloco, 32))
        self.campos.append(Campo(8, 68, 'principal', bloco, 1))
        self.campos.append(Campo(9, 69, 'contrato', bloco, 16))
        self.campos.append(Campo(10, 85, 'sub_judice', bloco, 1))
        self.campos.append(Campo(11, 86, 'filler_2', bloco, 8))
        self.campos.append(Campo(12, 94, 'serie_cadus', bloco, 1))
        self.campos.append(Campo(13, 95, 'chv_cadus', bloco, 10))
        self.campos.append(Campo(14, 105, 'tipo_ocorrencia', bloco, 1))
        self.campos.append(Campo(15, 106, 'filler_3', bloco, 9))


class RegistrosI220_subtipo02(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'filial_cnpj', bloco, 4))
        self.campos.append(Campo(4, 10, 'digito_documento', bloco, 2))
        self.campos.append(Campo(5, 12, 'data_inclusao', bloco, 8))
        self.campos.append(Campo(6, 20, 'hora_inclusao', bloco, 6))
        self.campos.append(Campo(7, 26, 'tipo_ocorrencia', bloco, 1))
        self.campos.append(Campo(8, 27, 'modalidade', bloco, 12))
        self.campos.append(Campo(9, 39, 'filler', bloco, 76))


class RegistrosI220_subtipo03(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'documento_credor', bloco, 14))
        self.campos.append(Campo(4, 20, 'nome', bloco, 70))
        self.campos.append(Campo(5, 90, 'filler_1', bloco, 16))
        self.campos.append(Campo(6, 106, 'tipo_ocorrencia', bloco, 1))
        self.campos.append(Campo(7, 107, 'cred_partic', bloco, 1))
        self.campos.append(Campo(8, 108, 'filler_2', bloco, 1))


class RegistrosA900(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'codigo', bloco, 6))
        self.campos.append(Campo(3, 10, 'mensagem_reduzida', bloco, 32))
        self.campos.append(Campo(4, 42, 'mensagem', bloco, 70))
        self.campos.append(Campo(5, 112, 'filler', bloco, 3))


class RegistrosT999(object):

    def __init__(self, bloco):
        self.campos = []
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'codigo', bloco, 3))
        self.campos.append(Campo(3, 7, 'mensagem', bloco, 70))
        self.campos.append(Campo(4, 7, 'filler', bloco, 38))