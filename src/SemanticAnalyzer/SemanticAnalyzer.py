
from src.lib.Global import VariableGlobal

varGlobal = VariableGlobal()

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
    def __init__(self, aritm, comp):
        self.aritm = aritm
        self.comp = comp
        self.table = varGlobal.table()
        varGlobal.setTable(self.aritm, self.comp)
    
    def evaluate(self):
        # if self.table.get(self.aritm) is None:
            # varGlobal.setTable(self.aritm, self.comp)
        # else:
        #     print('Error: variable "{0}" is already defined'.format(self.aritm))
        varGlobal.setTable(self.aritm, self.comp)


class StatementAssign(Expression):
    def __init__(self, varName, expr):
        self.varName = varName
        self.expr = expr
        self.table = varGlobal.table()
        varGlobal.setTable(self.varName, self.expr)
    
    def evaluate(self):
        # if self.table.get(self.varName) is None:
        #     varGlobal.setTable(self.varName, self.expr)
        # else:
        #     print('Error: variable "{0}" is already defined'.format(self.varName))
        varGlobal.setTable(self.varName, self.expr)

class StatementExpr(Expression):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        print(self.value)


class ExpressionBinop(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def evaluate(self):
        if isinstance(self.left, ExpressionId):
            self.left = self.left.evaluate()
        
        if isinstance(self.right, ExpressionId):
            self.right = self.right.evaluate()
        
        if self.op == '+'  : return self.left + self.right
        elif self.op == '-': return self.left - self.right
        elif self.op == '*': return self.left * self.right
        elif self.op == '/': return self.left / self.right


class ExpressionUminus(Expression):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        return -self.value


class ExpressionGroup(Expression):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        return self.value

class ExpressionId(Expression):
    def __init__(self, varName):
        self.varName = varName
        self.table = varGlobal.table()
    
    def evaluate(self):
        if self.table.get(self.varName) is None:
            return 0
        return self.table.get(self.varName)



class Comparison(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def evaluate(self):
        if isinstance(self.left, ExpressionId):
            self.left = self.left.evaluate()
        
        if isinstance(self.right, ExpressionId):
            self.right = self.right.evaluate()

        if self.op == '=='  : return self.left == self.right
        elif (self.op=='!='or self.op=='≠'or self.op=='<>'):
            return self.left != self.right
        elif self.op == '>': return self.left > self.right
        elif self.op == '>=': return self.left >= self.right
        elif self.op == '<': return self.left < self.right
        elif self.op == '<=': return self.left <= self.right


class ComparisonPreposition(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def evaluate(self):
        if isinstance(self.left, ExpressionId):
            self.left = self.left.evaluate()
        
        if isinstance(self.right, ExpressionId):
            self.right = self.right.evaluate()

        if self.op == '^'  : return self.left and self.right
        elif self.op=='∨': return self.left or self.right


class ExpressionEscribir(Expression):

    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        while isinstance(self.value, Expression):
            self.value = self.value.evaluate()
        print(self.value)

# Expresión para los Numeros Enteros
class Integer(Expression):
    
    def __init__(self, value):
        self.value = int(value)
    
    def evaluate(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    def __add__(self, other):
        if isinstance(other, Expression):
            return Integer(self.value + other.value)
        return Integer(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Expression):
            return Integer(self.value - other.value)
        return Integer(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Expression):
            return Integer(self.value * other.value)
        return Integer(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Expression):
            return Integer(self.value / other.value)
        return Integer(self.value / other)
    
    def __gt__(self, other):
        if isinstance(other, Expression):
            return Boolean(self.value > other.value)
        return Boolean(self.value > other)
    
    def __ge__(self, other):
        if isinstance(other, Expression):
            return Boolean(self.value >= other.value)
        return Boolean(self.value >= other)
    
    def __lt__(self, other):
        if isinstance(other, Expression):
            return Boolean(self.value < other.value)
        return Boolean(self.value < other)
    
    def __le__(self, other):
        if isinstance(other, Expression):
            return Boolean(self.value <= other.value)
        return Boolean(self.value <= other)
    
    def __eq__(self, other):
        if isinstance(other, Expression):
            return Boolean(self.value == other.value)
        return Boolean(self.value == other)
    
    def __ne__(self, other):
        if isinstance(other, Expression):
            return Boolean(self.value != other.value)
        return Boolean(self.value != other)
    
    def __neg__(self):
        return Integer(-self.value)

# Expresiones Booleanas
class Boolean(Expression):
    
    def __init__(self, value):
        self.value = None
        if value == 'true' or value == True:
            self.value = bool(True)
        elif value == 'false'or value == False:
            self.value = bool(False)
    
    def evaluate(self):
        return self.value
    
    def __str__(self):
        return self.evaluate()
    
    def __repr__(self):
        return self.evaluate()
    
    def __eq__(self, other):
        return Boolean(self.value == other.value)
    
    def __ne__(self, other):
        return Boolean(self.value != other.value)
