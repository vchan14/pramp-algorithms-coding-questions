import unittest
from decodeVariations import decodeVariations


class test_decode_variations(unittest.TestCase):
    def testcase_1(self):
        myInput = "1262"
        expected = 3
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_2(self):
        myInput = "26"
        expected = 2
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_3(self):
        myInput = "127"
        expected = 2
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_4(self):
        myInput = "1270"
        expected = 0
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_5(self):
        myInput = "83778549129"
        expected = 2
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_6(self):
        myInput = "8254779486"
        expected = 2
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_7(self):
        myInput = "122231131122"
        expected = 120
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_8(self):
        myInput = "122212313113"
        expected = 126
        self.assertEqual(decodeVariations(myInput), expected)

    def testcase_9(self):
        myInput = "321121311231"
        expected = 65
        self.assertEqual(decodeVariations(myInput), expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
