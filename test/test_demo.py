import unittest

from database import db_session
from manage import Day
from rabbit import Rabbit


class MockResponse(object):

    def __init__(self, html):
        self.str_success_html = html


class TestScrapper(unittest.TestCase):
    def test_mm_num_gen(self):
        all_day = db_session.query(
            Day).filter(Day.id!=None).all()

        for i,r_day in enumerate(all_day):
            print(i)
            print(r_day.day)
            r_day.sehri_time_desc="Sehri"
            r_day.sehri_time_desc_mm_zawgyi=Rabbit.uni2zg("ဝါချည်ချိန်")
            r_day.sehri_time_desc_mm_uni="ဝါချည်ချိန်"
            from seeds import daily_dua
            r_day.dua_mm_uni=Rabbit.zg2uni(str(daily_dua(r_day.day)["dua_mm"]))
            r_day.dua_mm_zawgyi=daily_dua(r_day.day)["dua_mm"]
            r_day.dua_ar=daily_dua(r_day.day)["dua_ar"]
            r_day.dua_en=daily_dua(r_day.day)["dua_en"]
            r_day.iftari_time_desc="Iftari"
            r_day.iftari_time_desc_mm_zawgyi=Rabbit.uni2zg("ဝါဖြေချိန်")
            r_day.iftari_time_desc_mm_uni="ဝါဖြေချိန်"
            db_session.commit()
        print(all_day)

