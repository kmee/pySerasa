# -*- coding: utf-8 -*-

from blocos import RegistrosB49C
# from blocos import RegistrosP002
# from blocos import RegistrosN001
# from blocos import RegistrosN002_subtipo00
# from blocos import RegistrosN002_subtipo01
# from blocos import RegistrosN003
# from blocos import RegistrosN200_subtipo00
# from blocos import RegistrosN200_subtipo01
# from blocos import RegistrosN210_subtipo00
# from blocos import RegistrosN210_subtipo01
# from blocos import RegistrosN210_subtipo99
# from blocos import RegistrosN220
# from blocos import RegistrosN230_subtipo00
# from blocos import RegistrosN230_subtipo90
# from blocos import RegistrosN230_subtipo99
# from blocos import RegistrosN240_subtipo00
# from blocos import RegistrosN240_subtipo01
# from blocos import RegistrosN240_subtipo90
# from blocos import RegistrosN240_subtipo99
# from blocos import RegistrosN250_subtipo00
# from blocos import RegistrosN250_subtipo01
# from blocos import RegistrosN250_subtipo90
# from blocos import RegistrosN250_subtipo99
# from blocos import RegistrosN270_subtipo00
# from blocos import RegistrosN270_subtipo90
# from blocos import RegistrosN270_subtipo99
# from blocos import RegistrosN440_subtipo00
# from blocos import RegistrosN440_subtipo01
# from blocos import RegistrosN440_subtipo02
# from blocos import RegistrosN440_subtipo03
# from blocos import RegistrosN440_subtipo99
# from blocos import RegistrosT999


class Crednet(object):
    _blocos = []

    def getString(self):
        dicionario = []

        for bloco in self._blocos:
            dicionario.append(bloco.__dict__)

        for pos in dicionario:
            #print pos
            for att in pos:
                    print (att, ':', pos[att])

            print "\n"