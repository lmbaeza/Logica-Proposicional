from ply import lex
from ply.lex import TOKEN
import re


class Lexer:

    t_PREDICADO_ARITMETICO = r'[pqrtPQRT]([0-9]{1}|[0-9]{2}|[0-9]{3}|[0-9]{4}|[0-9]{5})?'
    t_PREDICADO_ALGEBRAICO = r'[xyzXYZ]([0-9]{1}|[0-9]{2}|[0-9]{3}|[0-9]{4}|[0-9]{5})?'
    t_LPAREN      = r'\('
    t_RPAREN      = r'\)'
    
    t_SEMICOLON   = r';'

    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'

    t_LSQUARE_BRACKET = r'\['
    t_RSQUARE_BRACKET = r'\]'
    t_LCURLY_BRACKET  = r'\{'
    t_RCURLY_BRACKET  = r'\}'


    t_EQUAL       = r'\=\='
    t_NOTEQ       = r'\!\='
    t_LARGE       = r'\>'
    t_LARGE_EQ    = r'\>\='
    t_SMALL       = r'\<'
    t_SMALL_EQ    = r'\<\='

    t_EQUALS      = r'\:\='
    t_ASSIGN_COMP = r'\:'

    t_MAIN        = r'(main)'
    t_VOID        = r'(void)'

    # Ignorar Caracteres
    t_ignore      = ' \t'

    def __init__(self, *args, **kwargs):
        self.tokens = [
            'PREDICADO_ARITMETICO', 'PREDICADO_ALGEBRAICO', 'LPAREN', 'RPAREN', 'SEMICOLON',
            'EQUAL', 'NOTEQ', 'LARGE', 'LARGE_EQ', 'SMALL', 'SMALL_EQ', 'INTEGER', 'FLOAT',
            'ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'ASSIGN_COMP', 'LSQUARE_BRACKET',
            'RSQUARE_BRACKET', 'LCURLY_BRACKET', 'RCURLY_BRACKET'
        ]

        self.keywords = {
            'void': 'VOID',
            'main': 'MAIN'
        }

        self.tokens +=  list([v for k, v in self.keywords.items()])
        self.lexer = lex.lex(module=self, **kwargs)


    @TOKEN(r'[0-9]+')
    def t_INTEGER(self, token):
        try:
            token.value = int(token.value)
        except ValueError:
            print("Integer value too large %d", token.value)
            token.value = 0
        return token
    

    @TOKEN(r'[-+]?[0-9]+(\.[0-9]+)([eE][-+]?[0-9]+)?')
    def t_FLOAT(self, token):
        try:
            token.value = float(token.value)
        except ValueError:
            print("Float value too large %f", token.value)
            token.value = 0
        return token
    
    @TOKEN(r'[a-zA-Z]([a-zA-Z]|[0-9]|"_")*')
    def t_ID(self, token):
        result = re.match(self.t_PREDICADO_ALGEBRAICO, str(token.value))
        
        if result != None:
            token.type = 'PREDICADO_ALGEBRAICO'
            return token
        
        result = re.match(self.t_PREDICADO_ARITMETICO, str(token.value))

        if result != None:
            token.type = 'PREDICADO_ARITMETICO'
        else:
            if token.value in self.keywords:
                token.value = token.value.upper();
                token.type = token.value
        return token


    @TOKEN(r'\n+')
    def t_newline(self, token):
        token.lexer.lineno += len(token.value)


    def t_error(self, token):
        print("Illegal character '%s'" % token.value[0])
        token.lexer.skip(1)
    

    def getTokens(self):
        return self.tokens
    

    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: break
            print(tok)