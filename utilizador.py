class Utilizador:

    lista_utilizadores = []

    def add_user(self):
        Utilizador.lista_utilizadores.append(self)


    def __init__(self, handle, password, numero, nome_completo, descricao):
        self.numero = numero
        self.handle = handle
        self.password = password 
        self.nome_completo = nome_completo
        self.descricao = descricao
        Utilizador.add_user(self)

    def verfificar_user(handle, password):
        utilizador = ""
        for user in Utilizador.lista_utilizadores:
            if user.handle == handle and user.password == password:
                utilizador = user
        return False if not utilizador else True, utilizador 
       
            

