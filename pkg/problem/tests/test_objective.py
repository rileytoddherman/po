import unittest

from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.objective import Objective
from pkg.problem.variable import Variable


def default_objective():
    return Objective(lambda vrs: sum(vr.get_value() for vr in vrs))


def default_variables():
    vrs = [Variable(DiscreteDomain([1, 2, 3, 4, 5])), Variable(DiscreteDomain([1, 2, 3, 4, 5]))]
    vrs[0].set_value(3)
    vrs[1].set_value(5)
    return vrs


class ObjectiveTest(unittest.TestCase):
    def test_get_objective_values(self):
        obj = default_objective()
        vrs = default_variables()
        self.assertEqual(obj.objective_value(vrs), 8)
        self.assertEqual(obj.objective_value(vrs), 8)
        vrs[0].set_value(4)
        self.assertEqual(obj.objective_value(vrs), 9)
