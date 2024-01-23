from models.clasesDiagrama.tipoLinkDiagrama import TipoLinkDiagrama


class LinkDiagrama:
    """Representa las conexiones que tienen los objetos del diagrama, 
    de dónde parte y a dónde llega"""
    i = 12345

    def __init__(self, desde, hasta, tipoLink: TipoLinkDiagrama):
        self.desde = desde
        self.hasta= hasta
        self.tipoLink = tipoLink

    
    @classmethod
    def nuevoHecho(self, desde, hasta):
        return LinkDiagrama(desde, hasta,  TipoLinkDiagrama.ARCO_SIMPLE)


    @classmethod
    def nuevoLinkOpcional(self, desde, hasta):
        return LinkDiagrama(desde, hasta,  TipoLinkDiagrama.ARCO_OPCIONAL)


    @classmethod
    def nuevoLinkMultiple(self, desde, hasta):
        return LinkDiagrama(desde, hasta,  TipoLinkDiagrama.ARCO_MULTIPLE)