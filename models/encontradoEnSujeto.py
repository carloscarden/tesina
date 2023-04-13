
class EncontradoEnSujeto:
    """ Guarda lo que pude encontrar en el notion de un sujeto """
    i = 12345

    def __init__(self, objectsSimple, nounChunks, pluralChunks):
        self.objectsSimple=objectsSimple 
        self.nounChunks=  nounChunks
        self.pluralChunks = pluralChunks

    def nuevoNounChunk(self, noun_chunk):
        self.nounChunks.append(noun_chunk)    

    def nuevoObjetoSimple(self, objectSimple):
        self.objectsSimple.append(objectSimple)    

    def nuevoPlural(self, nuevoPlural):
        self.pluralChunks.append(nuevoPlural)    