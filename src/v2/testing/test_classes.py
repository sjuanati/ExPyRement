from unittest import TestCase
from .classes import Printer, PrinterError


class TestPrinter(TestCase):
    #  option 1: run this setup for every test
    #            advantage is that arguments can be changed depending on the test
    #            This method has to be literally names "setUp"
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    # option 2: run this only once and use in all tests
    #           for this printer test, it's highly not recommended because the capacity will change,
    #           so every new test will run with a different capacity value
    @classmethod
    def setUpClass(cls):
        cls.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        # if no error is raised, the tests passes
        self.printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        # this would fail if in the class we had the if statement like:
        # `if pages >= self._capacity` : this wouldn't print the last page
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."
        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_initial_params(self):
        pages_per_s = self.printer.pages_per_s
        capacity = self.printer._capacity
        self.assertEqual(pages_per_s, 2.0)
        self.assertEqual(capacity, 300)

    def test_speed_always_two_decimals(self):
        # ensure it's 3.67 instead of 3.66666666
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = "Printed 11 pages in 3.67 seconds."
        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)
        with self.assertRaises(PrinterError):
            self.printer.print(1)
