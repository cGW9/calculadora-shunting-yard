from dataclasses import dataclass
from enum import Enum, auto


# Catálogo fixo de categorias
class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    FUNCTION = auto()
    LPAREN = auto()
    RPAREN = auto()

# O contêiner que carrega o dado real
@dataclass
class Token:
    type: TokenType
    value: any

# Lexer
class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None
    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_char(self):

        self.skip_whitespace()
        if self.current_char is None:
            return None

        match self.current_char:
            case char if char.isdigit():
                return self.read_number()

            case '+' | '-' | '*' | '/':
                operator = self.current_char
                self.advance()
                return Token(TokenType.OPERATOR, operator)

            case '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')

            case ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')

            case None:
                self.advance()
                return None

            case _:
                raise ValueError(f"Caractere inválido: {self.current_char}")


    def read_number(self) -> Token:
        buffer = ''
        has_dot = False
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.') :

            if self.current_char == '.':
                if has_dot:
                    raise ValueError("Número inválido: múltiplos pontos decimais")
                has_dot = True

            buffer += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, float(buffer))

    def tokenize(self) -> list[Token]:
        tokens = []
        while True:
            token = self.get_next_char()
            if token is None:
                break
            tokens.append(token)
        return tokens
