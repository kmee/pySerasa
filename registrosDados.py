# -*- coding: utf-8 -*-

from campos import Campo


class RegistrosB49C(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'Protocolo', bloco, 4))
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
        self.campos.append(Campo(52, 195, 'dataConsul', bloco, 8))
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
    campos = []

    def __init__(self, bloco):
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
    campos = []

    def __init__(self, bloco):
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
    campos = []

    def __init__(self, bloco):
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
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'valorCheque', bloco, 15))
        self.campos.append(Campo(4, 21, 'dataVencimentoCheque', bloco, 8))
        self.campos.append(Campo(5, 29, 'filler', bloco, 86))


class RegistrosN003(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 6))
        self.campos.append(Campo(3, 6, 'ddd', bloco, 3))
        self.campos.append(Campo(4, 9, 'telefone', bloco, 8))
        self.campos.append(Campo(5, 18, 'cep', bloco, 9))
        self.campos.append(Campo(6, 27, 'uf', bloco, 4))
        self.campos.append(Campo(7, 29, 'featScor', bloco, 4))
        self.campos.append(Campo(8, 109, 'filler', bloco, 6))


class RegistrosN200_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nomeRazao', bloco, 70))
        self.campos.append(Campo(4, 76, 'dataNascFundacao', bloco, 8))
        self.campos.append(Campo(5, 84, 'situacaoDoc', bloco, 2))
        self.campos.append(Campo(6, 86, 'dataSituacaoDoc', bloco, 8))
        self.campos.append(Campo(7, 94, 'filler', bloco, 21))


class RegistrosN200_subtipo01(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'nomeMae', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN210_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'numMensagem', bloco, 2))
        self.campos.append(Campo(4, 8, 'totalMensagem', bloco, 2))
        self.campos.append(Campo(5, 10, 'tipoDoc', bloco, 6))
        self.campos.append(Campo(6, 16, 'numDoc', bloco, 20))
        self.campos.append(Campo(7, 36, 'motivo', bloco, 4))
        self.campos.append(Campo(8, 40, 'dataOcorrencia', bloco, 10))
        self.campos.append(Campo(9, 50, 'filler', bloco, 59))


class RegistrosN210_subtipo01(object):
    campos = []

    def __init__(self, bloco):
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
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR210', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN220(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgNadaConsta', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN230_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'modalidade', bloco, 30))
        self.campos.append(Campo(5, 44, 'avalista', bloco, 1))
        self.campos.append(Campo(6, 45, 'tipoMoeda', bloco, 3))
        self.campos.append(Campo(7, 48, 'valor', bloco, 15))
        self.campos.append(Campo(8, 63, 'contrato', bloco, 16))
        self.campos.append(Campo(9, 79, 'origem', bloco, 30))
        self.campos.append(Campo(10, 109, 'siglaEmbratel', bloco, 4))
        self.campos.append(Campo(11, 113, 'filler', bloco, 2))


class RegistrosN230_subtipo90(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(Campo(4, 11, 'dataOcorrenciaAntiga', bloco, 6))
        self.campos.append(Campo(5, 17, 'dataOcorrenciaRecente', bloco, 6))
        self.campos.append(Campo(6, 23, 'valorTotal', bloco, 15))
        self.campos.append(Campo(7, 38, 'filler', bloco, 77))


class RegistrosN230_subtipo99(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR230', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN240_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'modalidade', bloco, 30))
        self.campos.append(Campo(5, 44, 'avalista', bloco, 1))
        self.campos.append(Campo(6, 45, 'tipoMoeda', bloco, 3))
        self.campos.append(Campo(7, 48, 'valor', bloco, 15))
        self.campos.append(Campo(8, 63, 'contrato', bloco, 16))
        self.campos.append(Campo(9, 79, 'origem', bloco, 30))
        self.campos.append(Campo(10, 109, 'siglaEmbratel', bloco, 4))
        self.campos.append(Campo(11, 113, 'filler', bloco, 2))


class RegistrosN240_subtipo01(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'subjudice', bloco, 1))
        self.campos.append(Campo(4, 7, 'msgSubjudice', bloco, 76))
        self.campos.append(Campo(5, 83, 'tipoAnotacao', bloco, 1))
        self.campos.append(Campo(6, 84, 'codCadus', bloco, 10))
        self.campos.append(Campo(7, 94, 'filler', bloco, 21))


class RegistrosN240_subtipo90(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(Campo(4, 11, 'dataOcorrenciaAntiga', bloco, 6))
        self.campos.append(Campo(5, 17, 'dataOcorrenciaRecente', bloco, 6))
        self.campos.append(Campo(6, 23, 'valorTotal', bloco, 15))
        self.campos.append(Campo(7, 38, 'tipoAnotacao', bloco, 1))
        self.campos.append(Campo(8, 39, 'filler', bloco, 16))


class RegistrosN240_subtipo99(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR240', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN250_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataOcorrencia', bloco, 8))
        self.campos.append(Campo(4, 14, 'tipoMoeda', bloco, 3))
        self.campos.append(Campo(5, 17, 'valor', bloco, 15))
        self.campos.append(Campo(6, 32, 'cartorio', bloco, 2))
        self.campos.append(Campo(7, 34, 'cidade', bloco, 30))
        self.campos.append(Campo(8, 64, 'uf', bloco, 2))


class RegistrosN250_subtipo01(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'subjudice', bloco, 1))
        self.campos.append(Campo(4, 7, 'msgSubjudice', bloco, 76))
        self.campos.append(Campo(5, 83, 'tipoAnotacao', bloco, 1))
        self.campos.append(Campo(6, 84, 'codCadus', bloco, 10))
        self.campos.append(Campo(7, 94, 'filler', bloco, 21))


