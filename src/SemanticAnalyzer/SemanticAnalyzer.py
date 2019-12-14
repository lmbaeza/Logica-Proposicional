
# Clase padre para todas las Expresiones
class Expression(object):
    def evaluate(self):
        # Acá se implementa cada tipo de expresion.
        raise NotImplementedError


class StatementList(Expression):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def evaluate(self):
        if self.value is not None:
            self.value.evaluate()
        return self.next


class StatementMain(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        return super().evaluate()


class StatementAssignComparison(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Assign Comparison')


class StatementAssign(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Assign')

class StatementExpr(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Expr')


class ExpressionBinop(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('BinOp')


class ExpressionUminus(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Uminus')


class ExpressionGroup(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Group')


class ExpressionId(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Expression ID')


class Comparison(Expression):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        print('Comparison')