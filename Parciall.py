#Miguel Ramos
#Biblioteca básica

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._isbn = isbn
        self._disponible = True

    def prestar(self):
        self._disponible = False

    def devolver(self):
        self._disponible = True

    def disponible(self):
        return self._disponible

    def isbn(self):
        return self._isbn


class Usuario:
    def __init__(self, nombre, id_u):
        self._nombre = nombre
        self._id = id_u
        self._libros = []

    def prestar(self, libro):
        self._libros.append(libro)

    def id(self):
        return self._id


class Biblioteca:
    CATEGORIAS = ["Ciencia", "Literatura", "Ingenieria"]

    def __init__(self):
        self._libros = []
        self._usuarios = []

    def registrar_libro(self):
        clave = input("Contraseña de administrador: ")
        if clave != "admin":
            print("Acceso denegado. Solo administradores pueden registrar libros.")
            return
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")
        isbn = input("ISBN: ")
        if categoria not in self.CATEGORIAS:
            print("Categoria no valida.")
            return
        self._libros.append(Libro(titulo, autor, categoria, isbn))
        print("Libro registrado.")

    def registrar_usuario(self):
        nombre = input("Nombre: ")
        id_u = input("ID: ")
        self._usuarios.append(Usuario(nombre, id_u))
        print("Usuario registrado.")

    def prestar_libro(self):
        id_u = input("ID usuario: ")
        isbn = input("ISBN libro: ")
        usuario = next((u for u in self._usuarios if u.id() == id_u), None)
        libro = next((l for l in self._libros if l.isbn() == isbn), None)
        if usuario and libro and libro.disponible():
            libro.prestar()
            usuario.prestar(libro)
            print("Libro prestado.")
        else:
            print("Error: usuario, libro no encontrado o no disponible.")

    def menu(self):
        while True:
            print("\n1. Registrar libro (admin)")
            print("2. Registrar usuario")
            print("3. Prestar libro")
            print("4. Salir")
            opcion = input("Opcion: ")
            if opcion == "1":
                self.registrar_libro()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                self.prestar_libro()
            elif opcion == "4":
                break
            else:
                print("Opcion invalida.")


if __name__ == "__main__":
    Biblioteca().menu()