class RegistrosN250_subtipo90(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(Campo(4, 11, 'dataOcorrenciaAntiga', bloco, 6))
        self.campos.append(Campo(5, 17, 'dataOcorrenciaRecente', bloco, 6))
        self.campos.append(Campo(6, 23, 'moeda', bloco, 3))
        self.campos.append(Campo(7, 26, 'valorTotal', bloco, 15))
        self.campos.append(Campo(8, 41, 'filler', bloco, 74))


class RegistrosN250_subtipo99(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR250', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN270_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataOcorrencia', bloco, 8))
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
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'totalOcorrencias', bloco, 5))
        self.campos.append(Campo(4, 11, 'dataOcorrenciaAntiga', bloco, 8))
        self.campos.append(Campo(5, 19, 'dataOcorrenciaRecente', bloco, 8))
        self.campos.append(Campo(6, 27, 'banco', bloco, 3))
        self.campos.append(Campo(7, 30, 'agencia', bloco, 4))
        self.campos.append(Campo(8, 34, 'nomeFantasiaBanco', bloco, 12))
        self.campos.append(Campo(9, 46, 'filler', bloco, 69))


class RegistrosN270_subtipo99(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR270', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosN440_subtipo00(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataEmissaoPrimeiroChequeVista', bloco, 4))
        self.campos.append(Campo(4, 10, 'dataEmissaoUltimoChequeVista', bloco, 4))
        self.campos.append(Campo(5, 14, 'totalChequesUltimos15DiasPrazo', bloco, 3))
        self.campos.append(Campo(6, 17, 'totalChequesUltimos30DiasPrazo', bloco, 2))
        self.campos.append(Campo(7, 19, 'totalChequesUltimos60DiasPrazo', bloco, 2))
        self.campos.append(Campo(8, 21, 'totalChequesUltimos90DiasPrazo', bloco, 2))
        self.campos.append(Campo(9, 23, 'totalChequesPrazo', bloco, 3))
        self.campos.append(Campo(10, 26, 'filler', bloco, 89))


class RegistrosN440_subtipo01(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'dataEmissaoPrimeiroChequeVista', bloco, 4))
        self.campos.append(Campo(4, 10, 'dataEmissaoUltimoChequeVista', bloco, 4))
        self.campos.append(Campo(5, 14, 'totalChequesUltimos15DiasPrazo', bloco, 3))
        self.campos.append(Campo(6, 17, 'totalChequesUltimos30DiasPrazo', bloco, 2))
        self.campos.append(Campo(7, 19, 'totalChequesUltimos60DiasPrazo', bloco, 2))
        self.campos.append(Campo(8, 21, 'totalChequesUltimos90DiasPrazo', bloco, 2))
        self.campos.append(Campo(9, 23, 'totalChequesPrazo', bloco, 3))
        self.campos.append(Campo(10, 26, 'filler', bloco, 89))


class RegistrosN440_subtipo02(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'PrimeiroRecenteNomeEmpr', bloco, 25))
        self.campos.append(Campo(4, 31, 'PrimeiroRecenteData', bloco, 4))
        self.campos.append(Campo(5, 35, 'SegundoRecenteNomeEmpr', bloco, 25))
        self.campos.append(Campo(6, 60, 'SegundoRecenteData', bloco, 4))
        self.campos.append(Campo(7, 64, 'TericeiroRecenteNomeEmpr', bloco, 25))
        self.campos.append(Campo(8, 89, 'TericeiroRecenteData', bloco, 4))
        self.campos.append(Campo(9, 93, 'filler', bloco, 22))


class RegistrosN440_subtipo03(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'qtdConsultaUltimos15Dias', bloco, 3))
        self.campos.append(Campo(4, 9, 'qtdConsultaUltimos30Dias', bloco, 3))
        self.campos.append(Campo(5, 12, 'qtdConsultaUltimos60Dias', bloco, 3))
        self.campos.append(Campo(6, 15, 'qtdConsultaUltimos90Dias', bloco, 33))
        self.campos.append(Campo(7, 18, 'filler', bloco, 97))


class RegistrosN440_subtipo99(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'subtipo', bloco, 2))
        self.campos.append(Campo(3, 6, 'msgR440', bloco, 40))
        self.campos.append(Campo(4, 46, 'filler', bloco, 69))


class RegistrosT999(object):
    campos = []

    def __init__(self, bloco):
        self.campos.append(Campo(1, 0, 'tipoReg', bloco, 4))
        self.campos.append(Campo(2, 4, 'codigo', bloco, 3))
        self.campos.append(Campo(3, 7, 'mensagem', bloco, 70))
        self.campos.append(Campo(4, 7, 'filler', bloco, 38))







