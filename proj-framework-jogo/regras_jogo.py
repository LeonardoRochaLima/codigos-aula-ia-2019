from abc import ABC
import turtle

#Setando o Mapa do Labirinto
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Labirinto")
wn.setup(700, 700)

#Registrando os GIFS
turtle.register_shape("person.gif")
turtle.register_shape("wall.gif")
turtle.register_shape("finish.gif")

class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Treasure(turtle.Turtle):
    def __int__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Checkpoint (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("finish.gif")
        self.color("red")
        self.penup()
        self.speed(0)

#Criando um Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("person.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

class RegrasJogo(ABC):
    """ Interface mínima para implementar um jogo interativo e modular. Não
    tente instanciar objetos dessa classe, ela deve ser herdada e seus métodos
    abstratos sobrecarregados.
    """

    #@abstractmethod
    def registrarAgenteJogador():
        """ Cria ou recupera id de um elemento de jogo agente.
        """
        class Player(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape("person.gif")
                self.color("blue")
                self.penup()
                self.speed(0)
        return
    
    #@abstractmethod
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        return

    #@abstractmethod
    def gerarCampoVisao(self, idAgente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        return

    #@abstractmethod
    def registrarProximaAcao(self, id_jogador, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        return
    
    #@abstractmethod
    def atualizarEstado(diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        return

levels = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XP   X                X",
    "XXXX X		XXXX X  X     X",
    "X    XXXXXXX    X  X  X",
    "XXXX       X  XXX     X",
    "X  X  X    X  X   XXXXX",
    "X  XXXX   XX  X X     X",
    "X  X    X   X X X     X",
    "X  X    XXX X X XXX   X",
    "X      XX          X  X",
	  "XXXX X  X   XXXXX  X  X",
	  "X    X    X           X",
    "XXXXXXXXXXXXXXXXXXXXCXX"
]
treasures = []
levels.append(level_1)
#Class Pen
pen = Pen()
player = Player()
checkpoing = Checkpoint()

#Criando uma Lista de cordenadas para restrição da parede
walls = []

def construir_jogo(level):
    """ Método factory para uma instância Jogavel arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    for y in range(len(level)):
        for x in range(len(level)):
            character = level[y][x]
            screan_x = -288 + (x*24)
            screan_y = 288 - (y*24)

            if character == "X":
                pen.goto(screan_x, screan_y)
                pen.shape("wall.gif")
                pen.stamp()
                #Condição de coordenadas para travar as paredes
                walls.append((screan_x, screan_y))
            if character == "P":
                player.goto(screan_x, screan_y)
            if character == "C":
                checkpoing.goto(screan_x, screan_y)
            if character == "T":
                treasures.append(Treasure(screan_x, screan_y))