import os

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


def get_state_name(x):
    print(x)
    state_name = str(str(x).lower().split("|")[0]).strip()
    district_name = str(str(x).lower().split("|")[1]).strip()
    return ({'yangon': "ရန်ကုန်တိုင်း",
             'naypyidaw': "နေပြည်တော် (ပျဉ်းမနား)",
             'mandalay': "မန္တလေးတိုင်း",
             'karen': "ကရင်ပြည်နယ်",
             'mon': "မွန်ပြည်နယ်",
             'kayah': "ကယားပြည်နယ်",
             'kachin': "ကချင်ပြည်နယ်",
             'chin': "ချင်းပြည်နယ်",
             'shan_s_w': "ရှမ်းပြည်နယ်(နောက်/တောင်)",
             'shan_s_e': "ရှမ်းပြည်နယ်(ရှေ့/တောင်)",
             'shan_n': "ရှမ်းပြည်နယ်(မြောက်)",
             'rakhine': "ရခိုင်ပြည်နယ်",
             'tanintharyi': "တင်္နသာရီတိုင်း",
             'magwe': "မကွေးတိုင်း",
             'sagaing': "စစ်ကိုင်းတိုင်း",
             'irrwaddy': "ဧရာဝတီတိုင်း",
             'irrwaddy_2': "ဧရာဝတီတိုင်း",
             'ayeyarwaddy': "ဧရာဝတီတိုင်း",
             'bago_w': "ပဲခူးတိုင်း(နောက်)",
             'bago_e': "ပဲခူးတိုင်း(ရှေ့)"

             }[state_name], district_name)


