from rabbit import Rabbit


def mm_num(x):
    return {
        0: '၀',
        1: '၁',
        2: '၂',
        3: '၃',
        4: '၄',
        5: '၅',
        6: '၆',
        7: '၇',
        8: '၈',
        9: '၉'

    }[x]


def get_mm_num(num):
    mm_digit = ""
    for c in range(len(str(num))):
        mm_digit += mm_num(int(str(num)[c]))
    return mm_digit


def gen_seeds():
    import uuid
    from database import db_session, Country, State, Day

    source_arr = [{
        "base_url": "http://androidweekly.net/issues/",
        "name": "Myanmar",
        "tag": "android"
    }]
    state_arr = ["ရန်ကုန်တိုင်း", "မန္တလေးတိုင်း", "ဧရာဝတီတိုင်း", "မကွေးတိုင်း", "စစ်ကိုင်းတိုင်း", "တင်္နသာရီတိုင်း",
                 "ပဲခူးတိုင်း", "ကချင်ပြည်နယ်", "ချင်းပြည်နယ်", "ရခိုင်ပြည်နယ်", "ရှမ်းပြည်နယ်", "ကယားပြည်နယ်",
                 "ကရင်ပြည်နယ်", "မွန်ပြည်နယ်"]
    for s in source_arr:
        print("Generating Country.......\n\n\n")
        country_id = str(uuid.uuid4().hex)

        country = Country(id=country_id, object_id=country_id, name=str(s["name"]))
        db_session.add(country)
        db_session.commit()
        for state in state_arr:
            print("Generating State........\n\n")
            issue_id = str(uuid.uuid4().hex)
            issue = State(id=issue_id, object_id=issue_id, country_id=str(country.object_id), name_mm_uni=str(state),
                          name_mm_zawgyi=Rabbit.uni2zg(state))
            db_session.add(issue)
            db_session.commit()

            for art in range(1, 31):
                print("Generating Days.......\n")
                article_id = str(uuid.uuid4().hex)
                article = Day(id=article_id, object_id=article_id,
                              country_id=str(country.object_id),
                              state_id=str(issue.object_id),
                              day=art, day_mm=str(get_mm_num(art)), sehri_time="4:3" + str(art) + " am",
                              iftari_time="7:3" + str(art) + " pm"
                              )
                db_session.add(article)
                db_session.commit()
