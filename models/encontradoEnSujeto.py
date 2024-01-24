
from spacy.tokens import Span


class EncontradoEnSujeto:
    """ Guarda lo que pude encontrar en el notion de un sujeto """
    i = 12345

    stop_words = ["its", "an", "a"]

    def __init__(self, objectsSimple, nounChunks, pluralChunks):
        self.objectsSimple=objectsSimple 
        self.nounChunks=  nounChunks
        self.pluralChunks = pluralChunks

    def nuevoNounChunk(self, noun_chunk):
        self.nounChunks.append(noun_chunk)    

    def nuevoObjetoSimple(self, objectSimple):
        self.objectsSimple.append(objectSimple)    


    def nuevoObjeto(self, noun_chunk: Span):
        # Crear lista de palabras a eliminar

        palabraPlural = list( filter( lambda nc: nc.tag_ in ["NNS", "NNPS"],noun_chunk))

        sinPreposiciones = [t for t in noun_chunk if t.text.lower() not in self.stop_words]
        if(len(sinPreposiciones) > 1):
            # palabras dobles
            self.nuevoNounChunk(sinPreposiciones)
            if(palabraPlural):
                self.pluralChunks.append(sinPreposiciones)
        else:
            self.nuevoObjetoSimple(sinPreposiciones[0])
            if(palabraPlural):
                self.pluralChunks.append(sinPreposiciones[0])

