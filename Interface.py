# from Evaluator import Evaluator
# from Lexer import Lexer
# from Parser import Parser
# from Translator import Translator
#
# # 1. A matéria-prima bruta
# expressao = input('Faça uma operação: ')
#
# # 1.5 Tranlator inicia com a expressao digitada
# meu_translator = Translator(expressao)
#
# # 1.7 Translator executa a limpeza de linguagem da entrada
#
#
# # 2. Ligando a primeira máquina (Lexer)
# # Como você cria um objeto da classe Lexer entregando a 'expressao' para ele?D
# meu_lexer = Lexer()
#
# # Como você pede para o 'meu_lexer' executar o método que empacota tudo
# # (aquele método tokenize() que testamos ontem) e guarda o resultado?
# lista_de_tokens = meu_lexer.tokenize()
#
# # 3. Ligando a segunda máquina (Parser)
# # Como você cria um objeto da classe Parser entregando a 'lista_de_tokens' para ele?
# meu_parser = Parser(lista_de_tokens)
#
# # Como você pede para o 'meu_parser' executar o método principal dele e guarda o resultado?
# fila_final = meu_parser.parse()
#
# meu_avaliador = Evaluator(fila_final)
#
# resultado = meu_avaliador.evaluate()
#
# # 4. Inspecionando o produto final
# print(resultado)