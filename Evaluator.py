import operator

from Lexer import TokenType



class Evaluator:

    def __init__(self,fila_final):
        self.fila_final = fila_final

    def evaluate(self):
        operacoes = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        pilha = []
        for token in self.fila_final:
            match token.type:
                case TokenType.NUMBER:
                    pilha.append(token.value)
                case TokenType.OPERATOR:
                    a = pilha.pop()
                    b = pilha.pop()
                    funcao = operacoes[token.value]
                    resultado = funcao(b, a)  # b é o elemento da esquerda, a é o da direita
                    pilha.append(resultado)
        return pilha.pop()