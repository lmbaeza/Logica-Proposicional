from src.SyntacticAnalyzer.Parser import Parser

parser = Parser()



with open('./example/input-1.txt', 'r') as file:
    code = file.read()
    parser.run(code)
