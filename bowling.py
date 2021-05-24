#Escribir una clase que se llame Juego que tenga
#–Tirar (int pinos) se llama cada vez que el jugador hace un tiro.  El argumento es la cantidad de pinos que el jugador derribo.
#–int Score() se llama solo al final del juego. Devuelve el score total.

class Juego:

    scoreAcum = 0
    tiroAnterior = 0
    isSpare = False
    isStrike = False
    isDoubleStrike = False
    tiroStrike = 0
    tirosRestantes = 20
    isTiroExtra = False
    tiroDelTurno = 1

    def tirar(self, pinos):

        if self.tirosRestantes <= 0 and (self.isStrike or self.isSpare):
            self.isTiroExtra = True

        if not self.isTiroExtra:
            self.scoreAcum += pinos
            self.tirosRestantes -= 1

        if self.isSpare:
            self.scoreAcum += pinos
            self.isSpare = False

        if self.isStrike:
            if self.tiroStrike <= 0:
                self.tiroStrike = 0
                self.isStrike = False
            else:
                self.scoreAcum += pinos
                self.tiroStrike -= 1

        if self.isDoubleStrike:
            self.scoreAcum += pinos
            self.isDoubleStrike = False

        if pinos + self.tiroAnterior == 10 and self.tiroAnterior != 0 and self.tiroDelTurno == 2:   
            self.isSpare = True

        if self.tiroDelTurno == 1:
            self.tiroDelTurno = 2
        else:
            self.tiroDelTurno = 1

        if pinos == 10:   
            if self.isStrike and not self.isTiroExtra and self.tiroStrike > 0:
                self.isDoubleStrike = True
            self.isStrike = True
            self.tirosRestantes -= 1
            self.tiroDelTurno = 1
            if not self.isTiroExtra:
                self.tiroStrike = 2

        self.tiroAnterior = pinos

    def score(self):
        return self.scoreAcum