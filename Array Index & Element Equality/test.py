import unittest
from index_equals_value_search import index_equals_value_search


class test_flatten_a_dicionary(unittest.TestCase):
    def testcase_1(self):
        myInput = [0]
        expected = 0
        self.assertEqual(index_equals_value_search(myInput), expected)

    def testcase_2(self):
        myInput = [0, 3]
        expected = 0
        self.assertEqual(index_equals_value_search(myInput), expected)

    def testcase_3(self):
        myInput = [-8, 0, 1, 3, 5]
        expected = 3
        self.assertEqual(index_equals_value_search(myInput), expected)

    def testcase_4(self):
        myInput = [-5, 0, 2, 3, 10, 29]
        expected = 2
        self.assertEqual(index_equals_value_search(myInput), expected)

    def testcase_5(self):
        myInput = [-5, 0, 3, 4, 10, 18, 27]
        expected = -1
        self.assertEqual(index_equals_value_search(myInput), expected)

    def testcase_6(self):
        myInput = [-6, -5, -4, -1, 1, 3, 5, 7]
        expected = 7
        self.assertEqual(index_equals_value_search(myInput), expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
