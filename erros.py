# -*- coding: utf-8 -*-


class CampoInexistenteError(object):

    def exibirErro(self, name):
        return 'Este campo ' + name + ' não existe neste bloco de registros!'

class BlocoInexistenteError(object):

    def exibirErro(self, name):
        return 'Este bloco ' + name + ' não existe neste arquivo!'