import time
from regras_jogo import construir_jogo
from agentes import construir_agente
import turtle

#Setando o Mapa do Labirinto
#wn = turtle.Screen()
#wn.bgcolor("white")
##wn.title("Labirinto")
#wn.setup(700, 700)

#Registrando os GIFS
#turtle.register_shape("person.gif")
#turtle.register_shape("wall.gif")
#turtle.register_shape("finish.gif")

#Criando uma Caneta para Desenhar o Mapa
#class Pen (turtle.Turtle):
  #  def __init__(self):
   #     turtle.Turtle.__init__(self)
  #       self.color("black")
 #       self.penup()
#        self.speed(0)

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

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, passe 1 (rodada), senão se o jogo for
    continuo ou estratégico, precisa.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():

    # Inicializar e configurar jogo
    jogo = construir_jogo(level_1)
    id_jogador, jogador = jogo.registrarAgenteJogador(), construir_agente()
    tempo_de_jogo = 0

    while not jogo.isFim():

        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(id_jogador)
        jogador.adquirirPercepcao(ambiente_perceptivel)

        # Decidir jogada e apresentar ao jogo
        acao = jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(id_jogador, acao)

        # Atualizar jogo
        tempo_corrente = ler_tempo()
        jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += tempo_corrente


if __name__ == '__main__':
    iniciar_jogo()
