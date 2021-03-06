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

# Implemente seu jogador humano nessa classe, sobrescrevendo os métodos
# abstratos de Agente. Em construir_agente, retorne uma instância dessa classe.
class AgenteHumano(Agente):
    
    def adquirirPercepcao(self, percepcao_mundo):
        # Utilize percepcao de mundo para atualizar tela (terminal ou blit),
        # tocar sons, dispositivos hápticos, etc, todo e qualquer dispositivo
        # de saída para interface humana.
        
        raise NotImplementedError
    
    def escolherProximaAcao(self):
        # Receba entrada humana apenas neste momento, seja com prompt (terminal)
        # ou polling (jogos interativos).
        
        raise NotImplementedError


def construir_agente(tipo_agente):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    if tipo_agente == 'HUMANO':
        agente = AgenteHumano()
    elif tipo_agente == 'ROBO':
        agente = AgenteRobo()
    else:
        raise print("Tipo de agente desconhecido. Por favor escolha HUMANO ou ROBO.")
    return agente