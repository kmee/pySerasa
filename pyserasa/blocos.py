# -*- coding: utf-8 -*-


class RegistrosB49C(object):
    protocolo = None
    codEstacaoChamadora = None
    numDocumentoConsultado = None
    tipoPessoaConsultado = None
    baseCons = None
    modalidade = None
    vlrConsul = None
    centroCusto = None
    codificado = None
    qtdRegistros = None
    conversa = None
    funcao = None
    tipoConsulta = None
    atualiza = None
    ident_term = None
    rescli = None
    delts = None
    cobra = None
    passa = None
    consCollec = None
    localizador = None
    docCredor = None
    qtdCheque = None
    endTel = None
    qtdCho1 = None
    scoCho1 = None
    tarCho1 = None
    naoCobrarBureau = None
    autoPosit = None
    bureauViaSiteTransacion = None
    querTel9Digtos = None
    ctaCorrent = None
    dgCtacorr = None
    agencia = None
    alerta = None
    logon = None
    viaInternet = None
    resposta = None
    periodoCompro = None
    periodoEndereco = None
    backtest = None
    dtQuality = None
    prdOrigem = None
    trnOrigem = None
    consultante = None
    tpOr = None
    cnpjSoftware = None
    filler = None
    qtdCompr = None
    negativos = None
    cheque = None
    dataConsul = None
    horaConsult = None
    totalReg = None
    qtdReg1 = None
    codTab = None
    itemTsDados = None
    tsDados = None
    tsScore1 = None
    tsBp49 = None
    tsAutor = None
    itemTsAutor = None
    itemTsScor1 = None
    itemTsBp49 = None
    itemTsDados2 = None
    tsDados2 = None
    fase1 = None
    fase2 = None
    dbTabela = None
    codAut = None
    operid = None
    reciCompr = None
    reciPagto = None
    filler2 = None
    acessRechq = None
    temOcorrenciaRecheque = None
    reservado = None

    def get_nome_bloco(self):
        return "Bloco Protocolo"


class RegistrosP002(object):
    tipoReg = None
    cod1 = None
    chave1 = None
    cod2 = None
    chave2 = None
    cod3 = None
    chave3 = None
    cod4 = None
    chave4 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco P002"


class RegistrosN001(object):
    tipoReg = None
    subtipo = None
    tipoConsulta = None
    transacaoConsulta = None
    solGrandeVarejo = None
    idCheque = None
    agrupa = None
    consultaSintetica = None
    reservado = None
    anotacoesResumo = None
    chaveConsulta = None
    fantasia = None
    statusBanco = None
    filler = None
    trataTel = None

    def get_nome_bloco(self):
        return "Bloco N001"


class RegistrosN002_subtipo00(object):
    tipoReg = None
    subtipo = None
    banco = None
    agencia = None
    contaCorrente = None
    chequeInicial = None
    digitoChequeInicial = None
    chequeFinal = None
    digitoChequeFinal = None
    cmc7Inicial = None
    cmc7Final = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N002 subtipo 00"


class RegistrosN002_subtipo01(object):
    tipoReg = None
    subtipo = None
    valorCheque = None
    dataVencimentoCheque = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N002 subtipo 01"


class RegistrosN003(object):
    tipoReg = None
    subtipo = None
    ddd = None
    telefone = None
    cep = None
    uf = None
    featScor = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N003"


class RegistrosN200_subtipo00(object):
    tipoReg = None
    subtipo = None
    nomeRazao = None
    dataNascFundacao = None
    situacaoDoc = None
    dataSituacaoDoc = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N200 subtipo 00"


class RegistrosN200_subtipo01(object):
    tipoReg = None
    subtipo = None
    nomeMae = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N200 subtipo 01"


class RegistrosN210_subtipo00(object):
    tipoReg = None
    subtipo = None
    numMensagem = None
    totalMensagem = None
    tipoDoc = None
    numDoc = None
    motivo = None
    dataOcorrencia = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N210 subtipo 00"


class RegistrosN210_subtipo01(object):
    tipoReg = None
    subtipo = None
    ddd1 = None
    fone1 = None
    ddd2 = None
    fone2 = None
    ddd3 = None
    fone3 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N210 subtipo 01"


class RegistrosN210_subtipo99(object):
    tipoReg = None
    subtipo = None
    msgR210 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N210 subtipo 99"


class RegistrosN220(object):
    tipoReg = None
    subtipo = None
    msgNadaConsta = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N220"


class RegistrosN230_subtipo00(object):
    tipoReg = None
    subtipo = None
    dataOcorrencia = None
    modalidade = None
    avalista = None
    tipoMoeda = None
    valor = None
    contrato = None
    origem = None
    siglaEmbratel = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N230 subtipo 00"


