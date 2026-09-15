import re
import math
from Lexer import Lexer
from dataclasses import dataclass
from enum import Enum, auto


substituicaoEntrada = {
    # Prioridades de cálculo
    '[': '(',
    ']': ')',
    '{': '(',
    '}': ')',
    # Potência
    '^': '**',
    'potencia de': '**',
    'elevado a': '**',
    'ao quadrado': '**2',
    'ao cubo': '**3',
    # Multiplicação
    'x': '*',
    'multiplicado por': '*',
    'vezes': '*',
    # Soma
    'mais': '+',
    # Subtração
    'menos': '-',
    # Divisão
    'dividido por': '/',
    '÷': '/',
    'pela metade': '/2',
    # Tradução Decimal
    ',': '.',
    #Logaritmo de base 10
    'logaritmo de base 10':'math.log10(',
    'logaritmo 10': 'math.log10(',
    'log10': 'math.log10(',
    #Logaritmo de base 2
    'logaritmo de base 2':'math.log2(',
    'logaritmo 2': 'math.log2(',
    'log2': 'math.log2(',
    #Logaritmo natural
    'logaritmo de':'math.log(',
    'logaritmo':'math.log(',
    'log':'math.log(',
    # Raiz Cubica
    'raiz cubica de': 'math.cbrt(',
    'raíz cúbica de': 'math.cbrt(',
    'raíz cúbica': 'math.cbrt(',
    'raiz cubica': 'math.cbrt(',
    # Razões trigonométricas
    'seno de': 'math.sin(math.radians(',
    'seno': 'math.sin(math.radians(',
    'sen': 'math.sin(math.radians(',
    'tangente de': 'math.tan(math.radians(',
    'tangente': 'math.tan(math.radians(',
    'tan': 'math.tan(math.radians(',
    'cosseno de': 'math.cos(math.radians(',
    'cosseno': 'math.cos(math.radians(',
    'cos': 'math.cos(math.radians(',
    # Fatorial
    'fatorial de': 'math.factorial(',
    'fatorial': 'math.factorial(',
    '!': 'math.factorial(',
    # Raiz Quadrada
    'raiz de': '√',
    'raíz de': '√',
    'raíz': '√',
    'raiz': '√',
    # Definição de Constantes
    'π': '3.1415926535897932384626433832795028841971693993751',
    'pi': '3.1415926535897932384626433832795028841971693993751',
    'e': '2.71828182845904523536028747135266249775724709369995',

    # Definição de porcentagem
    '%': '/100',
}

# # Faz a substituição da entrada uma única vez
padraoLimpezaEntrada = re.compile("|".join(re.escape(chave) for chave in substituicaoEntrada.keys()))

def higienizarEntrada(texto: str) -> str:
    texto_minusculo = texto.lower().strip()

    # Ajustando o ! como fatorial antes da limpeza
    texto_minusculo = re.sub(r'(\d+(?:\.\d+)?)\s*!', r'math.factorial(\1)', texto_minusculo)

    resultado = padraoLimpezaEntrada.sub(lambda m: substituicaoEntrada[m.group(0)], texto_minusculo)
    #Padroes de entradas
    resultado = re.sub(r'√(\s?\d+(?:\.\d+)?)', r'(\1 ** 0.5)', resultado)
    resultado = re.sub(r'metade de(\s\d+(?:\.\d+)?)', r'(\1 /2)', resultado)

    #Fechando os colchetes do cálculo, necessário para operações de seno e cosseno
    abertos = resultado.count('(')
    fechados = resultado.count(')')
    if abertos > fechados:
        resultado += ')' * (abertos - fechados)

    return resultado

# |---------------- Fluxo Principal ----------------|

operacao = ''

while operacao.lower() not in ['exit', 'quit', 'sair']:
    # conta = re.search(r'^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(?:\.\d+)?)\s*$', operacao)

    operacao = input('Qual a sua operação? ')
    if operacao.lower() in ['exit', 'quit', 'sair']:
        print('Encerrando operações.')
        break

    limparOrientacaoEntrada = higienizarEntrada(operacao)

    padrao_seguro = r'^(?:[\d\s\+\-\*/\.\(\)]|math|sin|cos|tan|cbrt|radians|log10|log2|log|factorial)+$'

    if not re.match(padrao_seguro, limparOrientacaoEntrada):
        print('ERRO: A sua equação contém caracteres inválidos. ')
        continue

    try:
        resultado = eval(limparOrientacaoEntrada, {"math":math})
        print(f'Resultado: {resultado}\n')

    except ZeroDivisionError:
        print("ERRO: Não é possivel dividir um número por zero.\n")

    except OverflowError:
        print('ERRO: O resultado desta potência é grande demais para ser calculado. \n')

    except SyntaxError:
        print('ERRO: A formatação do cálculo está incorreta. \n')

    except Exception as e:
        print(f'ERRO: Cálculo inválido. \n')