def daily_dua(x):
    return {
        1: dict(
            dua_mm="အိုအလႅာလ္အရွင္ျမတ္ ကြ်ႏ္ုပ္၏ ဥပုပ္သီလေစာင့္တည္ျခင္းသည္ ဧကန္အမွန္ေစာင့္္တည္ျခင္း၊ ကြ်ႏု္ပ္၏ဝတ္ျပဳ ဆုေတာင္းမႈမ်ားသည္ ဧကန္အမွန္ေတာင္းဆုေခြ်ျခင္းသည္ ျခင္းသည္ ဧကန္အမွန္ေတာင္းဆုျပဳ ျခင္း၊ ဂရုမမႈေသာအိပ္စက္ျခင္းမွကြ်ႏု္ပ္ကို ႏိႈးထေစၿပီး ကြ်ႏု္ပ္၏ အျပစ္မ်ားကို ခြင့္လြတ္ေပးရန္ ေတာင္းဆိုမႈျပဳပါ၏၊ ဤကမာၻေလာကကို ဖန္ဆင္းေသာ ဖန္ဆင္းရွင္အလႅာလ္ရွင္ျမတ္ ကြ်ႏု္ပ္ကိုခြင့္လြတ္ေပးပါ အလႅာလ္ရွင္ျမတ္သာလ်ွင္ အျပစ္သားမ်ားကိုခြင့့္လြတ္ႏုိင္သူ့ပါ။",
            dua_en="Lord! Make my fast in it one of those who truly fast, my prayers those of who truly pray, and awaken me from the sleep of the inattentive, grant me forgiveness for my sins in it, O Lord of the Worlds, and do forgive me, O One Who forgives criminals.",
            dua_ar="اَللّـهُمَّ اجْعَلْ صِيامي فيهِ صِيامَ الصّائِمينَ، وَقِيامي فيهِ قيامَ الْقائِمينَ، وَنَبِّهْني فيهِ عَنْ نَوْمَةِ الْغافِلينَ، وَهَبْ لى جُرْمي فيهِ يا اِلـهَ الْعالَمينَ، وَاعْفُ عَنّي يا عافِياً عَنْ الْمجْرِمينَ ."),
        2: dict(
            dua_mm="အိုအလႅာလ္အရွင္ျမတ္ မပာာဂရုဏာရွင္ အရွင့္၏သနားညွာတာမႈႏွင့္ ကြ်ႏု္ပ္၏သည္အရွင့္၏ဂရုဏာေတာ္ႏွင့္ အတူဖတ္ရြတ္ေသာ က်မ္းစာပိုဒ္ရြတ္ဆိုျခင္း ကိုလက္ခံေတာ္မႈပါ ၊ အရွင့္၏ အမ်က္ေဒါသႏွင့္ စိတ္ဆိုးေစမႈ မ်ားမွာ ကြ်ႏု္ပ္ကိုဖယ္ရွားေပးပါ။ကြ်ႏု္ပ္ကို သင္၏ႏွစ္လိုဖြယ္ေကာင္းေသာေပ်ာ္ရႊင္မႈဆီသို ့ကြ်ႏု္ပ္ကို ေဆာင္ၾကဥ္ေပးပါ။",
            dua_en="Lord! Bring me closer in it to Your pleasure, enable me in it to avoid Your anger and wrath, enable me to be in it to recite Your verses with Your mercy, O most merciful of those who have mercy!",
            dua_ar="اَللّـهُمَّ قَرِّبْني فيهِ اِلى مَرْضاتِكَ، وَجَنِّبْني فيهِ مِنْ سَخَطِكَ وَنَقِماتِكَ، وَوَفِّقْني فيهِ لِقِرآءَةِ آياتك بِرَحْمَتِكَ يا اَرْحَمَ الرّاحِمينَ"),
        3: dict(
            dua_mm="အိုအလႅာလ္အရွင္ျမတ္အရွင္ျမတ္သည္သေဘာထားႀကီးႏိုင္ဆံုးေသာသူျဖစ္ၿပီးအရွင့္၏အလြန္တရာ ရက္ေရာမႈျဖင့္ ေပးပို ့ေသာ ေကာင္းမႈ အရာခပ္သိမ္း ကို ကြ်ႏု္ပ္အတြက္လဲမွ်ေဝေပးသနားေတာ္ၿပီး ၊ အနတၱ ႏွင့္အဆိပ္ (လ်ိွဝွက္မႈ) မ်ားကေနကြ်ႏု္ပ္ကိုဖယ္ရွားေပးပါ၊ကြ်ႏု္ပ္ကို သတိ တရားႏွင့္ အသိတရားကို လဲေပးသနားေတာ္မူပါ။",
            dua_en="Lord! Grant me in it intelligence and attentiveness, distance me in it from nonsense and concealment, allot for me a portion of everything good which You send down in it with Your generosity, O most generous One!",
            dua_ar="اَللّـهُمَّ ارْزُقْني فيهِ الذِّهْنَ وَالتَّنْبيهَ ، وَباعِدْني فيهِ مِنَ السَّفاهَةِ وَالَّتمْويهِ ، وَاجْعَلْ لى نَصيباً مِنْ كُلِّ خَيْر تُنْزِلُ فيهِ، بِجُودِكَ يا أجود الاْجْوَدينَ"),
        4: dict(
            dua_mm="အိုအလႅာလ္အရွင္ျမတ္ အရွင့္၏ အမိန္ ့မ်ားကို နာခံနိုင္ရန္အတြက္ကြ်ႏ္ုပ္ကို စြမ္းေဆာင္ရည္မ်ား ေပးသနားေတာ္မူ ပါ ၊ အရွင့္၏ နာမေတာ္ေဖာ္က်ဴးျခင္းျဖင့္ ကြ်ႏု္ပ္၏ ခ်ိဳၿမိန္မႈမ်ားကိုလက္ခံေတာ္မူပါ၊အရွင့္၏ ရက္ေရာမႈ ႏွင့္အတူ ကြ်ႏု္ပ္၏ စစ္မွန္ေသာေက်းဇူးေတာ္ကိုလက္ခံေပးပါ၊ အရွင့္၏ အရာခပ္သိမ္းျမင္ႏုိင္စြမ္းျဖင့္ ကြ်ႏု္ပ္ကို ၾကည့္ရႈေစာင့္ေလ်ွာက္ ကာကြယ္ေပးသနားေတာ္မႈပါ။",
            dua_en="Lord! Strengthen me in it to perform Your commands, enable me in it to taste the sweetness of mentioning Your Name, enable me in it to truly thank You with Your generosity, and safeguard me in it with Your safeguard and cover, O most seeing One!",
            dua_ar="اَللّـهُمَّ قَوِّني فيهِ عَلى إقامة أمرك، وأذقني فيهِ حَلاوَةَ ذِكْرِكَ، وَاَوْزعْني فيهِ لاِداءِ شُكْرِكَ بِكَرَمِكَ، وَاحْفَظْني فيهِ بِحِفْظِكَ وَسَتْرِكَ، يا أبصر النّاظِرينَ"),
        5: dict(
            dua_mm="အိုအလႅာလ္အရွင္ျမတ္ မပာာဂရုဏာရွင္ ကြ်ႏု္ပ္ကို အရွင့္၏ အသနားေတာ္ေတာင္းခံသူမ်ားအနက္ မွ တစ္ေယာက္အျဖစ္ လက္ခံေတာ္မူပါ၊ ကြ်ႏု္ပ္ကိုအရွင့္၏ ေျဖာင့္မတ္မွန္ကန္ေသာ ၊ ႏွစ္လိုဖြယ္ေကာင္းေသာ အမိန္ ့နာခံသူတစ္ေယာက္အျဖစ္ လက္ခံ ေတာ္မူပါ၊ ကြ်ႏု္္ပ္ကို အရွင့္၏ေမတၱာျဖင့္ ရင္းႏွီးေသာ အေဆြေတာ္တစ္ေယာက္အျဖင့္ လက္ခံေပးေတာ္မူပါ။",
            dua_en="Lord! Enable me in it to be among those who seek Your forgiveness, make me in it among Your righteous and adoring servants, and enable me to be one of Your close friends through Your compassion, O most merciful One!",
            dua_ar="اَللّـهُمَّ اجْعَلْني فيهِ مِنْ الْمُسْتَغْفِرينَ، وَاجْعَلْني فيهِ مِنْ عِبادِكَ الصّالِحينَ اْلقانِتينَ ، وَاجْعَلني فيهِ مِنْ اَوْلِيائِكَ الْمُقَرَّبينَ، بِرَأْفَتِكَ يا اَرْحَمَ الرّاحِمينَ"),
        6: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အရွင့္၏ ကန္ ့သတ္ခ်က္မ်ားကို ေက်ာ္လြန္ၿပီး ေလာကစည္းကမ္းမ်ားကို ေဖာက္ဖ်က္ခဲ့လ်ွင္ ကြ်ႏု္ပ္ကို စြန္ ့ပစ္ျခင္း မႈ မျပဳလုပ္ပါ နဲ ့၊ အရွင့္၏ ေဒါသႏွင္တံ ႏွင့္ ကြ်ႏု္ပ္ကို မႏွင္ပါနဲ ့၊ အရွင့္၏ ကူညီမႈ ၊ အခြင့္အေရးေပးမႈ ျဖင့္ အရွင္္ျမတ္ကိုအျမတ္ေဒါသ ကိုျဖစ္ေစႏိုင္ ေသာအေၾကာင္းအရာ လုပ္ေဆာင္ခ်က္မ်ား မွ ကြ်ႏု္ပ္ကို ဖယ္ရွားေပးေတာ္မူပါ၊",
            "dua_en": "Lord! Do not abandon me in it when I am exposed to transgressing Your limits, do not whip me with the whips of Your wrath, keep me away from whatever brings about Your anger with Your boons and assistance, O One Who is the ultimate end of the desirous.",
            "dua_ar": "اللّـهُمَّ لا تَخْذُلْني فيهِ لِتَعَرُّضِ مَعْصِيَتِكَ، وَلا تَضْرِبْني بِسِياطِ نَقِمَتِكَ، وَزَحْزِحْني فيهِ مِنْ مُوجِباتِ سَخَطِكَ ، بِمَنِّكَ وأياديك يا مُنْتَهى رَغْبَةِ الرّاغِبي"
        },
        7: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အရွင္ျမတ္သည္ လမ္းေၾကာင္းေသြဖယ္ေနသူမ်ားကို တည့္မတ္ေပးနိုင္သူ ၊ အရွင္၏ ေထာက္ပံ့ မႈ ႏွင့္ အတူကြ်ႏု္ပ္ သည္ အရွင္ကို အစဥ္အျမဲသတိရမႈကို လက္ခံေပးပါ၊ ကြ်ႏု္ပ္၏ ေပါ့ဆမႈ မ်ား ၊ အျပစ္မ်ား မွ ကူညီဖယ္ရွားေပးပါ ၊ ကြ်ႏ္ုပ္ ၏ ဥပုပ္သီလ တည္ေစာင့္မႈ ႏွင့္ ေတာင္းဆု ေခြ်မႈ မ်ားကို အက်ိဳးအရိွဆံုး အျဖစ္ အကူအညီေပးေတာ္မူပါ။",
            "dua_en": "Lord! Help me in it to fast and to pray as it is worth, help me avoid its slips and sins, and grant me in it to continuously remember You with Your enabling, O One Who guides those who stray!",
            "dua_ar": "اَللّـهُمَّ اَعِنّي فِيهِ عَلى صِيامِهِ وَقِيامِهِ، وَجَنِّبْني فيهِ مِنْ هَفَواتِهِ وَآثامِهِ، وَارْزُقْني فيهِ ذِكْرَكَ بِدَوامِهِ، بِتَوْفيقِكَ يا هادِيَ الْمُضِلّي"
        },
        8: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အရွင္ျမတ္သည္ သာလွ်င္ ေမ်ွာ္လင့္ခ်က္ ၊ အရွင့္၏ အလို ျဖင့္သာ ကြ်ႏ္ုပ္သည္မိဘမဲ့ကေလးမ်ားကို အစားအေသာက္မ်ား မ်ွေဝ ေပးႏိုင္ရန္ ၊ၿငိမ္းခ်မ္းေရး တရားမ်ားကို ျပန္လည္ လက္ဆင့္ကမ္း ျဖန္ ့ျဖဴးႏိုင္ ရန္ ႏွင့္ ေကာင္းမႈ မ်ားတြင္ ပါဝင္လိုက္ႏိုင္ရန္ ျဖစ္ေသာေၾကာင့္ကြ်ႏု္ပ္၏ ဂရုဏာ ေတာ္ကို လက္ခံေပးသနားေတာ္မူပါ။",
            "dua_en": "Lord! Grant me in it mercy due to orphans, to be able to give away food, to disseminate the peace, to accompany the good ones through Your own favors, O haven of the hopeful!",
            "dua_ar": "اَللّـهُمَّ ارْزُقْني فيهِ رَحْمَةَ الأيتام، وإطعام اَلطَّعامِ، وإفشاء السَّلامِ، وَصُحْبَةَ الْكِرامِ، بِطَولِكَ يا ملجأ الآملين"
        },
        9: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အရွင္ျမတ္သည္သာလွ်င္ စိတ္ခြန္းအားထက္သန္စြာႏုိင္ေသာေမွ်ာ္လင့္ခ်က္ တစ္ခု ပါ၊ အရွင့္္၏ စုစည္းသာယာမႈမ်ားရရိွသည့္အခါ အရွင့္ ၏ခ်စ္ျခင္းျဖင့္ ကြ်ႏု္ပ္ နဖူးေရွ ့စြန္းကို ယူပါ၊ အရွင့္၏ ေတာက္ပေနေသာ သက္ေသအေထာက္အထားမ်ားဆီသို ့ကြ်ႏု္ပ္ကိုေခၚေဆာင္သြားပါ၊ အရွင့္၏ တန္းဖိုးျဖတ္၍မရႏုိင္ေသာ မပာာဂရုဏာေတာ္မ်ားကို ကြ်ႏု္ပ္ကို ခဲြေဝေပးသနားေတာ္မူပါ၊",
            "dua_en": "Lord! Allot for me in it a portion of Your spacious mercy, guide me in it to Your glittering proofs, take my forelock to whatever achieves Your collective Pleasure through Your love, O hope of the eager ones!",
            "dua_ar": "اللّـهُمَّ اجْعَلْ لي فيهِ نَصيباً مِنْ رَحْمَتِكَ الْواسِعَةِ، وَاهْدِني فيهِ لِبَراهينِكَ السّاطِعَةِ، وَخُذْ بِناصِيَتي اِلى مَرْضاتِكَ الْجامِعَةِ، بِمَحَبَّتِكَ يا أمل الْمُشْتاقي"
        },
        10: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလၻာရွင္ျမတ္ကို အဆံုးမဲ့ ရွာေဖြသူမ်ား ထဲမွ အရွင့္၏ ရင္းႏွီးမႈ ရိွသူမ်ားအနက္မွတစ္ေယာက္အျဖင့္၊ေအာင္ျမင္မႈရရိွသူမ်ားအနက္မွ တစ္ေယာက္ အျဖင့္ ၊ အရွင့္အားမွီခိုသူမ်ားအနက္မွ တစ္ေယာက္အျဖင့္ အရွင့္၏ ၾကင္နာမႈ ႏွင့္အတူ ကြ်ႏု္ပ္ကို လက္ခံေပးပါ၊",
            "dua_en": "Lord! Make me in it among those who depend on You, make me in it among the winners, and make me in it among those who are close to You with Your kindness, O ultimate end of the seekers!",
            "dua_ar": " اَللّـهُمَّ اجْعَلْني فيهِ مِنَ الْمُتَوَكِّلينَ عَلَيْكَ، وَاجْعَلْني فيهِ مِنَ الْفائِزينَ لَدَيْكَ، وَاجْعَلْني فيهِ مِنَ الْمُقَرَّبينَ اِلَيْكَ، بإحسانك يا غايَةَ الطّالِبي"
        },
        11: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ အသနားခံမႈ ကို ေျဖေလ်ာ့ေပးႏိုင္သူ ျဖစ္သည္ ၊ ထို ့ေၾကာင့္ ေဒါသမီးမ်ားမွတားျမစ္ပါ ၊ အက်င့္ပ်က္မႈ ႏွင့္ ပုန္ကန္မႈ တို ့ကို မုန္းတီးေစလို ပါ၊ ေစတနာထားမႈကို ႏွစ္သက္ေစလို ေသာ သူတစ္ဦး အျဖင့္ကြ်ႏု္ပ္ ကို အရွင့္၏ အကူအညီျဖင့္ ျပဳလုပ္ေပးပါ၊",
            "dua_en": "Lord! Make me in it love benevolence, hate immorality and rebellion, and prohibit in it anger against me and the Fires with Your assistance, O One Who brings relief to those who plead for it!",
            "dua_ar": " اَللّـهُمَّ حَبِّبْ اِلَيَّ فيهِ الإحسان، وَكَرِّهْ اِلَيَّ فيهِ الْفُسُوقَ وَالْعِصْيانَ، وَحَرِّمْ عَلَيَّ فيهِ السَّخَطَ وَالنّيرانَ بِعَوْنِكَ يا غِياثَ الْمُسْتَغيثي"
        },
        12: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္ ေၾကာက္မက္ဖြယ္ရာမ်ားကို ကာကြယ္ေပးႏုိင္သူျဖစ္သည္ ၊ထို ့ေၾကာင့္ အရွင့္၏ ဂုဏ္ေတာ္မ်ားျဖင့္ လြမ္္းျခံဳ ၿပီး ကြ်ႏု္ပ္ကို ျပဳျပင္ ေပးပါ၊ ေရာင့္ရဲတင္းတိမ္မႈ ႏွင့္ ကာကြယ္ေပး ပါ၊ မွ်တမႈ ႏွင့္ တရားရိွမႈ တို ့ကို ေထာက္ကူေပးပါ၊ ေၾကာက္ရြံ ့ေသာစိတ္မွ လံႈျခံဳ မႈ ဆီသို ့အရွင့္၏ ကာကြယ္ေပး မႈ ႏွင့္ အတူ ေခၚေဆာင္ေပးေတာ္မူ ပါ။",
            "dua_en": "Lord! Decorate me in it with a covering and with honors, shield me in it with the outfit of contentment and sufficiency, enable me in it to be just and fair, and bring me in it security against what I fear with Your protection, O Protector of the fearful!",
            "dua_ar": "اَللّـهُمَّ زَيِّنّي فيهِ بِالسِّتْرِ وَالْعَفافِ، وَاسْتُرْني فيهِ بِلِباسِ الْقُنُوعِ وَالْكَفافِ، وَاحْمِلْني فيهِ عَلَى الْعَدْلِ والإنصاف، وَآمِنّي فيهِ مِنْ كُلِّ ما أخاف، بِعِصْمَتِكَ يا عِصْمَةَ الْخائِفي"
        },
        13: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ကြ်ႏု္ပ္ကို ညစ္ညဴးေသာ မသန္ ့ရွင္းမႈ မ်ား မွ စင္ၾကယ္ေစေတာ္မူ ပါ ၊ မည္ကဲ့သို ့ေသာ ကံၾကမၼာ ၾကံဳလာပါက သည္းခံႏုိင္စြမ္း ကြ်ႏု္ပ္ကို ေပးသနားေတာ္မူပါ ၊တရားနည္းလမ္းက်စြာ ၾကင္နာမႈတစ္ခု အတြက္ကြ်ႏု္ပ္ပါဝင္ ၿပီး ေအာင္ျမင္မႈ တစ္ခု ကို အရွင့္၏ အကူအညီျဖင့္ေပးသနားေတာ္မူပါ၊",
            "dua_en": "Lord! Purify me in it from uncleanness and filth, enable me in it to be patient about whatever the fates bring, grant me success in it for righteousness and for the company of the kind ones with Your assistance, O apple of the eyes of the indigent!",
            "dua_ar": "اَللّـهُمَّ طَهِّرْني فيهِ مِنَ الدَّنَسِ والأقذار، وَصَبِّرْني فيهِ عَلى كائِناتِ الأقدار، وَوَفِّقْني فيهِ لِلتُّقى وَصُحْبَةِ الأبرار، بِعَوْنِكَ يا قُرَّةَ عَيْنِ الْمَساكينَ"
        },
        14: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ မြတ္စလင္မ်ား၏ ဂုဏ္သိကၡာကို လံႈျခံဳမႈ ေပးႏုိင္သူတစ္ဦးျဖစ္သည္၊ ကြ်ႏု္ပ္ ေပါ့ဆ မႈျပဳလုပ္ခဲ့လွ်င္ အရွင္ အျပစ္ မျမင္ ပါနဲ ့၊ ေပါ့ဆ မႈျဖစ္ေသာ အျပစ္ျဖစ္ေစေသာ အရာမ်ား မွ ကြ်ႏု္ပ္ကို ကာကြယ္ေပး ပါ၊စမ္းသပ္မႈ ျဖစ္ေသာ ဆင္းရဲ ဒုကၡ ကို အရွင့္၏ ႀကီးမားေသာ ဂုဏ္သိကၡာျဖင့္ ရည္ရြယ္မႈ မျပဳလုပ္ပါနဲ ့",
            "dua_en": "Lord! Do not penalize me in it when I slip, protect me in it from sinning and slipping, and do not be an object to trials and tribulations with Your Dignity, O One Who safeguards the dignity of the Muslims!",
            "dua_ar": "اَللّـهُمَّ لا تُؤاخِذْني فيهِ بِالْعَثَراتِ، وَاَقِلْني فيهِ مِنَ الْخَطايا وَالْهَفَواتِ ، وَلا تَجْعَلْني فيهِ غَرَضاً لِلْبَلايا والآفات، بِعِزَّتِكَ يا عِزَّ الْمُسْلِمي"
        },
        15: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ ေၾကာက္ရံြ ့မႈမ်ား မွ လံႈျခံဳမႈသို့သယ္ေဆာင္ႏိုင္သူျဖစ္သည္၊ ကြ်ႏု္ပ္၏ ရိုးသားျဖဴစင္ ၿပီး အမိန္ ့နာခံသူတစ္ေယာက္အျဖစ္၊ အရွင္အား စြန္ ့ခြာ သြားသူမ်ား ျဖစ္ခဲ့ပါက အရွင့္၏ လံႈျခံဳ မႈ ျဖင့္အရွင့္ထံ ႏွလံုးသားဖြင့္ၿပီး ျပန္လာႏိုင္သူ အျဖစ္ လက္ခံေတာ္မူပါ။",
            "dua_en": "Lord! Grant me in it the obedience of the devout, expand my chest in it with the return to You of those who abandoned You, through Your security, O One Who brings security to the fearful!",
            "dua_ar": "اَللّـهُمَّ ارْزُقْني فيهِ طاعَةَ الْخاشِعينَ، وَاشْرَحْ فيهِ صَدْري بإنابة الْمخْبِتينَ، بأمانك يا أمان الْخائِفينَ"
        },
        16: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ ဤေလာက၏ အရွင္သခင္ျဖစ္ေတာ္မူ သည္။ ကြ်ႏု္ပ္ အား ၾကင္နာကတိတည္သူ တစ္ေယာက္ အျဖင့္၊ မေကာင္းေသာ/ယုတ္မာေသာသူမ်ား ႏွင့္ အေပါင္းအသင္း ျဖစ္ျခင္းမွ ဖယ္ရွားေပးပါ၊ အရွင့္၏ မပာာဂရုဏာေတာ္ျဖင့္ ဂ်ဒ္နဒ္ သုခဘံု သို ့အရွင့္ ၏အဆံုးမရိွေသာ ဂုဏ္ေတာ္မ်ား နွင့္အတူ ဝင္ေရာက္ခြင့့္ျပဳပါ။",
            "dua_en": "Lord! Grant me success in it to be in agreement with the kind ones, enable me in it to avoid the company of evildoers, enable me in it with Your mercy to be lodged in the abode of eternity with Your Godhead, O Lord of the Worlds!",
            "dua_ar": "اَللّـهُمَّ وَفِّقْني فيهِ لِمُوافَقَةِ الأبرار، وَجَنِّبْني فيهِ مُرافَقَةَ الأشرار، وَآوِني فيهِ بِرَحْمَتِكَ اِلى دارِ الْقَـرارِ، بإلهيّتك يا اِلـهَ الْعالَمي"
        },
        17: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ ကြ်ႏု္ပ္ကို ေကာင္းမႈ ကုသိုိလ္ မ်ားျပဳလုပ္ရန္အတြက္ လမ္းညႊန္ျပသေတာ္မူပါ၊ လိုအပ္ခ်က္မ်ားကို ျဖည့္ဆည္းေပးလို ေသာဆႏၵမ်ားကို ကြ်ႏု္ပ္ကို မွ်ေဝေပးပါ ၊ မည္သူမွွ် ရွင္းျပရန္ ၊ ေမးျမန္းရန္ လိုအပ္ျခင္းမရိွသည့္ ေလာကကို နက္နက္နဲနဲ သိျမင္ႏိုင္စြမ္းရိွေသာ ေက်းဇူးေတာ္ရွင္ တမန္ေတာ္ မုပာမၼဒ္၏ ခ်ီးက်ဴးမႈျဖင့္ ကြ်ႏု္ပ္ ကို လက္ခံေပးေတာ္မူပါ၊",
            "dua_en": "Lord! Grant me in it guidance to do good deeds, allot for me in it the fulfillment of needs and of aspirations, O One Who needs no explanation or queries, the One Who knows the innermost of the worlds, bless Muhammed and his pure Progeny!",
            "dua_ar": "اَللّـهُمَّ اهْدِني فيهِ لِصالِحِ الإعمال، وَاقْضِ لي فيهِ الْحَوائِجَ والآمال، يا مَنْ لا يَحْتاجُ اِلَى التَّفْسيرِ وَالسُّؤالِ، يا عالِماً بِما في صُدُورِ الْعالَمينَ، صَلِّ عَلى مُحَمَّد وَآلِهِ الطّاهِرينَ"
        },
        18: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ႏွလံုးသားမ်ားထံသို ့ အလင္းေရာင္ျခည္ယူေဆာင္ေပးႏိုင္ေသာသူတစ္ေယာက္ျဖစ္သည္။ အရွင့္ ၏ အလင္းေရာင္ျခည္မ်ားေနာက္သို့တေသြမသိမ္း လိုက္ပါသူတစ္ေယာက္အျဖင့္ ကြ်ႏု္ပ္အား ျပဳလုပ္ေတာ္မူပါ၊ အရွင့္၏ လင္းေရာင္ျခည္ျဖင့္သာ ကြ်ႏ္ုပ္၏ ႏွလံုးသားကို အလင္းျပေတာ္မူပါ၊ မနက္ခင္း အခ်ိန္မ်ားတြင္ အရွင့္၏ ေကာင္းခ်ီး ေပးမႈ မ်ားအား ကြ်ႏ္ုပ္ အေပၚက်ေရာက္ေစေတာ္မူပါ။",
            "dua_en": "Lord! Make me attentive in it to the blessings of his Sahar times, enlighten my heart in it with the light of its noors, make all my parts follow its tracks with Your own Noor, O One Who brings the noor (light) to the hearts of those who know You!",
            "dua_ar": "اَللّـهُمَّ نَبِّهْني فيهِ لِبَرَكاتِ أسحاره، وَنَوِّرْ فيهِ قَلْبي بِضياءِ أنواره، وَخُذْ بِكُلِّ أعضائي اِلَى إتباع آثارِهِ، بِنُورِكَ يا مُنَوِّرَ قُلُوبِ الْعارِفي"
        },
        19: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္သက္ဝင္ယံုၾကည္မႈ၏ ၿငိမ္သက္ေသာ ႏွလံုးသား မ်ားကို ပို ့ေဆာင္ႏိုင္သူျဖစ္သည္၊ကြ်ႏု္ပ္အား က်မ္းျမတ္ကုအာန္ ကိုရြတ္ဆို ႏိုင္သူတစ္ဦး အျဖင့္လက္ခံေတာ္မူပါ၊ ကြ်ႏု္ပ္ထံမွ မီးေတာက္ ဂိတ္တံခါးမ်ားကို ပိတ္ေပး ၿပီး ပန္းဥယ်ာဥ္ ဂိတ္တံခါးမ်ားကို ဖြင့္ေပးေတာ္မူပါ။",
            "dua_en": "Lord! Open for me in it the gates of the gardens, close from me in it the gates of the fires, enable me in it to recite the Qur’an, O One Who sends down calm to the hearts of the faithful!",
            "dua_ar": " اَللّـهُمَّ افْتَحْ لي فيهِ أبواب الْجِنانِ، وأغلق عَنّي فيهِ أبواب النّيرانِ، وَوَفِّقْني فيهِ لِتِلاوَةِ الْقُرْآنِ، يا مُنْزِلَ السَّكينَةِ فى قُلُوبِ الْمُؤْمِني"
        },
        20: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ အသနားခံသူ မ်ား၏လိုအပ္ခ်က္မ်ားကို ျဖည့္ဆည္းေပးႏိုင္သူတစ္ေယာက္ ျဖစ္ပါသည္ေကာင္းကင္ဘံု (ဂ်နဒ္) ကို ကြ်ႏု္ပ္ ၏ထာဝရအိမ္ေတာ္ ျဖစ္ခြင့္ေပးပါ၊ မာရ္နတ္၏ အေႏွာက္အယွက္မ်ား မွ ကင္း ေဝးရလိုပါ၏ ၊ အရွင့္၏ သာယာေပ်ာ္ရႊင္မ်ားရွာေဖြႏိုင္သူအျဖစ္ လမ္းညႊန္ ျပသေတာ္မူပါ။",
            "dua_en": "Lord! Guide me in it to earn Your Pleasure, do not let Satan find in it his way to me, and let Paradise be my home and eternal abode, O One Who fulfills the needs of those who plead!",
            "dua_ar": "اَللّـهُمَّ اجْعَلْ لى فيهِ اِلى مَرْضاتِكَ دَليلاً، وَلا تَجْعَلْ لِلشَّيْطانِ فيهِ عَلَيَّ سَبيلاً، وَاجْعَلِ الْجَنَّةَ لى مَنْزِلاً وَمَقيلاً، يا قاضِيَ حَوائِجِ الطّالِبي"
        },
        21: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ အခက္အခဲအၾကပ္အတည္း မ်ားၾကားတြင္ အရွင္၏ နာမေတာ္ ေခၚဆိုလိုက္ျခင္းျဖင့္ တံု ့ျပန္ႏိုင္စြမ္း ရိွသူျဖစ္သည္။ အရွင့္၏ ခမ္းနာထည္ဝါေသာ ဥယ်ာဥ္ကို ကြ်ႏု္ပ္၏အ္ိမ္ေတာ္ အျဖင့္၊ အရွင့္၏ သာယာ ေပ်ာ္ရႊင္ကို ရွာေဖြႏိုင္သူအျဖစ္ လက္ခံ ေတာ္မူ ပါ၊ ကြ်ႏု္ပ္ အေပၚသို ့အရွင့္၏ ခ်ီးက်ဳးမႈမ်ား က်ေရာက္ေစေတာ္မႈပါ ၊ အရွင့္၏ ႏွစ္လိုဖြယ္ေကာင္းေသာတံခါးမ်ားကို ကြ်ႏု္ပ္အတြက္ ဖြင့္လွစ္ေပးသနားေတာ္မႈပါ၊",
            "dua_en": "Lord! Open for me in it the gates of Your favor, send down to me in it Your blessings, enable me in it to earn whatever brings about Your Pleasure, house me in it in the opulence of Your gardens, O One Who responds to the call of the compelled ones!",
            "dua_ar": "اَللّـهُمَّ افْتَحْ لى فيهِ أبواب فَضْلِكَ، وَاَنْزِلْ عَلَيَّ فيهِ بَرَكاتِكَ، وَوَفِّقْني فيهِ لِمُوجِباتِ مَرْضاتِكَ، وَاَسْكِنّي فيهِ بُحْبُوحاتِ جَنّاتِكَ، يا مُجيبَ دَعْوَةِ الْمُضْطَرّينَ"
        },
        22: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ ေပါ့ဆမႈ အျပစ္မ်ားကို မွန္ကန္ေအာင္ ျပဳလုပ္ေပးႏိုင္သူျဖစ္ပါသည္။ ကြ်ႏ္ုပ္၏ ဘာသာတရားကိုင္းရိႈင္းမႈ ကို ကြ်ႏု္ပ္ ႏွလံုးသားသိရိွေစလိုပါ၏ ၊ ကြ်ႏ္ုပ္ ခြ်တ္ယြင္းခ်က္ မ်ားမွာ သန္ ့စင္ေပးေတာ္မူပါ၊ ကြ်ႏ္ုပ္၏ အျပစ္မ်ားကို ေဆးေၾကာေပးေတာ္မူပါ။",
            "dua_en": "Lord! Wash my sins away in it, purify me from defects, ascertain my heart in it with the piety of the hearts, O One Who corrects the slips of the sinners!",
            "dua_ar": " اَللّـهُمَّ اغْسِلْني فيهِ مِنَ الذُّنُوبِ، وَطَهِّرْني فيهِ مِنَ الْعُيُوبِ، وَامْتَحِنْ قَلْبي فيهِ بِتَقْوَى الْقُلُوبِ، يا مُقيلَ عَثَراتِ الْمُذْنِبي"
        },
        23: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ ေတာင္းပန္ ျခင္းကို သေဘာထားႀကီးေပးႏိုင္သူတစ္ဦးျဖစ္ပါသည္၊ ကြ်ႏု္ပ္၏အမိန္ ့မနာခံျခင္း မ်ားကို အရွင့္ ထံ ေတာင္းပန္ၿပီး အရွင့္ ၏ အမိန္ ့ကို နာခံသူ တစ္ေယာက္အျဖင့္၊ အရွင့္ အား ဆန္ ့က်င္ၿပီး ျပဳလုပ္မိေသာ အျပစ္မ်ားကို အရွင့္ ထံတြင္ ခိုလံုခြင့္ေတာင္းခံသူတစ္ေယာက္အျဖင့္၊ အရွင့္အား ႏွစ္လိုဖြယ္ေစႏိုင္ေသာအရာမ်ားကို စြမ္းေဆာင္ ႏိုင္သူ တစ္ေယာက္ အျဖစ္ ကြ်ႏု္ပ္ အသနားခံမႈ ကို လက္ခံေပး ေတာ္မူပါ။",
            "dua_en": "Lord! I plead to You to enable me to achieve whatever pleases You, I seek refuge with You from whatever offends You, and I plead to You to grant me the ability to obey You and not to disobey, O most Generous One of all those to whom pleas are made!",
            "dua_ar": "  اَللّـهُمَّ إني أسألك فيهِ ما يُرْضيكَ، وأعوذ بِكَ مِمّا يُؤْذيكَ، وأسألك التَّوْفيقَ فيهِ لاِنْ أطيعك وَلا أعصيك، يا جَوادَ السّائِلينَ"
        },
        24: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ တမန္ေတာ္၏ ႏွလံုးသားမ်ားကို ကာကြယ္ေပးႏိုင္သူတစ္ဦးျဖစ္ပါသည္။ အရွင့္ တမန္ေတာ္မ်ား၏ တံဆိပ္ေတာ္ျဖစ္ေသာ စြန္နတ္ဒ္ ေတာ္မ်ားကို လိုက္နာႏိုင္သူ အျဖင့္၊ ကြ်ႏ္ုပ္အား ဆန္ ့က်င္ မုန္းတီးသူမ်ားကို မိတ္ေဆြကဲ့သို ့ခ်စ္ခင္ႏိုင္စြမ္း အရွင္ျပဳလုပ္ေပးေတာ္မူပါ။",
            "dua_en": "Lord! Make me in it one who loves Your friends, who is hostile to Your foes, following the Sunnah of the Seal of Your Prophets, O One Who protects the prophets’ hearts!",
            "dua_ar": " اَللّـهُمَّ اجْعَلْني فيهِ مُحِبَّاً لأوليائك، وَمُعادِياً لأعدائك، مُسْتَنّاً بِسُنَّةِ خاتَمِ أنبيائك، يا عاصِمَ قُلُوبِ النَّبِيّينَ"
        },
        25: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ ေတာင္းပန္ျခင္း ကိုၾကားရိွႏိုင္စြမ္းရိွသူတစ္ဦးျဖစ္ပါသည္၊ ကြ်ႏု္ပ္ ျပဳလုပ္ေသာ ေကာင္းမႈကုသိုလ္မ်ားကို က်ဴးလြန္ခဲ့မိေသာအျပစ္ မ်ားနွင့္ ေပးေခ်ခြင့္ကို လက္ခံေတာ္ မူပါ ၊ ကြ်ႏု္ပ္၏အျပစ္မ်ားကို ခြင့္လြတ္ေတာ္မူပါ ၊ ကြ်ႏ္ုပ္၏ ႀကိဳးစားအားထုတ္မႈမ်ားကို ခ်ီးၾကဴးေထာပနာ ျပဳေတာ္မူပါ၊",
            "dua_en": "Lord! Make my endeavor in it appreciated (by You), my sin it forgiven, my deed in it accepted, my defect in it covered, O most hearing of those who hear (pleas)!",
            "dua_ar": "اَللّـهُمَّ اجْعَلْ سَعْيي فيهِ مَشْكُوراً، وَذَنْبي فيهِ مَغْفُوراً وَعَمَلي فيهِ مَقْبُولاً، وَعَيْبي فيهِ مَسْتُوراً، يا اَسْمَعَ السّامِعينَ"
        },
        26: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ အရွင့္၏ နည္းလမ္းတက် အမိန္ ့နာခံသူမ်ားကို ၾကင္နာသူတစ္ဦးျဖစ္ပါသည္၊ ကြ်ႏ္ုပ္ ၏ ဆင္ေျခမ်ား ၊ အျပစ္မ်ား ၊ ဝန္ထုပ္ဝန္ပိုးမ်ားကို ဖယ္ရွားေပးေတာ္ မူပါ၊ ကြ်ႏ္ုပ္ ၏အခက္အခဲမ်ားကို လြယ္ကူေခ်ာေမြ ့မႈ အျဖစ္ သို ့ေျပာင္းလဲေပးေတာ္မူပါ၊ ယေန ့က်ေရာက္ေသာ လိုက္လာသြလ္ ကာရ္ဒလ္ ညျမတ္၏ ေက်းဇူး ဂုဏ္ေတာ္မ်ားကို ကြ်ႏု္ပ္အားေပးသနားေတာ္မူပါ။",
            "dua_en": "Lord! Grant me in it the honor of Laylatul-Qadr, change my affairs in it from hardship to ease, accept my excuses, remove from the sin and its burden, O One Who is affectionate towards His righteous servants!",
            "dua_ar": "اَللّـهُمَّ ارْزُقْني فيهِ فَضْلَ لَيْلَةِ الْقَدْرِ، وَصَيِّرْ أموري فيهِ مِنَ الْعُسْرِ إلى الْيُسْرِ، وَاقْبَلْ مَعاذيري، وَحُطَّ عَنّيِ الذَّنْبَ وَالْوِزْرَ، يا رَؤوفاً بِعِبادِهِ الصّالِحي"
        },
        27: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ စိတ္္အာရံုပ်ံ ့လြင့္ ျခင္း မရိွေအာင္ ဇဲြေကာင္းေအာင္ျပဳလုပ္စြမ္း ရိွသူ တစ္ဦးျဖစ္ပါသည္။ အရွင့္ ၏ လမ္းစဥ္ မ်ားအနက္ မွ ကြ်ႏု္ပ္ ကို အရွင့္ ထံ အနီးဆံုး ေရာက္ရွိႏုိင္မည့္ လမ္းစဥ္ ျဖင့္ ကြ်ႏ္္ုပ္အား ေခၚေဆာင္ ေတာ္မူပါ ၊ ဖတ္ရြတ္ေသာ နဖိလ္ ဆြလာသ္ ျဖင့္ ေကာင္းမႈ ကုသိုလ္ ၾကြယ္ဝမႈ ကို ကြ်ႏု္ပ္၏ ေတာင္းပန္ ျခင္းႏွင့္ အတူ အရွင့္ ေပးသနားေတာ္မူပါ။",
            "dua_en": "Lord! Make my lot of Nafl (supererogatory) deeds in it abundant, honor me in it with the presence of pleas, bring my means towards You closer from among all means, O One Who is not distracted by the persistence of those who persist!",
            "dua_ar": "اَللّـهُمَّ وَفِّرْ حَظّي فيهِ مِنَ النَّوافِلِ، وأكرمني فيهِ بإحضار الْمَسائِلِ، وَقَرِّبْ فيهِ وسيلتي إليك مِنْ بَيْنِ الْوَسائِلِ، يا مَنْ لا يَشْغَلُهُ إلحاح الْمُلِحّينَ"
        },
        28: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ အရွင့္ အား ယံုၾကည္သက္ဝင္ အမိန္ ့နာခံသူမ်ားကို မပာာဂရုဏာေတာ္ သက္ေရာက္ေစသူျဖစ္ပါသည္၊ ကြ်ႏ္ုပ္ ၏ႏွလံုသား ထဲမွ နက္နဲေသာ အျပစ္မ်ားကို သန္ ့စင္ ေပးေတာ္မူပါ၊ ကာကြယ္မႈ နွင့္ အတူ ေအာင္ျမင္မႈ ေပးသနားေတာ္မူ ပါ၊ အရွင့္ ၏ မပာာဂရုဏာေတာ္မ်ားျဖင့္ ကြ်ႏု္ပ္အား လြမ္းျခံဳေစေတာ္မူပါ။",
            "dua_en": "Lord! Overwhelm me in it with (Your) mercy, grant me in it success and protection, purge my heart of the depths of accusation, O most Merciful One of His believing servants!",
            "dua_ar": "اَللّـهُمَّ غَشِّني فيهِ بِالرَّحْمَةِ ، وَارْزُقْني فيهِ التَّوْفيقَ وَالْعِصْمَةَ ، وَطَهِّرْ قَلْبي مِنْ غَياهِبِ التُّهْمَةِ ، يا رَحيماً بِعِبادِهِ الْمُؤْمِني"
        },
        29: {
            "dua_mm": "အိုအလႅာလ္အရွင္ျမတ္ အလႅာလ္အရွင္ျမတ္သည္သာလွ်င္ ကမာၻေလာကကို ပိုင္ဆိုင္ေတာ္မူေသာ အရွင္ ျဖစ္ပါသည္။ ကြ်ႏ္ုပ္သည္ ဥပုဒ္သီလေစာင့္တည္ျခင္း အတြက္အရွင့္ လက္ခံေသာအရာမ်ား ၊ တမန္ေတာ္ မုပာမၼဒ္(SWT) လက္ခံေသာ ေသာ နည္းလမ္းမ်ား ခ်မွတ္ထားေသာ လမ္းစဥ္မ်ားကို လက္ဆင့္ကမ္း ေဆာင္ရြက္ေစမႈမ်ား၏ ေက်းဇူးေတာ္မ်ားကို ကြ်ႏု္ပ္အားေပးသနားေတာ္မူပါ။",
            "dua_en": "Lord! Make my fast in it a means to thanking You and to accepting what You accept and what the Messenger () accepts, its branches perfected through its principles, by the right of our Master Muhammed and his Pure Progeny, and all praise belongs to Allah, Lord of the Worlds.",
            "dua_ar": "اَللّـهُمَّ اجْعَلْ صِيامى فيهِ بِالشُّكْرِ وَالْقَبُولِ عَلى ما تَرْضاهُ وَيَرْضاهُ الرَّسُولُ، مُحْكَمَةً فُرُوعُهُ بِالاْصُولِ، بِحَقِّ سَيِّدِنا مُحَمَّد وَآلِهِ الطّاهِرينَ، وَالْحَمْدُ للهِ رَبِّ الْعالَمي"
        },
        30: {
            "dua_mm": "",
            "dua_en": "",
            "dua_ar": ""
        }
    }[x]


