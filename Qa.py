import unittest

def f(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

class QaTestCase(unittest.TestCase):
    def setUp(self):
        self.testqa_str = "junyiacademy"

    def tearDown(self):
        self.testqa_str = None

    def test_Qa(self):
        qa_expected_str = "ymedacaiynuj"
        result = f(self.testqa_str)
        self.assertEqual(qa_expected_str, result)
suite = unittest.TestSuite()
suite.addTest(QaTestCase('test_Qa'))

unittest.TextTestRunner(verbosity=2).run(suite)