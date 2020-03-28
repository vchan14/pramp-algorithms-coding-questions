import unittest
from absSort import absSort


class test_absSort(unittest.TestCase):
    def testcase_1(self):
        myInput =  [2,-7,-2,-2,0]
        expected = [0,-2,-2,2,-7]
        self.assertEqual(absSort(myInput), expected)

    def testcase_2(self):
        myInput =  [-2,1]
        expected = [1,-2]
        self.assertEqual(absSort(myInput), expected)
    
    def testcase_3(self):
        myInput = [0,1,2]
        expected =[0,1,2]
        self.assertEqual(absSort(myInput), expected)
    
    def testcase_4(self):
        myInput =  [2,-1,-1,-1]
        expected =[-1,-1,-1,2]
        self.assertEqual(absSort(myInput), expected)
    
    def testcase_5(self):
        myInput = [-2,3,5,-1,4]
        expected = [-1,-2,3,4,5]
        self.assertEqual(absSort(myInput), expected)
    
    def testcase_6(self):
        myInput =  [4,-1,6,-4,2,-1]
        expected = [-1,-1,2,-4,4,6]
        self.assertEqual(absSort(myInput), expected)
    
    def testcase_7(self):
        myInput = [6,4,-5,0,-1,7,0]
        expected =[0,0,-1,4,-5,6,7]
        self.assertEqual(absSort(myInput), expected)
    
    def testcase_8(self):
        myInput =  [-7,-2,-2,6,5,-6,-2,-6]
        expected = [-2,-2,-2,5,-6,-6,6,-7]

        self.assertEqual(absSort(myInput), expected)
    
    def testcase_9(self):
        myInput =[-4,9,-1,1,-1,2,-8,-6,3]
        expected = [-1,-1,1,2,3,-4,-6,-8,9]
        self.assertEqual(absSort(myInput), expected)




def main():
    unittest.main()

if __name__ == "__main__":
    main()
