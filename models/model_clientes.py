from .conectaBD import ConexaoBancoDeDados
from json import dumps

class ModelCliente(ConexaoBancoDeDados):

    def __init__(self):
        super().__init__()

    def cadastroDeCliente(self, dadosDoServidor):
        try:
            sql = """insert into clientes ( nome_cliente, razao_social, celular, celular2, fixo, endereco, email)
                VALUES("{nome}", "{razaoSocial}", {celular}, {celular1}, {fixo}, "{endereco}", "{email}")""".format(
                    nome=dadosDoServidor['nome'],
                    razaoSocial=dadosDoServidor['razaoSocial'],
                    celular=dadosDoServidor['celular'],
                    celular1=dadosDoServidor['celular2'],
                    fixo=dadosDoServidor['fixo'], 
                    endereco=dadosDoServidor['endereco'],
                    email=dadosDoServidor['email'])

            self.executaSql(sql)
            self.confirmaAcao()
        
            return dumps({"resposta": "Cliente cadastrado com sucesso !"})
        
        except:

            return dumps({"resposta": "Problema para executar essa ação !"})

    
    def deletarCliente(self, id):
        try:
            sql = "delete from clientes WHERE id_clientes = {id}".format(id)
            self.executaSql(sql)
            self.confirmaAcao()
        
            return dumps({"resposta": "Cliente deletado com sucesso !"})

        except:
            return dumps({"resposta": "Problema para executar essa ação !"})


    def listarCliente(self, id):
        try:
            sql = "select * from clientes WHERE id_clientes = {id}".format(id)
            self.executaSql(sql)
            self.confirmaAcao()
        
            return dumps({"resposta": "Cliente deletado com sucesso !"})

        except:
            return dumps({"resposta": "Problema para executar essa ação !"})
    

    def atulizarCliente(self, dadosDoServidor):
        try:
            sql = """
            UPDATE clientes 
            set nome_cliente = {nome_cliente}" ,
            razao_social = "{razao_social}",
            celular = {celular},
            celular2 =  {celular2},
            fixo = {fixo},
            endereco = "{endereco}",
            email = "{email}"
            where id_clientes = {id_clientes}""".format(
                nome_cliente=dadosDoServidor['nome'],
                razao_social=dadosDoServidor['razaoSocial'],
                celular=dadosDoServidor['celular'],
                celular1=dadosDoServidor['celular1'],
                fixo=dadosDoServidor['fixo'], 
                endereco=dadosDoServidor['endereco'],
                email=dadosDoServidor['email'],
                id_clientes=dadosDoServidor['idCliente'])

            return dumps({"resposta": "Cliente atualizado com sucesso !"})

        except:
            return dumps({"resposta": "Problema para executar essa ação !"})