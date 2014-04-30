import StringIO
import sys

from unittest import TestCase
from fizzbuzz import FizzBuzz

class FizzBuzzTest(TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def assertOutputIsExpected(self, i, expected):
        self.assertEqual(self.fizzbuzz.outputForNumber(i), expected)

        #self.assertOutputIsPrintedAsExpected(i, expected)

    # also checks the correctness of printing to the console
    def assertOutputIsPrintedAsExpected(self, i, expected):
        output = StringIO.StringIO()
        sys.stdout = output
        self.fizzbuzz.printOutputForNumber(i)
        output.seek(0)
        self.assertEqual(output.read().strip(), expected)

    def test_outputForNumber_when_01_returns_01(self):
        self.assertOutputIsExpected(1, '1')

    def test_outputForNumber_when_03_returns_fizz(self):
        self.assertOutputIsExpected(3, 'fizz')

    def test_outputForNumber_when_05_returns_buzz(self):
        self.assertOutputIsExpected(5, 'buzz')

    def test_outputForNumber_when_15_returns_fizzbuzz(self):
         self.assertOutputIsExpected(15, 'fizzbuzz')

    def test_outputForNumber_when_98_returns_fizzbuzz(self):
         self.assertOutputIsExpected(98, '98')
