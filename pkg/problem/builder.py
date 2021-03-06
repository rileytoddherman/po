from copy import deepcopy
from math import floor

from pkg.problem.continuous_domain import ContinuousDomain
from pkg.random.random import Random
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint
from pkg.client.stock_client import StockClient, stock_names
from pkg.consts import Constants
from pkg.log import Log


def default_portfolio_optimization_problem():
    def convert_stock_data_to_variable(vsd):
        return Variable(ContinuousDomain(0, floor(float(Constants.BUDGET) / vsd['price'])), vsd)

    def get_budget_constraint():
        return Constraint(tuple(i for i in range(len(stock_names))), lambda vsds: Constants.BUDGET > sum(
            [(0.0 if vsd.get_value() is None else vsd.get_value()) * vsd.get_objective_info()['price'] for vsd in
             vsds]))

    def get_risk_objective():
        return lambda vsds: -sum(
            [(1.0 if vsd.get_value() is None else vsd.get_value()) * vsd.get_objective_info()['risk'] for vsd in vsds])

    def get_reward_objective():
        return lambda vsds: sum(
            [(1.0 if vsd.get_value() is None else vsd.get_value()) * vsd.get_objective_info()['reward'] for vsd in
             vsds])

    stock_data = StockClient().get_stock_data()
    thing = {sd: [str(key) + ": " + str(stock_data[sd][key]) for key in stock_data[sd]] for sd in stock_data}
    Log.begin_debug("default-po-problem")
    for t in thing:
        Log.log(t)
        for j in thing[t]:
            Log.log("\t" + str(j))
    Log.end_debug()
    return Problem([convert_stock_data_to_variable(stock_data[vsd]) for vsd in stock_data], [get_budget_constraint()],
                   [get_risk_objective(), get_reward_objective()])


def generate_many_random_solutions(problem, population_size):
    individuals = set()
    give_up = 0
    while len(individuals) < population_size and give_up < Constants.GIVE_UP_MAX:
        p = deepcopy(problem)
        for v in range(p.num_variables()):
            p.set_value(v, p.get_random_from_variable(v))
        if p.consistent() and p.variable_assignments() not in [i.variable_assignments() for i in individuals]:
            individuals.add(p)
        else:
            give_up += 1
    return individuals
