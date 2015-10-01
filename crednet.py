# -*- coding: utf-8 -*-

class Crednet(object):
    blocos = []


    def __getattr__(self, name):
        bloco = ([c for c in self.blocos if c.nome == name] or [None])[0]
        # if not campo:
        #     raise CampoInexistenteError(self, name)
        return bloco