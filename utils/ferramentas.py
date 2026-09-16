import time

class Cronometro:

    def iniciar(self):
        self.inicio = time.perf_counter()
        
    def parar(self):
        self.tempo = time.perf_counter() - self.inicio
        return self.tempo  