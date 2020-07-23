class CasillaVotacion:
    def __init__(self, indentificador,pais):
        self._identificador = indentificador
        self._pais = pais
        self._region = None
    @property
    def region(self):
        return self._region
    @region.setter
    def region(self,reg):
        if reg in self._pais:
            self._region = reg
        else:
            raise ValueError('La region no es valida')

casilla = CasillaVotacion(123,['Bogota','Medellin'])
print(casilla.region)
casilla.region = 'China'
print(casilla.region)
