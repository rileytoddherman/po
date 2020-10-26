from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.objective import Objective
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem


def default_variables():
    return [
        Variable(DiscreteDomain([0, 1, 2, 3, 4, 5]), []),
        Variable(DiscreteDomain([0, 1, 2, 3, 4, 5]), []),
        Variable(DiscreteDomain([0, 1, 2, 3, 4, 5]), []),
    ]


def default_consistent_problem():
    variables = default_variables()
    return Problem(
        variables,
        [
            Constraint((0, 1),
                       lambda vrs: vrs[0].get_value() != vrs[1].get_value()),
            Constraint(tuple([2]), lambda vrs: vrs[0].get_value() > 0),
        ], [Objective(lambda vrs: vrs[0].get_value()), Objective(lambda vrs: vrs[1].get_value()),
            Objective(lambda vrs: vrs[2].get_value())])


def default_consistent_problem_set_values():
    problem = default_consistent_problem()
    problem.set_value(0, 2)
    problem.set_value(1, 1)
    problem.set_value(2, 2)
    return problem


def default_inconsistent_problem():
    variables = default_variables()
    return Problem(
        variables,
        [
            Constraint((0, 2),
                       lambda vrs: False),
        ], [Objective(lambda vrs: vrs[0].get_value()), Objective(lambda vrs: vrs[1].get_value()),
            Objective(lambda vrs: vrs[2].get_value())])


def default_inconsistent_problem_set_values():
    problem = default_inconsistent_problem()
    problem.set_value(0, 2)
    problem.set_value(1, 1)
    problem.set_value(2, 2)
    return problem


def default_multi_objective_problem():
    variables = default_variables()
    return Problem(
        variables,
        [
            Constraint((0, 2),
                       lambda vrs: vrs[0] == vrs[1]),
            Constraint(tuple([1]), lambda vrs: vrs[0] == 1),
            Constraint(tuple([2]), lambda vrs: vrs[0] > 0)
        ], [Objective(lambda vrs: sum(var.get_value() for var in vrs)),
            Objective(lambda vrs: -sum(var.get_value() for var in vrs))])


def default_multi_objective_problem_set_values():
    problem = default_multi_objective_problem()
    problem.set_value(0, 2)
    problem.set_value(1, 1)
    problem.set_value(2, 2)
    return problem
