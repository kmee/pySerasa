# -*- coding: utf-8 -*-
from erros import BlocoInexistenteError

class Crednet(object):
    blocos = []


    def __getattr__(self, name):
        bloco = ([c for c in self.blocos if c.nome == name] or [None])[0]
        if not bloco:
            print BlocoInexistenteError().exibirErro(name)
        else:
            return bloco