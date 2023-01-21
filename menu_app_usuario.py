from logger_base import log
from usuario import Usuario
from usuario_dao import UsuarioDAO

opcion = None
while opcion !=5:
    try:
        print('Opciones: ')
        print('1. Listar Usuario')
        print('2. Agregar Usuario')
        print('3. Actualizar Usuario')
        print('4. Eliminar Usuario')
        print('5. Salir')
        opcion = int(input('Escribe tu opción (1-5): '))

        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                print(usuario)
        elif opcion == 2:
            username = input('Username: ')
            password = input('Password: ')
            new_usuario = Usuario(username=username, password=password)
            usuario_nuevo = UsuarioDAO.insertar(new_usuario)
        elif opcion == 3:
            id_usuario = int(input('ID usuario: '))
            username = input('New username: ')
            password = input('New password: ')
            update_usuario = Usuario(id_usuario, username, password)
            usuario_actualizado = UsuarioDAO.actualizar(update_usuario)
        elif opcion == 4:
            id_usuario = int(input('ID usuario: '))
            delete_usuario = Usuario(id_usuario,)
            usuario_eliminado = UsuarioDAO.eliminar(delete_usuario)
    except Exception as e:
        log.error(f'Ocurrio un error durante la ejecución de la app {e}')
        opcion = None
else:
    log.debug('FIN DEL PROGRAMA...')