def get_mm_num(num):
    mm_digit = ""
    for c in range(len(str(num))):
        mm_digit += mm_num(int(str(num)[c]))
    return mm_digit


def gen_seeds():
    import uuid
    from database import db_session
    from manage import Country, State, Day

    state_arr = ["ရန်ကုန်တိုင်း", "မန္တလေးတိုင်း", "ဧရာဝတီတိုင်း", "မကွေးတိုင်း", "စစ်ကိုင်းတိုင်း", "တင်္နသာရီတိုင်း",
                 "ပဲခူးတိုင်း", "ကချင်ပြည်နယ်", "ချင်းပြည်နယ်", "ရခိုင်ပြည်နယ်", "ရှမ်းပြည်နယ်", "ကယားပြည်နယ်",
                 "ကရင်ပြည်နယ်", "မွန်ပြည်နယ်"]
    # for s in source_arr:
    print("Generating Country.......\n\n\n")
    country_id = str(uuid.uuid4().hex)

    country = Country(id=country_id, object_id=country_id,
                      name=str(s["name"]))
    db_session.add(country)
    db_session.commit()

    if os.environ["ENV"] != 'production':
        for state in state_arr:
            print("Generating State.........\n\n")
            issue_id = str(uuid.uuid4().hex)
            issue = State(id=issue_id, object_id=issue_id, country_id=str(country.object_id),
                          name_mm_uni=str(state),
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
                              sehri_time_desc="Sehri",
                              sehri_time_desc_mm_zawgyi=Rabbit.uni2zg(
                                  "ဝါချည်ချိန်"),
                              sehri_time_desc_mm_uni="ဝါချည်ချိန်",
                              iftari_time="7:3" + str(art) + " pm",
                              dua_mm_uni=Rabbit.zg2uni(
                                  str(daily_dua(art)["dua_mm"])),
                              dua_mm_zawgyi=daily_dua(art)["dua_mm"],
                              dua_ar=daily_dua(art)["dua_ar"],
                              dua_en=daily_dua(art)["dua_en"],
                              iftari_time_desc="Iftari",
                              iftari_time_desc_mm_zawgyi=Rabbit.uni2zg(
                                  "ဝါဖြေချိန်"),
                              iftari_time_desc_mm_uni="ဝါဖြေချိန်"
                              )
                db_session.add(article)
                db_session.commit()

                for art in range(1, 31):
                    print("Generating Days.......\n")
                    article_id = str(uuid.uuid4().hex)
                    article = Day(id=article_id, object_id=article_id,
                                  country_id=str(country.object_id),
                                  state_id=str(issue.object_id),
                                  day=art, day_mm=str(get_mm_num(art)), sehri_time="4:3" + str(art) + " am",
                                  sehri_time_desc="Sehri",
                                  sehri_time_desc_mm_zawgyi=Rabbit.uni2zg(
                                      "ဝါချည်ချိန်"),
                                  sehri_time_desc_mm_uni="ဝါချည်ချိန်",
                                  iftari_time="7:3" + str(art) + " pm",
                                  dua_mm_uni=Rabbit.zg2uni(
                                      str(daily_dua(art)["dua_mm"])),
                                  dua_mm_zawgyi=daily_dua(art)["dua_mm"],
                                  dua_ar=daily_dua(art)["dua_ar"],
                                  dua_en=daily_dua(art)["dua_en"],
                                  iftari_time_desc="Iftari",
                                  iftari_time_desc_mm_zawgyi=Rabbit.uni2zg(
                                      "ဝါဖြေချိန်"),
                                  iftari_time_desc_mm_uni="ဝါဖြေချိန်"
                                  )
                    db_session.add(article)
                    db_session.commit()


if __name__ == "__main__":
    gen_seeds()
