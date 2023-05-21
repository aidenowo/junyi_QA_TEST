import unittest

def reverse(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str
def f(input_str):
    result_words=""
    input_words_list=input_str.split(" ")
    for i in range(len(input_words_list)):
        result_words+=(reverse(input_words_list[i]))
        if i != len(input_words_list)-1:
            result_words+=" "
    return result_words

class QbTestCase(unittest.TestCase):
    def setUp(self):
        self.testqb_str = "flipped classroom is important"

    def tearDown(self):
        self.testqb_str = None

    def test_Qb(self):
        qb_expected_str = "deppilf moorssalc si tnatropmi"
        result = f(self.testqb_str)
        self.assertEqual(qb_expected_str, result)
suite = unittest.TestSuite()
suite.addTest(QbTestCase('test_Qb'))

unittest.TextTestRunner(verbosity=2).run(suite)