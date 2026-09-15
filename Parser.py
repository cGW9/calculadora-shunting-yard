from Lexer import Lexer



# Associatividade: 'L' = Esquerda para Direita, 'R' = Direita para Esquerda
operadores = {
    '+': {'precedencia':1, 'associatividade': 'L'},
    '-': {'precedencia':1, 'associatividade': 'L'},
    '*': {'precedencia':2, 'associatividade': 'L'},
    '/': {'precedencia':2, 'associatividade': 'L'},
    '**': {'precedencia':3, 'associatividade': 'R'},
    '√': {'precedencia':3, 'associatividade': 'L'},
    '%': {'precedencia':3, 'associatividade': 'R'}

}
class Parser:
    output_queue = []
    stack_op = []

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
