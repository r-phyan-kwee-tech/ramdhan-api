import uuid

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import seeds
from database import db_session
from manager import State, Day
from rabbit import Rabbit


class SheetFetch(object):
    def fetch(self, country_id):
        fetch_state = False
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)
        sh = gspread.authorize(credentials).open_by_key('1SjJG2RzITf8qAmYDU9RFnWVaMP9912y8KfbuJe8th-c')

        country_id = str(country_id)
        for ws_count, worksheet in enumerate(sh.worksheets()):
            # TODO write State By Country Here

            state_name = seeds.get_state_name(worksheet.title)
            state_id = str(uuid.uuid4().hex)
            state = State(id=state_id, object_id=state_id, country_id=str(country_id), name_mm_uni=str(state_name),
                          name_mm_zawgyi=Rabbit.uni2zg(state_name))
            cal_day_list = worksheet.col_values(1)
            hij_day_list = worksheet.col_values(2)
            sehri_time_list = worksheet.col_values(3)
            iftari_time_list = worksheet.col_values(4)

            db_session.add(state)
            db_session.commit()
            for i, (cal_day, hij_day, seh_time, iftar_time) in enumerate(
                    zip(cal_day_list, hij_day_list, sehri_time_list, iftari_time_list)):
                if i is not 0:
                    article_id = str(uuid.uuid4().hex)
                    article = Day(id=article_id, object_id=article_id,
                                  country_id=str(country_id),
                                  state_id=str(state.object_id),
                                  day=i, day_mm=str(seeds.get_mm_num(i)), sehri_time=str(seh_time + " am"),
                                  sehri_time_desc="Sehri",
                                  calendar_day=str(cal_day),
                                  hijari_day=str(hij_day),
                                  sehri_time_desc_mm_zawgyi=Rabbit.uni2zg("ဝါချည်ချိန်"),
                                  sehri_time_desc_mm_uni="ဝါချည်ချိန်",
                                  iftari_time=str(iftar_time + " pm"),
                                  dua_mm_uni=Rabbit.zg2uni(seeds.daily_dua(i)["dua_mm"]),
                                  dua_mm_zawgyi=Rabbit.uni2zg(seeds.daily_dua(i)["dua_mm"]),
                                  dua_ar=seeds.daily_dua(i)["dua_ar"],
                                  dua_en=seeds.daily_dua(i)["dua_en"],
                                  iftari_time_desc="Iftari",
                                  iftari_time_desc_mm_zawgyi=Rabbit.uni2zg("ဝါဖြေချိန်"),
                                  iftari_time_desc_mm_uni="ဝါဖြေချိန်")

                    db_session.add(article)
                    db_session.commit()
                    fetch_state = True

        return fetch_state
