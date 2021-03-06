import unittest
from pkg.branchbound.branch_bound import BranchBound
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.log import Log


class BranchBoundTest(unittest.TestCase):
    def test_solve(self):
        branch_bound = BranchBound(default_consistent_problem())
        solutions = branch_bound.solve()
        Log.newline()
        Log.log([str(s) for s in solutions], context="test-branch-bound")
