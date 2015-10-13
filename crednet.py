# -*- coding: utf-8 -*-
from erros import BlocoInexistenteError
from blocosDados import pendenciasInternas
from blocosDados import pendenciasFinanceiras
from blocosDados import protestosEstados
from blocosDados import chequesSemFundos


class Crednet(object):
    blocos = []

    def __init__(self):
        self.blocos.append(pendenciasInternas())
        self.blocos.append(pendenciasFinanceiras())
        self.blocos.append(protestosEstados())
        self.blocos.append(chequesSemFundos())


    def __getattr__(self, name):
        bloco = ([c for c in self.blocos if c.nome == name] or [None])[0]
        if not bloco:
            print BlocoInexistenteError().exibirErro(name)
        else:
            if bloco.nome == 'pendenciasInternas':
                print "Pendencias Internas\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print campos._nome,
                        print ": ",
                        print campos._valor

                    print " "
            if bloco.nome == 'pendenciasFinanceiras':
                print "Pendencias Financeiras\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print campos._nome,
                        print ": ",
                        print campos._valor

                    print " "
            if bloco.nome == 'protestosEstados':
                print "Protestos do Estado\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print campos._nome,
                        print ": ",
                        print campos._valor

                    print " "
            if bloco.nome == 'chequesSemFundos':
                print "Cheques Sem Fundos\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print campos._nome,
                        print ": ",
                        print campos._valor

                    print " "
            else:
                return bloco


    def getString(self):
        for bloco in self.blocos:
            print "Bloco :" + bloco.nome
            for campo in bloco.campos.campos:
                print campo._nome + " : " + campo._valor

            print ""