class Variables:
    def __init__(self):
        self.variables = {}
        return

    def set_var(self, name, value):
        self.variables[name] = value
        return

    def get_var(self, name):
        assert len(self.variables) != 0
        return self.variables[name]

    def clear_var(self, name):
        self.variables[name] = None

    def delete_var(self, name):
        self.variables.popitem(name)

    def isempty(self):
        return self.variables == {}

    def print_vars(self):
        print self.variables
