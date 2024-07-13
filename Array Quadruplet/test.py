import unittest
from find_array_quadruplet import find_array_quadruplet


class test_absSort(unittest.TestCase):
    def testcase_1(self):
        myInput = []
        s = 12
        expected = []
        self.assertEqual(find_array_quadruplet(myInput, s), expected)

    def testcase_2(self):
        myInput = [4, 4, 4]
        s = 12
        expected = []
        self.assertEqual(find_array_quadruplet(myInput, s), expected)

    def testcase_3(self):
        myInput = [4, 4, 4, 2]
        s = 16
        expected = []
        self.assertEqual(find_array_quadruplet(myInput, s), expected)

    def testcase_4(self):
        myInput = [4, 4, 4, 4]
        s = 16
        expected = [4, 4, 4, 4]
        self.assertEqual(find_array_quadruplet(myInput, s), expected)

    def testcase_5(self):
        myInput = [2, 7, 4, 0, 9, 5, 1, 3]
        s = 20
        expected = [0, 4, 7, 9]
        self.assertEqual(find_array_quadruplet(myInput, s), expected)

    def testcase_6(self):
        myInput = [2, 7, 4, 0, 9, 5, 1, 3]
        s = 120
        expected = []
        self.assertEqual(find_array_quadruplet(myInput, s), expected)

    def testcase_7(self):
        myInput = [1, 2, 3, 4, 5, 9, 19, 12, 12, 19]
        s = 40
        expected = [4, 5, 12, 19]
        self.assertEqual(find_array_quadruplet(myInput, s), expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
