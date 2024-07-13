import unittest
from sort_k_messed_array import sort_k_messed_array


class test_flatten_a_dicionary(unittest.TestCase):
    def testcase_1(self):
        myInput = [1]
        k = 0
        expected = [1]
        self.assertEqual(sort_k_messed_array(myInput, k), expected)

    def testcase_2(self):
        myInput = [1, 0]
        k = 1
        expected = [0, 1]
        self.assertEqual(sort_k_messed_array(myInput, k), expected)

    def testcase_3(self):
        myInput = [1, 0, 3, 2]
        k = 1
        expected = [0, 1, 2, 3]
        self.assertEqual(sort_k_messed_array(myInput, k), expected)

    def testcase_4(self):
        myInput = [1, 0, 3, 2, 4, 5, 7, 6, 8]
        k = 1
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(sort_k_messed_array(myInput, k), expected)

    def testcase_5(self):
        myInput = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
        k = 2
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sort_k_messed_array(myInput, k), expected)

    def testcase_6(self):
        myInput = [6, 1, 4, 11, 2, 0, 3, 7, 10, 5, 8, 9]
        k = 6
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertEqual(sort_k_messed_array(myInput, k), expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
