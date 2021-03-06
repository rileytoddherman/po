class Problem:
    def __init__(self, variables, constraints, objective_funcs):
        self.variables = variables
        self.constraints = constraints
        self.objective_funcs = objective_funcs

    def __str__(self):
        return "Problem: \n\tvariables: " + str([str(var) for var in self.variables]) + "\n\tconstraints: " + str(
            [str(con) for con in self.constraints])

    def consistent(self):
        for constraint in self.constraints:
            if not constraint.holds(self.variables):
                return False
        return True

    def will_be_consistent(self, variable_index, variable_value):
        if variable_index < 0 or variable_index >= len(self.variables):
            return False
        old_value = self.get_value(variable_index)
        self.set_value(variable_index, variable_value)
        consistent = self.consistent()
        self.set_value(variable_index, old_value)
        return consistent

    def all_assigned(self):
        for variable in self.variables:
            if variable.get_value() is None:
                return False
        return True

    def set_value(self, variable_index, value):
        if 0 <= variable_index < len(self.variables):
            self.variables[variable_index].set_value(value)

    def get_value(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            return self.variables[variable_index].get_value()
        return None

    def reset_value(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            self.variables[variable_index].reset_value()

    def get_variables(self):
        return self.variables

    def objective_values(self):
        if self.objective_funcs is None:
            return None
        return tuple([obj_func(self.variables) for obj_func in self.objective_funcs])

    def get_random_from_variable(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            return self.variables[variable_index].get_random_from_domain()

    def num_variables(self):
        return len(self.variables)

    def variable_assignments(self):
        return tuple([v.get_value() for v in self.variables])

    def closest_in_domain(self, variable_index, value):
        if 0 <= variable_index < len(self.variables):
            return self.variables[variable_index].closest_in_domain(value)

    def get_variable_iterator(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            return iter(self.variables[variable_index].get_domain())
