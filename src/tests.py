# -*- coding: utf-8 -*-
"""Unit tests on mutant checker
"""

import unittest
from utils import checker


class TestChecker(unittest.TestCase):

    def test_human(self):
        self.assertEqual(checker.is_mutant([
            "ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"
        ]), False)

    def test_mutant_full(self):
        self.assertEqual(checker.is_mutant([
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTA"
        ]), True)

    def test_mutant_horizontal(self):
        self.assertEqual(checker.is_mutant([
            "TTGCAA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTA"
        ]), True)

    def test_mutant_vertical(self):
        self.assertEqual(checker.is_mutant([
            "TTGCGA", "CAGTGC", "TTATGT", "AGAAGG", "ACCCTA", "TCACTA"
        ]), True)

    def test_mutant_diagonal_right(self):
        self.assertEqual(checker.is_mutant([
            "ATGCAA", "CAGTGC", "TTATGT", "AGAAGG", "ACCCTA", "TCACTA"
        ]), True)

    def test_mutant_diagonal_left(self):
        self.assertEqual(checker.is_mutant([
            "TTGCAA", "CAGTGC", "TTATCT", "AGACGG", "ACCCTA", "TCACTA"
        ]), True)


if __name__ == '__main__':
    unittest.main()
