from pkg.cache import cached
from pkg.generic import Generic


class Objective(Generic):
    def __init__(self, objective_func):
        self.objective_func = objective_func

    def __str__(self):
        return str(id(self.objective_func))

    @cached
    def get_objective_value(self, variables):
        return self.objective_func(variables)
