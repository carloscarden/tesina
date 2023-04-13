
class ProcesadoEnSujeto:
    """ Acá se guarda todo lo que se puede procesar de un sujeto"""
    i = 12345

    def __init__(self, lelsDePropiedad, lelsDeNivel):
        self.lelsDePropiedad=lelsDePropiedad 
        self.lelsDeNivel=  lelsDeNivel

    def nuevoLelDePropiedad(self, unLelDePropiedad):
        self.lelsDePropiedad.append(unLelDePropiedad)

    def nuevoLelDeNivel(self, unLelDeNivel):
        self.lelsDeNivel.append(unLelDeNivel)