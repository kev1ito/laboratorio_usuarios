from conexion import Conexion
from logger_base import log


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta metodo __exit__')
        if exc_val: #Si el valor de la excepción no es None se hace rollback de la conexión
            self._conexion.rollback()
            log.error(f'Ocurrio una excepción, se hace rollback: {exc_val} {exc_type} {exc_tb}')
        else:
            self._conexion.commit() #Se guardan los cambio sde los queries realizados
            log.debug('commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

