import unittest

from pip._vendor import requests

from readingtime import ReadingTime


class MockResponse(object):

    def __init__(self, html):
        self.str_success_html = html


class TestScrapper(unittest.TestCase):

    def test_page(self):
        # print(generate_meta(10, 1, [None] * 100))
        # print(generate_meta(10, 10, [None] * 100))
        for issue_number in range(120, 305):
            print(issue_number)
        print("done")



