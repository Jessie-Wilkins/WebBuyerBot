import unittest

class WebBuyerTest(unittest.TestCase):

    def test_one_equal_one(self):
        self.assertEqual(1, 1)
    
    def test_will_fail(self):
        self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()
