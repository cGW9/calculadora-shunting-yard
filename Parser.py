from tokenize import Token

from Lexer import Token, TokenType, Lexer

# Associatividade: 'L' = Esquerda para Direita, 'R' = Direita para Esquerda
operadores = {
    '+': {'precedencia':1, 'associatividade': 'L'},
    '-': {'precedencia':1, 'associatividade': 'L'},
    '*': {'precedencia':2, 'associatividade': 'L'},
    '/': {'precedencia':2, 'associatividade': 'L'},
    '^': {'precedencia':3, 'associatividade': 'R'},

}
class Parser:

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens

    def parse(self):
        output_queue: list[Token] = []
        stack_op: list[Token] = []

        for token in self.tokens:
            match token.type:
                case TokenType.NUMBER:
                    output_queue.append(token)
                case TokenType.LPAREN:
                    stack_op.append(token)
                case TokenType.OPERATOR:
                    while stack_op and stack_op[-1].type != TokenType.LPAREN and (operadores[stack_op[-1].value]['precedencia'] > operadores[token.value]['precedencia'] or (operadores[stack_op[-1].value]['precedencia'] == operadores[token.value]['precedencia'] and operadores[token.value]['associatividade'] == 'L')):
                        output_queue.append(stack_op.pop())

                    stack_op.append(token)

                case TokenType.RPAREN:
                    while stack_op and stack_op[-1].type != TokenType.LPAREN:
                        output_queue.append(stack_op.pop())
                    if not stack_op:
                        raise ValueError("Erro de sintaxe: parêntese de fechamento sem abertura correspondente.")
                    stack_op.pop()



        while stack_op:
            if stack_op[-1].type != TokenType.LPAREN:
                output_queue.append(stack_op.pop())
            else:
                raise ValueError("Erro de sintaxe: parêntese de abertura sem fechamento correspondente.")

        return output_queue


