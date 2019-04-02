import json

# !!!!!!USE HALF-WIDTH PUNCTUATIONS!!!!!!
# !!!!!!DO NOT MODIFY THIS FILE IN THE REPO,
#       MAKE A COPY AS "record_generate_copy.py" INSTEAD!!!!!!

model = {
    # name of bus route in the red part of the board,
    # e.g. "612","通勤班车","360快"
    'name': '',
    # departure stop on the board in simplified Chinese,
    # e.g. "北官厅"
    'from_stop_zh': '',
    # departure stop on the board in pinyin(space ignored),
    # e.g. "BEIGUANTING"
    'from_stop_pinyin': '',
    # terminal stop on the board in simplified Chinese,
    # e.g. "张仪村南站"
    'to_stop_zh': '',
    # terminal stop on the board in pinyin(space ignored),
    # e.g. "ZHANGYICUNNANZHAN"
    'to_stop_pinyin': '',
    # schedule of bus on the board(space ignored,"营业时间" ignored(if exist)),
    # transform schedule to the formats below:
    # 1) "6:40-23:00" (consecutive)
    # 2) "6:30,9:30,13:00,16:00" (discrete)
    # 3) "7:00-9:00,16:30-20:30" (divided into consecutive periods)
    # 4) "平日6:15-9:45,16:15-19:45节假日8:45-18:15" (different schedule on weekends & holidays)
    # if the board shows both directions of the route,
    # e.g. "香泉环岛5:20-21:40动物园枢纽站5:20-22:00"
    # if from_stop=="动物园枢纽站" then use "5:20-22:00"
    'schedule': '',
    # fare information on the board(space ignored)
    # e.g. "10公里以内(含)票价2元每增加5公里以内(含)加价1元"
    'fare': '',
    # tuples of stops and their mileage code
    # e.g. [
    #     ('地铁苹果园站', 1),
    #     ('绿岛家园', 10),
    #     ................
    #     ('延庆南菜园总站', 92)
    # ]
    'stops': []
}


def record_generate(record):
    # jsonify your record to the route lists
    record = {key: record[key] for key in model}
    file_name = f'{record["name"]}({record["from_stop_zh"]}-{record["to_stop_zh"]})'
    with open(f'../routes/{file_name}.json', 'w', encoding='utf-8')as f:
        json.dump(record, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    new_record = {
        'name': '977快',
        'from_stop_zh': '公主坟北',
        'from_stop_pinyin': 'GONGZHUFENBEI',
        'to_stop_zh': '冯村西里',
        'to_stop_pinyin': 'FENGCUNXILI',
        'schedule': '7:00-9:00,16:30-20:30',
        'fare': '10公里以内(含)票价2元每增加5公里以内(含)加价1元',
        'stops': [
            ('公主坟北', 29), ('航天桥西', 27), ('西钓鱼台', 26), ('定慧寺东', 25),
            ('晋元桥西', 17), ('杨庄东', 17), ('杨庄', 16), ('地铁苹果园站', 15),
            ('金顶南路', 14), ('金安桥西', 13), ('侯庄子', 8), ('双峪环岛西', 8),
            ('京煤集团', 7), ('新桥南街', 7), ('月季园东里', 7), ('葡东小区', 6),
            ('葡萄嘴环岛南', 5), ('永定中学', 4), ('冯村', 4), ('冯村大桥', 3),
            ('冯村南口', 3), ('冯西园', 2), ('冯村西里', 1)
        ]
    }
    record_generate(new_record)
