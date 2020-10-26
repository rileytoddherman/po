from pkg.cache import cached


class Objective:
    def __init__(self, objective_func):
        self.objective_func = objective_func

    def __str__(self):
        return str(id(self.objective_func))

    def __repr__(self):
        return str(self)

    @cached
    def get_objective_value(self, variables):
        return self.objective_func(variables)
