import unittest
from flatten_a_dictionary import flatten_dicionary


class test_flatten_a_dicionary(unittest.TestCase):
    def testcase_1(self):
        myInput = {"Key1": "1", "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": "1"}}}
        expected = {
            "Key1": "1",
            "Key2.a": "2",
            "Key2.b": "3",
            "Key2.c.d": "3",
            "Key2.c.e": "1",
        }
        self.assertEqual(flatten_dicionary(myInput), expected)

    def testcase_2(self):
        myInput = {"Key": {"a": "2", "b": "3"}}
        expected = {"Key.a": "2", "Key.b": "3"}
        self.assertEqual(flatten_dicionary(myInput), expected)

    def testcase_3(self):
        myInput = {
            "Key1": "1",
            "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": {"f": "4"}}},
        }
        expected = {
            "Key1": "1",
            "Key2.a": "2",
            "Key2.b": "3",
            "Key2.c.d": "3",
            "Key2.c.e.f": "4",
        }
        self.assertEqual(flatten_dicionary(myInput), expected)

    def testcase_4(self):
        myInput = {"": {"a": "1"}, "b": "3"}
        expected = {"a": "1", "b": "3"}
        self.assertEqual(flatten_dicionary(myInput), expected)

    def testcase_5(self):
        myInput = {"a": {"b": {"c": {"d": {"e": {"f": {"": "awesome"}}}}}}}
        expected = {"a.b.c.d.e.f": "awesome"}
        self.assertEqual(flatten_dicionary(myInput), expected)

    def testcase_6(self):
        myInput = {"a": "1"}
        expected = {"a": "1"}
        self.assertEqual(flatten_dicionary(myInput), expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
