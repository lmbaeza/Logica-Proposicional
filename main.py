from src.SyntacticAnalyzer.Parser import Parser

parser = Parser()


code = '''
void main() {
    x := 12;
    p := p == 0;
}
'''
parser.run(code)
