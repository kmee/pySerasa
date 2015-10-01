# -*- coding: utf-8 -*-
from erros import CampoInexistenteError

class Registro(object):

    def __getitem__(self, key):
        campo = ([c for c in self.campos if c.indice == key or c.nome == key] or [None])[0]
        if not campo:
            raise CampoInexistenteError(self, key)
        return campo.get(self)


    def __getattr__(self, name):
        campo = ([c for c in self.campos.campos if c._nome == name] or [None])[0]
        if not campo:
            raise CampoInexistenteError(self, name)
        return campo._valor