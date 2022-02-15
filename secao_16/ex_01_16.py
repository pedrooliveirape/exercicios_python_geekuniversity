class Pessoa:

    def __init__(self, nome: str, idade: int, altura: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @property
    def altura(self) -> float:
        return self.__altura


pessoa = Pessoa('Pedro', 33, 1.73)
print(f'{pessoa.nome} tem {pessoa.idade} anos de idade e mede {pessoa.altura}')
