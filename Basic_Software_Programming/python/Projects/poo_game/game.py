import random
#personagem: classe mãe
#heroi: controlado pelo usuário
#inimigo: adversário do usuário


class Personagem: #classe mãe
    def __init__(self, nome, vida, nivel):
        self.__nome = nome #encapsulamento
        self.__vida = vida
        self.__nivel = nivel

#encapsulamento - recuperar os valores pelo get dos valores dos atributos 
    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida:{self.get_vida()} \nNivel: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo): 
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) #o dano baseado no nível, usando a 
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    

#Instâncias da classe mãe (herança) 

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade): #precisa receber os parametros
        super().__init__(nome, vida, nivel) #precisa usar/executar aqui os parâmetros mencionados lá em cima
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidades: {self.get_habilidade()}\n" #Polomorfismo (herdou da mãe e foi reinplementado no exibir detalhes)
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)#dano aumentado
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo): #precisa receber os parametros
        super().__init__(nome, vida, nivel) #precisa usar/executar aqui os parâmetros mencionados lá em cima
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n" #Polomorfismo (herdou da mãe e foi reinplementado no exibir detalhes)
    

class Jogo:    
    """Classe orquestradora do jogo"""
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Heroi", vida= 100, nivel =5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida= 80, nivel =5, tipo="voador")

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""

        print("Iniciando Batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha(1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2': #habilitando o ataque especial por parte do heroi no morcego(inimigo)
                self.heroi.ataque_especial(self.inimigo)
            else: 
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                #inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)


        if self.heroi.get_vida() > 0:
            print("Parabéns, você venceu a batalha!")
        else: 
            print("\nVocê foi derrotado!")

#Criar instância do jogo e iniciar batalha

jogo = Jogo() #iniciar o jogo, criando os personagens
jogo.iniciar_batalha() #iniciar batalhas em turnos