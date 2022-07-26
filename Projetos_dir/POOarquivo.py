class Pessoa:
    from datetime import date

    ano_atual = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return self.ano_atual - self.idade
