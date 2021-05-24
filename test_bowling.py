#1.Testear un juego de perdedor, o sea, tira todos los tiros y nunca tumba un pino.
#2.Testear todos 1.
#3.Probar que al menos haya un Spare
#4.Probar que haya al menos un Strike
#5.Probar el juego perfecto.

import unittest
from bowling import Juego

class TestsBasicos(unittest.TestCase):

    def test_todos_0(self):
        bolos = Juego()
        for i in range(0,10,1):
            bolos.tirar(0)
            bolos.tirar(0)
        self.assertEqual(0,bolos.score())
        
    def test_todos_1(self):
        bolos = Juego()
        for i in range(0,10,1):
            bolos.tirar(1)
            bolos.tirar(1)
        self.assertEqual(20,bolos.score())

    def test_1_spare(self):
        bolos = Juego()
        bolos.tirar(4)
        bolos.tirar(6)
        for i in range(1,10,1):
            bolos.tirar(1)
            bolos.tirar(1) 
        self.assertEqual(29,bolos.score())

    def test_1_strike(self):
        bolos = Juego()
        for i in range(1,10,1):
            bolos.tirar(1)
            bolos.tirar(1)
        bolos.tirar(10)
        bolos.tirar(1)
        bolos.tirar(1)
        self.assertEqual(30,bolos.score())

    def test_todos_strikes(self):
        bolos = Juego()
        for i in range(0,12,1):
            bolos.tirar(10)
        self.assertEqual(300,bolos.score())

    def test_ejemplo_del_ppt_agiles(self):
        bolos = Juego()
        bolos.tirar(1)
        bolos.tirar(4)

        bolos.tirar(4)
        bolos.tirar(5)

        bolos.tirar(6)
        bolos.tirar(4)

        bolos.tirar(5)
        bolos.tirar(5)

        bolos.tirar(10)

        bolos.tirar(0)
        bolos.tirar(1)

        bolos.tirar(7)
        bolos.tirar(3)

        bolos.tirar(6)
        bolos.tirar(4)

        bolos.tirar(10)

        bolos.tirar(2)
        bolos.tirar(8)

        bolos.tirar(6)

        self.assertEqual(133,bolos.score())
