
from ply import yacc

from src.LexicalAnalyzer.Scanner import Lexer
from src.SemanticAnalyzer.SemanticAnalyzer import *

class Parser:

    def __init__(self):
        # Se obtienen los tokens del Analizador Lexico
        self.tokens = Lexer().getTokens()

        # Se define el nivel de prioridad para la asociación a la hora de reducir y/o desplazar las expresiones
        self.precedence = (
            ('left', 'PLUS', 'MINUS'),
            ('left', 'TIMES', 'DIVIDE'),
            ('right', 'UMINUS'),
        )

        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)


    def p_statement_list(self, AST):
        r'''statements-list : statement statements-list
                            | expression statements-list'''
        AST[0] = StatementList(value=AST[1], next=AST[2]) 


    def p_statement_list_empty(self, AST):
        r'''statements-list : '''


    def p_statement_main(self, AST):
        r'''statement : VOID MAIN LPAREN RPAREN LCURLY_BRACKET statements-list RCURLY_BRACKET'''
        next = AST[6]

        while next is not None:
            tmp = next.evaluate()
            next = tmp


    def p_statement_escribir(self, AST):
        r'''statement : ESCRIBIR LPAREN expression RPAREN SEMICOLON'''
        AST[0] = ExpressionEscribir(value=AST[3])

    def p_statement_assign_comparison(self, AST):
        r'''statement : PREDICADO_ARITMETICO ASSIGN_COMP comparison SEMICOLON'''
        AST[0] = StatementAssignComparison(aritm=AST[1], comp=AST[3])


    def p_statement_assign(self, AST):
        r'''statement : PREDICADO_ARITMETICO EQUALS expression SEMICOLON
                      | PREDICADO_ALGEBRAICO EQUALS expression SEMICOLON'''
        AST[0] = StatementAssign(varName=AST[1], expr=AST[3])


    def p_statement_expr(self, AST):
        r'''statement : expression
                      | comparison'''
        AST[0] = StatementExpr(value=AST[1])


    def p_expression_binop(self, AST):
        r'''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
        # expression : expression OPERATOR expression
        #     ^            ^          ^        ^
        #   AST[0]        AST[1]    AST[2]    AST[3]
        
        left = AST[1]
        op = AST[2]
        right = AST[3]

        if isinstance(left, ExpressionId):
            left = left.evaluate()

        if isinstance(left, int):
            left = Integer(left)
        
        while isinstance(right, Expression):
            right = right.evaluate()

        if op == '+'  : AST[0] =  left + right
        elif op == '-': AST[0] =  left - right
        elif op == '*': AST[0] =  left * right
        elif op == '/': AST[0] =  left / right


    def p_expression_uminus(self, AST):
        r'expression : MINUS expression %prec UMINUS'
        AST[0] = ExpressionUminus(value=AST[2])


    def p_expression_group(self, AST):
        r'''expression : LPAREN expression RPAREN
                       | LSQUARE_BRACKET expression RSQUARE_BRACKET'''
        AST[0] = AST[2]


    def p_expression_integer(self, AST):
        'expression : INTEGER'
        AST[0] = Integer(value=AST[1])


    def p_expression_id(self, AST):
        r'''expression : ID
                       | PREDICADO_ARITMETICO
                       | PREDICADO_ALGEBRAICO'''
        AST[0] = ExpressionId(varName=AST[1])


    def p_comparison(self, AST):
        r'''comparison : expression EQUAL expression
                       | expression NOTEQ expression
                       | expression LARGE expression
                       | expression LARGE_EQ expression
                       | expression SMALL expression
                       | expression SMALL_EQ expression'''
        AST[0] = Comparison(left=AST[1], op=AST[2], right=AST[3])
    

    def p_error(self, AST):
        print("Syntax error at '%s'" % AST.value)
        print(AST)


    def shell(self):
        exit = False
        while not exit:
            try:
                s = input('shell> ')
                if s=='exit': break
            except EOFError:
                break
            self.lexer.test(s)
            self.parser.parse(s)


    # RUN: Se corre el parser (Analizador sintáctico)
    def run(self, code):
        self.parser.parse(code)

