import unittest
from array_of_array_products import array_of_array_products


class test_absSort(unittest.TestCase):
    def testcase_1(self):
        myInput = []
        expected = []
        self.assertEqual(array_of_array_products(myInput), expected)

    def testcase_2(self):
        myInput = [1]
        expected = []
        self.assertEqual(array_of_array_products(myInput), expected)

    def testcase_3(self):
        myInput = [2, 2]
        expected = [2, 2]
        self.assertEqual(array_of_array_products(myInput), expected)

    def testcase_4(self):
        myInput = [2, 7, 3, 4]
        expected = [84, 24, 56, 42]
        self.assertEqual(array_of_array_products(myInput), expected)

    def testcase_5(self):
        myInput = [2, 3, 0, 982, 10]
        expected = [0, 0, 58920, 0, 0]
        self.assertEqual(array_of_array_products(myInput), expected)

    def testcase_6(self):
        myInput = [-3, 17, 430, -6, 5, -12, -11, 5]
        expected = [
            -144738000,
            25542000,
            1009800,
            -72369000,
            86842800,
            -36184500,
            -39474000,
            86842800,
        ]
        self.assertEqual(array_of_array_products(myInput), expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
