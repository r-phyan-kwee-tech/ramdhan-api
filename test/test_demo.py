import unittest


class MockResponse(object):

    def __init__(self, html):
        self.str_success_html = html


class TestScrapper(unittest.TestCase):
    def test_mm_num_gen(self):
        from seeds import get_mm_num
        assert get_mm_num(10) == '၁၀'
        assert get_mm_num(100) == '၁၀၀'
        assert get_mm_num(1234567890) == '၁၂၃၄၅၆၇၈၉၀'
