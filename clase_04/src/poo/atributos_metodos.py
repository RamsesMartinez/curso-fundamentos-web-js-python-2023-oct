class PaginaWeb:
    def __init__(self, titulo, contenido, url):
        self.titulo = titulo 
        self.contenido = contenido
        self.url = url 

    def mostrar_titulo(self):
        print("Título de la página web:", self.titulo)

    def mostrar_contenido(self):
        print("Contenido de la página web:")
        print(self.contenido)

    def cambiar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        print("Contenido actualizado!")

# Crear una instancia de la clase PaginaWeb
mi_pagina = PaginaWeb("Mi primera página", "Bienvenido a mi página web", "www.mipagina.com")

mi_pagina.mostrar_titulo()
mi_pagina.mostrar_contenido()

mi_pagina.cambiar_contenido("Nuevo contenido de mi página web")

mi_pagina.mostrar_contenido()
