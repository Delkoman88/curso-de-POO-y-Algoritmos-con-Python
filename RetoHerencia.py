class Planta:

    def __init__(self, nombrecomun, iluminacion, uso):
        self.nombrecomun = nombrecomun
        self.iluminacion = iluminacion
        self.uso = uso

    def infoplanta(self):
        print(f'La planta {self.nombrecomun}, es de uso {self.uso} y crece mejor en {self.iluminacion}' )

class Culinaria(Planta):

    def __init__(self, nombrecomun, iluminacion, uso = 'culinario'):
        super().__init__(nombrecomun, iluminacion, uso)

class Medicinal(Planta):

    def __init__(self, nombrecomun, iluminacion, uso = 'medicinal'):
        super().__init__(nombrecomun, iluminacion, uso)

class Ornato(Planta):

    def __init__(self, nombrecomun, iluminacion, uso = 'ornato'):
        super().__init__(nombrecomun, iluminacion, uso)

if __name__ == '__main__':

    Albahaca = Culinaria('albahaca', 'sol')
    Romero = Medicinal('romero', 'sombra')
    Tulipan = Ornato('tulipan', 'sombra')

    Albahaca.infoplanta()
    Romero.infoplanta()
    Tulipan.infoplanta()
