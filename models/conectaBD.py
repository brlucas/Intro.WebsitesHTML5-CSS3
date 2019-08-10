from sqlite3 import connect 

class ConexaoBancoDeDados:

    def __init__(self):
        self._conexao = connect("../db/banco.db")
        self._cursor = self._conexao.cursor()
        self.executaSql = self._cursor.execute
        self.confirmaAcao = self._conexao.commit

    def __del__(self):
        self._conexao.close()
