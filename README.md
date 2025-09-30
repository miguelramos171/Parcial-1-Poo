# Simulador de Biblioteca – Parcial 1 POO  
Facultad de Ingeniería – Universidad Nacional de Colombia

## Requerimientos funcionales cumplidos

Requerimiento funcional                              Cumplido  
Registro de nuevos libros                            ✓  
Registro de nuevos usuarios                          ✓  
Mínimo 3 categorías de libros                        ✓  

> **Nota**: El registro de libros solo puede realizarse por un administrador (contraseña: `admin`).

## Descripción de las clases y métodos usados

El sistema está compuesto por tres clases:

- **Libro**:  
  Atributos: `_titulo`, `_autor`, `_categoria`, `_isbn`, `_disponible`.  
  Métodos: `prestar()`, `devolver()`, `disponible()`, `isbn()`.

- **Usuario**:  
  Atributos: `_nombre`, `_id`, `_libros` (lista de libros prestados).  
  Métodos: `prestar(libro)`, `id()`.

- **Biblioteca**:  
  Atributos: `_libros` (lista), `_usuarios` (lista), `CATEGORIAS` (lista fija).  
  Métodos:  
  - `registrar_libro()` → solicita contraseña de administrador.  
  - `registrar_usuario()` → crea un nuevo usuario.  
  - `prestar_libro()` → vincula un libro disponible con un usuario.  
  - `menu()` → muestra opciones en consola y gestiona la interacción.

## Justificación técnica de las decisiones de diseño

Se aplicó **encapsulamiento** usando el prefijo `_` en todos los atributos, lo que indica que son de uso interno y deben accederse únicamente mediante métodos públicos. Esto evita modificaciones accidentales del estado de los objetos.

La **interacción entre clases** se da en la clase `Biblioteca`, que actúa como coordinador:  
- Al prestar un libro, busca el `Usuario` y el `Libro` correspondientes.  
- Verifica su disponibilidad, actualiza el estado del libro y lo añade a la lista del usuario.

El control de acceso para registrar libros se implementó con una contraseña simple (`"admin"`) para cumplir con el requisito de perfil administrador.