class RegistrosN230_subtipo90(object):
    tipoReg = None
    subtipo = None
    totalOcorrencias = None
    dataOcorrenciaAntiga = None
    dataOcorrenciaRecente = None
    valorTotal = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N230 subtipo 90"


class RegistrosN230_subtipo99(object):
    tipoReg = None
    subtipo = None
    msgR230 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N230 subtipo 99"


class RegistrosN240_subtipo00(object):
    tipoReg = None
    subtipo = None
    dataOcorrencia = None
    modalidade = None
    avalista = None
    tipoMoeda = None
    valor = None
    contrato = None
    origem = None
    siglaEmbratel = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N240 subtipo 00"


class RegistrosN240_subtipo01(object):
    tipoReg = None
    subtipo = None
    subjudice = None
    msgSubjudice = None
    tipoAnotacao = None
    codCadus = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N240 subtipo 01"


class RegistrosN240_subtipo90(object):
    tipoReg = None
    subtipo = None
    totalOcorrencias = None
    dataOcorrenciaAntiga = None
    dataOcorrenciaRecente = None
    valorTotal = None
    tipoAnotacao = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N240 subtipo 90"


class RegistrosN240_subtipo99(object):
    tipoReg = None
    subtipo = None
    msgR240 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N240 subtipo 99"


class RegistrosN250_subtipo00(object):
    tipoReg = None
    subtipo = None
    dataOcorrencia = None
    tipoMoeda = None
    valor = None
    cartorio = None
    cidade = None
    uf = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N250 subtipo 00"


class RegistrosN250_subtipo01(object):
    tipoReg = None
    subtipo = None
    subjudice = None
    msgSubjudice = None
    tipoAnotacao = None
    codCadus = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N250 subtipo 01"


class RegistrosN250_subtipo90(object):
    tipoReg = None
    subtipo = None
    totalOcorrencias = None
    dataOcorrenciaAntiga = None
    dataOcorrenciaRecente = None
    moeda = None
    valorTotal = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N250 subtipo 90"


class RegistrosN250_subtipo99(object):
    tipoReg = None
    subtipo = None
    msgR250 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N250 subtipo 99"


class RegistrosN270_subtipo00(object):
    tipoReg = None
    subtipo = None
    dataOcorrencia = None
    cheque = None
    alinea = None
    quantidade = None
    valor = None
    numBanco = None
    nomeBanco = None
    agencia = None
    cidade = None
    uf = None
    codCadus = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N270 subtipo 00"


class RegistrosN270_subtipo90(object):
    tipoReg = None
    subtipo = None
    totalOcorrencias = None
    dataOcorrenciaAntiga = None
    dataOcorrenciaRecente = None
    banco = None
    agencia = None
    nomeFantasiaBanco = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N270 subtipo 90"


class RegistrosN270_subtipo99(object):
    tipoReg = None
    subtipo = None
    msgR270 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N270 subtipo 99"


class RegistrosN440_subtipo00(object):
    tipoReg = None
    subtipo = None
    dataEmissaoPrimeiroChequeVista = None
    dataEmissaoUltimoChequeVista = None
    totalChequesUltimos15DiasPrazo = None
    totalChequesUltimos30DiasPrazo = None
    totalChequesUltimos60DiasPrazo = None
    totalChequesUltimos90DiasPrazo = None
    totalChequesPrazo = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N440 subtipo 00"


class RegistrosN440_subtipo01(object):
    tipoReg = None
    subtipo = None
    dataEmissaoPrimeiroChequeVista = None
    dataEmissaoUltimoChequeVista = None
    totalChequesUltimos15DiasPrazo = None
    totalChequesUltimos30DiasPrazo = None
    totalChequesUltimos60DiasPrazo = None
    totalChequesUltimos90DiasPrazo = None
    totalChequesPrazo = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N440 subtipo 01"


class RegistrosN440_subtipo02(object):
    tipoReg = None
    subtipo = None
    PrimeiroRecenteNomeEmpr = None
    PrimeiroRecenteData = None
    SegundoRecenteNomeEmpr = None
    SegundoRecenteData = None
    TericeiroRecenteNomeEmpr = None
    TericeiroRecenteData = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N440 subtipo 02"


class RegistrosN440_subtipo03(object):
    tipoReg = None
    subtipo = None
    qtdConsultaUltimos15Dias = None
    qtdConsultaUltimos30Dias = None
    qtdConsultaUltimos60Dias = None
    qtdConsultaUltimos90Dias = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N440 subtipo 03"


class RegistrosN440_subtipo99(object):
    tipoReg = None
    subtipo = None
    msgR440 = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco N440 subtipo 99"


class RegistrosT999(object):
    tipoReg = None
    codigo = None
    mensagem = None
    filler = None

    def get_nome_bloco(self):
        return "Bloco T999"
