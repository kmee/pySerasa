# -*- coding: utf-8 -*-
from registrosDados import *
from bloco import Bloco


class pendenciasInternas(Bloco):

    def __init__(self):
        self.blocos = []
        self.nome_bloco = False
        self.nome = "pendenciasInternas"


class pendenciasFinanceiras(Bloco):

    def __init__(self):
        self.blocos = []
        self.nome_bloco = False
        self.nome = "pendenciasFinanceiras"


class protestosEstados(Bloco):

    def __init__(self):
        self.blocos = []
        self.nome_bloco = False
        self.nome = "protestosEstados"


class chequesSemFundos(Bloco):

    def __init__(self):
        self.blocos = []
        self.nome_bloco = False
        self.nome = "chequesSemFundos"


class blocoB49C(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros do Protocolo"
        self.nome = nome
        self.campos = RegistrosB49C(bloco)


class blocoP002(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosP002(bloco)


class blocoN001(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN001(bloco)


class blocoN002_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN002_subtipo00(bloco)

class blocoN002_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN002_subtipo01(bloco)


class blocoN003(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registros adicionais ao Protocolo"
        self.nome = nome
        self.campos = RegistrosN003(bloco)


class blocoN200_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Bloco de informações do Confirmei"
        self.nome = nome
        self.campos = RegistrosN200_subtipo00(bloco)


class blocoN200_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Bloco de informações do Confirmei"
        self.nome = nome
        self.campos = RegistrosN200_subtipo01(bloco)


class blocoN210_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Alerta de Documentos Roubados"
        self.nome = nome
        self.campos = RegistrosN210_subtipo00(bloco)


class blocoN210_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Alerta de Documentos Roubados"
        self.nome = nome
        self.campos = RegistrosN210_subtipo01(bloco)


class blocoN210_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Alerta de Documentos Roubados"
        self.nome = nome
        self.campos = RegistrosN210_subtipo99(bloco)


class blocoN220(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Nada Consta"
        self.nome = nome
        self.campos = RegistrosN220(bloco)


class blocoN230_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendencias Internas"
        self.nome = nome
        self.campos = RegistrosN230_subtipo00(bloco)


class blocoN230_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendencias Internas"
        self.nome = nome
        self.campos = RegistrosN230_subtipo90(bloco)


class blocoN230_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendencias Internas"
        self.nome = nome
        self.campos = RegistrosN230_subtipo99(bloco)


class blocoN240_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo00(bloco)


class blocoN240_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo01(bloco)


class blocoN240_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo90(bloco)


class blocoN240_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Pendências Financeiras"
        self.nome = nome
        self.campos = RegistrosN240_subtipo99(bloco)


class blocoN250_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo00(bloco)


class blocoN250_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo01(bloco)


class blocoN250_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo90(bloco)


class blocoN250_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Protestos do Estado"
        self.nome = nome
        self.campos = RegistrosN250_subtipo99(bloco)


class blocoN270_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Cheques sem fundos - Bacen"
        self.nome = nome
        self.campos = RegistrosN270_subtipo00(bloco)


class blocoN270_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Cheques sem fundos - Bacen"
        self.nome = nome
        self.campos = RegistrosN270_subtipo90(bloco)


class blocoN270_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Cheques sem fundos - Bacen"
        self.nome = nome
        self.campos = RegistrosN270_subtipo99(bloco)


class blocoN300_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Recheque Online"
        self.nome = nome
        self.campos = RegistrosN300_subtipo00(bloco)


class blocoN300_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Recheque Online"
        self.nome = nome
        self.campos = RegistrosN300_subtipo01(bloco)


class blocoN300_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Recheque Online"
        self.nome = nome
        self.campos = RegistrosN300_subtipo99(bloco)


class blocoN310_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Recheque"
        self.nome = nome
        self.campos = RegistrosN310_subtipo00(bloco)


class blocoN310_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Recheque"
        self.nome = nome
        self.campos = RegistrosN310_subtipo99(bloco)


class blocoN320_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Contumácia"
        self.nome = nome
        self.campos = RegistrosN320_subtipo00(bloco)


class blocoN320_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Contumácia"
        self.nome = nome
        self.campos = RegistrosN320_subtipo90(bloco)


class blocoN320_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Contumácia"
        self.nome = nome
        self.campos = RegistrosN320_subtipo99(bloco)


class blocoN330_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Histórico do Cheque - Feature REAC"
        self.nome = nome
        self.campos = RegistrosN330_subtipo00(bloco)


class blocoN330_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Histórico do Cheque - Feature REAC"
        self.nome = nome
        self.campos = RegistrosN330_subtipo01(bloco)


class blocoN330_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Histórico do Cheque - Feature REAC"
        self.nome = nome
        self.campos = RegistrosN330_subtipo02(bloco)


class blocoN330_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Histórico do Cheque - Feature REAC"
        self.nome = nome
        self.campos = RegistrosN330_subtipo99(bloco)


class blocoN400_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço de Agência Bancária"
        self.nome = nome
        self.campos = RegistrosN400_subtipo00(bloco)


class blocoN400_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço de Agência Bancária"
        self.nome = nome
        self.campos = RegistrosN400_subtipo01(bloco)


class blocoN400_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço de Agência Bancária"
        self.nome = nome
        self.campos = RegistrosN400_subtipo99(bloco)


class blocoN410_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do CEP"
        self.nome = nome
        self.campos = RegistrosN410_subtipo00(bloco)


class blocoN410_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do CEP"
        self.nome = nome
        self.campos = RegistrosN410_subtipo01(bloco)


class blocoN410_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do CEP"
        self.nome = nome
        self.campos = RegistrosN410_subtipo99(bloco)


class blocoN420_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do Telefone(Teleconfirma)"
        self.nome = nome
        self.campos = RegistrosN420_subtipo00(bloco)


class blocoN420_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do Telefone(Teleconfirma)"
        self.nome = nome
        self.campos = RegistrosN420_subtipo01(bloco)


class blocoN420_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do Telefone(Teleconfirma)"
        self.nome = nome
        self.campos = RegistrosN420_subtipo02(bloco)


class blocoN420_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Endereço do Telefone(Teleconfirma)"
        self.nome = nome
        self.campos = RegistrosN420_subtipo99(bloco)


class blocoN430_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Últimos telefones consultados"
        self.nome = nome
        self.campos = RegistrosN430_subtipo00(bloco)


class blocoN430_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Últimos telefones consultados"
        self.nome = nome
        self.campos = RegistrosN430_subtipo99(bloco)

class blocoN440_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo00(bloco)


class blocoN440_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo01(bloco)


class blocoN440_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo02(bloco)


class blocoN440_subtipo03(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo03(bloco)


class blocoN440_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Consultaas"
        self.nome = nome
        self.campos = RegistrosN440_subtipo99(bloco)


class blocoN460_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Ações Judiciais"
        self.nome = nome
        self.campos = RegistrosN460_subtipo00(bloco)


class blocoN460_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Ações Judiciais"
        self.nome = nome
        self.campos = RegistrosN460_subtipo01(bloco)


class blocoN460_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Ações Judiciais"
        self.nome = nome
        self.campos = RegistrosN460_subtipo02(bloco)


class blocoN460_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Ações Judiciais"
        self.nome = nome
        self.campos = RegistrosN460_subtipo90(bloco)


class blocoN460_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Ações Judiciais"
        self.nome = nome
        self.campos = RegistrosN460_subtipo99(bloco)


class blocoN470_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Falências / Concordatas"
        self.nome = nome
        self.campos = RegistrosN470_subtipo00(bloco)


class blocoN470_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Falências / Concordatas"
        self.nome = nome
        self.campos = RegistrosN470_subtipo90(bloco)


class blocoN470_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Falências / Concordatas"
        self.nome = nome
        self.campos = RegistrosN470_subtipo99(bloco)


class blocoN480_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Participação em Insucesso Empresarial"
        self.nome = nome
        self.campos = RegistrosN480_subtipo00(bloco)


class blocoN480_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Participação em Insucesso Empresarial"
        self.nome = nome
        self.campos = RegistrosN480_subtipo01(bloco)


class blocoN480_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Participação em Insucesso Empresarial"
        self.nome = nome
        self.campos = RegistrosN480_subtipo90(bloco)


class blocoN480_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Participação em Insucesso Empresarial"
        self.nome = nome
        self.campos = RegistrosN480_subtipo99(bloco)


class blocoN500_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Score"
        self.nome = nome
        self.campos = RegistrosN500_subtipo00(bloco)


class blocoN505_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Score"
        self.nome = nome
        self.campos = RegistrosN505_subtipo00(bloco)


class blocoN505_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Score"
        self.nome = nome
        self.campos = RegistrosN505_subtipo01(bloco)


class blocoN505_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Score"
        self.nome = nome
        self.campos = RegistrosN505_subtipo99(bloco)


class blocoN600_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Gestão de Crédito por Cheques"
        self.nome = nome
        self.campos = RegistrosN600_subtipo00(bloco)


class blocoN600_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Gestão de Crédito por Cheques"
        self.nome = nome
        self.campos = RegistrosN600_subtipo01(bloco)


class blocoN600_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Gestão de Crédito por Cheques"
        self.nome = nome
        self.campos = RegistrosN600_subtipo02(bloco)


class blocoN600_subtipo03(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Gestão de Crédito por Cheques"
        self.nome = nome
        self.campos = RegistrosN600_subtipo03(bloco)


class blocoN600_subtipo04(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Gestão de Crédito por Cheques"
        self.nome = nome
        self.campos = RegistrosN600_subtipo04(bloco)


class blocoN600_subtipo05(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Gestão de Crédito por Cheques"
        self.nome = nome
        self.campos = RegistrosN600_subtipo05(bloco)


class blocoN610_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Concentre Scoring PJ"
        self.nome = nome
        self.campos = RegistrosN610_subtipo00(bloco)


class blocoN610_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Concentre Scoring PJ"
        self.nome = nome
        self.campos = RegistrosN610_subtipo99(bloco)


class blocoN620_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Limite de Crédito PJ"
        self.nome = nome
        self.campos = RegistrosN620_subtipo00(bloco)


class blocoN620_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Limite de Crédito PJ"
        self.nome = nome
        self.campos = RegistrosN620_subtipo90(bloco)


class blocoN620_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Limite de Crédito PJ"
        self.nome = nome
        self.campos = RegistrosN620_subtipo99(bloco)


class blocoN630_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "AlertScoring PJ"
        self.nome = nome
        self.campos = RegistrosN630_subtipo00(bloco)


class blocoN630_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "AlertScoring PJ"
        self.nome = nome
        self.campos = RegistrosN630_subtipo99(bloco)


class blocoN640_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Faturamento Presumido PJ"
        self.nome = nome
        self.campos = RegistrosN640_subtipo00(bloco)


class blocoN640_subtipo90(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Faturamento Presumido PJ"
        self.nome = nome
        self.campos = RegistrosN640_subtipo90(bloco)


class blocoN640_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Faturamento Presumido PJ"
        self.nome = nome
        self.campos = RegistrosN640_subtipo99(bloco)


class blocoN650_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Localizador de Endereço PJ"
        self.nome = nome
        self.campos = RegistrosN650_subtipo00(bloco)


class blocoN650_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Localizador de Endereço PJ"
        self.nome = nome
        self.campos = RegistrosN650_subtipo01(bloco)


class blocoN650_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Localizador de Endereço PJ"
        self.nome = nome
        self.campos = RegistrosN650_subtipo02(bloco)


class blocoN650_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Localizador de Endereço PJ"
        self.nome = nome
        self.campos = RegistrosN650_subtipo99(bloco)


class blocoN660_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Renda Presumida PF"
        self.nome = nome
        self.campos = RegistrosN660_subtipo00(bloco)


class blocoN660_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Renda Presumida PF"
        self.nome = nome
        self.campos = RegistrosN660_subtipo99(bloco)


class blocoN670_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Indicador de Operacionalidade PJ"
        self.nome = nome
        self.campos = RegistrosN670_subtipo00(bloco)


class blocoN670_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Indicador de Operacionalidade PJ"
        self.nome = nome
        self.campos = RegistrosN670_subtipo99(bloco)


class blocoN680_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Indice Relacionamento Mercado"
        self.nome = nome
        self.campos = RegistrosN680_subtipo00(bloco)


class blocoN680_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Indice Relacionamento Mercado"
        self.nome = nome
        self.campos = RegistrosN680_subtipo99(bloco)


class blocoN690_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Participação Societária"
        self.nome = nome
        self.campos = RegistrosN690_subtipo00(bloco)


class blocoN690_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Participação Societária"
        self.nome = nome
        self.campos = RegistrosN690_subtipo99(bloco)


class blocoN700_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Sócios e Acionistas"
        self.nome = nome
        self.campos = RegistrosN700_subtipo00(bloco)


class blocoN700_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = u"Sócios e Acionistas"
        self.nome = nome
        self.campos = RegistrosN700_subtipo99(bloco)


class blocoN705_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Administradores"
        self.nome = nome
        self.campos = RegistrosN705_subtipo00(bloco)


class blocoN705_subtipo99(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Administradores"
        self.nome = nome
        self.campos = RegistrosN705_subtipo99(bloco)


class blocoI001_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Registro de Pedido"
        self.nome = nome
        self.campos = RegistrosI001_subtipo00(bloco)


class blocoI105(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Grafias"
        self.nome = nome
        self.campos = RegistrosI001_subtipo00(bloco)


class blocoI110_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Resumo de Protestos"
        self.nome = nome
        self.campos = RegistrosI001_subtipo00(bloco)


class blocoI110_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Detalhe de Protestos"
        self.nome = nome
        self.campos = RegistrosI110_subtipo01(bloco)


class blocoI220_subtipo00(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Resumo de PEFIN"
        self.nome = nome
        self.campos = RegistrosI220_subtipo00(bloco)


class blocoI220_subtipo01(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Detalhe de PEFIN"
        self.nome = nome
        self.campos = RegistrosI220_subtipo01(bloco)


class blocoI220_subtipo02(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Detalhe de PEFIN 02"
        self.nome = nome
        self.campos = RegistrosI220_subtipo02(bloco)


class blocoI220_subtipo03(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Detalhe de PEFIN - Credor"
        self.nome = nome
        self.campos = RegistrosI220_subtipo03(bloco)


class blocoA900(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Mensagens Informativas"
        self.nome = nome
        self.campos = RegistrosA900(bloco)


class blocoT999(Bloco):

    def __init__(self, nome, bloco):
        self.nome_bloco = "Trailler - Fim dos dados"
        self.nome = nome
        self.campos = RegistrosT999(bloco)
