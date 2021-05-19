import unittest
import WebBuyer

class WebBuyerTest(unittest.TestCase):

    def test_if_website_can_be_loaded(self):
        WebBuyer.load_website("https://www.walmart.com/ip/Dummy-Stress-Test-Video-Game-Hardware-19/813808061")
        self.assertEqual("https://www.walmart.com/ip/Dummy-Stress-Test-Video-Game-Hardware-19/813808061", WebBuyer.get_website())

if __name__ == '__main__':
    unittest.main()
