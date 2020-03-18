# Código com definição de agentes abstratos a serem utilizados em nossas aulas.

from abc import ABC

class Agente(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return
    
    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return


class AgenteReflexivo(Agente):
    def __init__(self, regras, sensores):
        ''' Inicializa o agente e suas regras de atuação
        
        :param regras: dicionário de condição-ação, no formato modelo -> ação
        :param sensores: função que filtra de descricao do mundo o que esse
            agente pode de fato perceber.
        '''
        self.regras = regras
        self.sensores = sensores

    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        self.ultima_percepcao = percepcao_mundo

    def escolherProximaAcao(self):
        modelo_imediato = self.sensores(self.ultima_percepcao)
        acao = self.regras[modelo_imediato]
        return acao


class AgenteComModelo(Agente):
    def __init__(self, estado, modelo, regras):
        self.estado = estado
        self.modelo = modelo
        self.regras = regras
        
        # Ultima acao realizada, inicialmente nenhuma
        self.acao = None
    
    def definirAcao(self, percepcao):
        atualizarEstado(percepcao)
        acao = self.regras[estado]
        return acao
    
    def atualizarEstado(self, percepcao):
        ''' Atualiza o estado de acordo com os atributos internos (estado,
            acao, modelo) e a nova percepcao do ambiente
        '''
        pass


class AgenteComObjetivo(Agente):
    def __init__(self, estado, problema):
        self.estado = estado
        self.problema = problema
        # Uma sequencia de acoes, inicialmente vazia
        self.seq = []
        # Um objetivo, inicialmente nulo
        self.objetivo = None
    
    def definirAcao(self, percepcao):
        # Se seq estiver vazia
        if not self.seq:
            self.formularObjetivo()
            self.formularProblema()
            self.busca()
            if not self.seq:
                return None
        acao = self.seq.pop(0)
        return acao
    
    def formularObjetivo(self):
        ''' Formula um novo objetivo para o agente com base no estado.
        
            Ao final, self.objetivo deve estar preenchido.
        '''
        pass
    
    def formularProblema(self):
        ''' Formula um novo problema a ser resolvido, com base no objetivo
            atual.
            
            Ao final, self.problema deve estar preenchido.
        '''
        pass
    
    def busca():
        ''' Monta uma nova sequencia de acoes para resolver o problema atual.
        
            Ao final, self.seq deve conter uma lista de acoes.
        '''
        pass