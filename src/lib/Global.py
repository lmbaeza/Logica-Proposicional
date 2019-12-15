
# VariableGlobal : Singleton

class VariableGlobal:

    class __VariableGlobal:

        def __init__(self):
            self.count = 1
            self.table = {}
        
        def __str__(self):
            return repr(self) + self.val
        
        def incrementCount(self, number):
            self.count += number
        
        def setTable(self, key, value):
            self.table[key] = value

        def getTable(self, key):
            return self.table.get(key)
  
    instance = None

    def __init__(self):
        if not VariableGlobal.instance:
            VariableGlobal.instance = VariableGlobal.__VariableGlobal()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __str__(self):
        return str(self.instance)
    
    def incrementCount(self, number):
        self.instance.incrementCount(number)
    
    def setTable(self, key, value):
        self.instance.setTable(key, value)
    
    def getTable(self, key):
        return self.instance.getTable(key)
    
    def table(self):
        return self.instance.table
    
    def getCount(self):
        return self.instance.count