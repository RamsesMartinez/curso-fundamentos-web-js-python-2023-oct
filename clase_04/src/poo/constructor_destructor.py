class PaginaWeb:
    def __init__(self, titulo, url):
        self.titulo = titulo
        self.url = url
        print(f"Se creó la página {self.titulo} con URL {self.url}")

    def __del__(self):
        print(f"Se eliminó la página {self.titulo}")

mi_pagina = PaginaWeb("Mi primera página", "www.mipagina.com")
del mi_pagina
