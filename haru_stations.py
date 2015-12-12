﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

station_names = {
    # 特定大規模駅
    "AAA": ( "はる空港", "はるくうこう" ),
    "CCC": ( "長府", "ちょうふ" ),
    "EEE": ( "エターナルフォースブリザード城前", "えたーなるふぉーすぶりざーどじょうまえ" ),
    "HHH": ( "役場前", "やくばまえ" ),
    "JJJ": ( "城南", "じょうなん" ),
    "SSS": ( "下関", "しものせき" ),
    "TTT": ( "津港", "つこう" ),
    "YYY": ( "雪見町", "ゆきみまち" ),
    # メガネケエスタワー(特殊扱い)
    "MCT": ( "メガネケエスタワー(南)", "めがねけえすたわーまえ（みなみ）" ),
    "MCW": ( "メガネケエスタワー(西)", "めがねけえすたわーまえ（にし）" ),
    "MCE": ( "メガネケエスタワー(東)", "めがねけえすたわーまえ（ひがし）" ),
    # 新幹線
    "CCN": ( "新長府", "しんちょうふ" ),
    "NGO": ( "名古屋", "なごや" ),
    "WKN": ( "稚内", "わっかない" ),
    # harutrak・ムメイ高速鉄道
    "AAN": ( "空港北", "くうこうきた" ),
    "AOH": ( "青木ヶ原", "あおきがはら" ),
    "FUT": ( "古谷", "ふるたに" ),
    "GEJ": ( "善通寺", "ぜんつうじ" ),
    "GES": ( "南善通寺", "みなみぜんつうじ" ),
    "IKP": ( "いくら港", "いくらこう" ),
    "JIC": ( "中辞林", "なかじりん" ),
    "JIR": ( "辞林", "じりん" ),
    "JOT": ( "城東", "じょうとう" ),
    "KAD": ( "楓", "かえで" ),
    "KAM": ( "春日野道", "かすがのみち" ),
    "KAN": ( "北香住", "きたかすみ" ),
    "KAS": ( "香住", "かすみ" ),
    "KIS": ( "北砂漠", "きたさばく" ),
    "KOZ": ( "古津賀", "こつか" ),
    "KUY": ( "久野山", "くのやま" ),
    "MEH": ( "明北", "めいほく" ),
    "NEM": ( "練馬", "ねりま" ),
    "NIT": ( "新津", "にいつ" ),
    "NMU": ( "中村", "なかむら" ),
    "NNO": ( "中野", "なかの" ),
    "NUM": ( "中海町", "なかうみまち" ),
    "OMR": ( "大室", "おおむろ" ),
    "OTP": ( "大津港", "おおつこう" ),
    "OIW": ( "追分", "おいわけ" ),
    "SHE": ( "東北沢", "ひがしきたざわ" ),
    "SHK": ( "湘南海岸", "しょうなんかいがん" ),
    "SHZ": ( "下北沢", "しもきたざわ" ),
    "SIB": ( "新橋", "しんばし" ),
    "SKV": ( "鮭の子村", "しゃけのこむら" ),
    "TOJ": ( "藤治湖", "とうじこ" ),
    "TSB": ( "筑波", "つくば" ),
    "TSI": ( "津入口", "ついりぐち" ),
    "TSU": ( "土浦", "つちうら" ),
    "TYF": ( "調布", "ちょうふ" ),
    "YAA": ( "宿木", "やどき" ),
    "YAB": ( "北宿木", "きたやどき" ),
    "YAC": ( "旧宿木", "きゅうやどき" ),
    "YAD": ( "西宿木", "にしやどき" ),
    "YOZ": ( "夜築町", "よづきまち" ),
    "YTH": ( "宿津平原", "やどつへいげん" ),
    # はるレール(東環線含む)
    "GOJ": ( "五条", "ごじょう" ),
    "KEE": ( "刑務所東", "けいむしょひがし" ),
    "KIM": ( "北森", "きたもり" ),
    "KYS": ( "京ヶ瀬", "きょうがせ" ),
    "MIH": ( "三原", "みはら" ),
    "MIN": ( "北三原", "きたみはら" ),
    "MOS": ( "森下", "もりした" ),
    "NTS": ( "中津", "なかつ" ),
    "SAB": ( "西原", "さいばら" ),
    "SUB": ( "水原", "すいばら" ),
    "TAI": ( "絶海池", "たるみいけ" ),
    "TSH": ( "筑波高原", "つくばこうげん" ),
    # はる急行鉄道(りんかい線含む)
    "AOM": ( "青宮", "あおみや" ),
    "CTS": ( "千歳", "ちとせ" ),
    "HAO": ( "浜大津", "はまおおつ" ),
    "HAS": ( "浜坂", "はまさか" ),
    "HGZ": ( "星川銀座", "ほしかわぎんざ" ),
    "HIZ": ( "雲雀坂", "ひばりざか" ),
    "IBY": ( "伊吹山", "いぶきやま" ),
    "ICJ": ( "一条", "いちじょう" ),
    "JOH": ( "城北", "じょうほく" ),
    "KAI": ( "上砂", "かみいさご" ),
    "KIH": ( "北見平原", "きたみへいげん" ),
    "KIY": ( "霧弥湖町", "きりやこちょう" ),
    "KOT": ( "こむぎこタワー", "こむぎこたわー" ),
    "MOY": ( "守山", "もりやま" ),
    "NAF": ( "南海埠頭", "なんかいふとう" ),
    "OAR": ( "大洗", "おおあらい" ),
    "SAK": ( "佐倉", "さくら" ),
    "SAN": ( "作並", "さくなみ" ),
    "SAT": ( "桜土浦", "さくらつちうら" ),
    "SHT": ( "新都心", "しんとしん" ),
    "SIM": ( "東雲", "しののめ" ),
    "SNM": ( "スノーマン前", "すのーまんまえ" ),
    "TEK": ( "天竜峡", "てんりゅうきょう" ),
    "TOT": ( "鳥取", "とっとり" ),
    "TSS": ( "月山神社", "つきやまじんじゃ" ),
    "TSD": ( "筑波大学", "つくばだいがく" ),
    "TYS": ( "月屋根沢", "つきやねさわ" ),
    "YON": ( "夜ノ森", "よのもり" ),
    "YUB": ( "結上橋", "ゆいあげばし" ),
    "YUH": ( "由利本荘", "ゆりほんじょう" ),
    "YUO": ( "雪見温泉", "ゆきみおんせん" ),
    # はる近郊鉄道
    "SAO": ( "ささみ温泉", "ささみおんせん" ),
    "SHJ": ( "しきみ城", "しきみじょう" ),
    # こむレール
    "CTK": ( "千歳海岸", "ちとせかいがん" ),
    "CTM": ( "南千歳", "みなみちとせ" ),
    "DAS": ( "大山", "だいせん" ),
    "FUK": ( "船越", "ふなこし" ),
    "HIO": ( "光が丘", "ひかりがおか" ),
    "KUM": ( "国見", "くにみ" ),
    "MIS": ( "水無瀬", "みなせ" ),
    "NIZ": ( "西塚", "にしづか" ),
    "ODW": ( "小田原", "おだわら" ),
    "OTK": ( "大月", "おおつき" ),
    "SOG": ( "蘇我", "そが" ),
    "TAS": ( "高瀬", "たかせ" ),
    #比那名居電鉄
    "YAE": ( "元宿木", "もとやどき" ),
    "TKN": ( "筍", "たけのこ" ),
    "HGW": ( "雛川", "ひながわ" ),
    "VTX": ( "暴龍天山", "ぼるてやま" ),
    "KUS": ( "釧路", "くしろ" ),
    "KRM": ( "桐間", "きりま" ),
    "TTM": ( "戸津美", "とつみ" ),
    "UJM": ( "宇治松", "うじまつ" ),
    "KFH": ( "香風ヶ丘", "かふうがおか" ),
    "TDB": ( "天々座湾", "てでざわん" ),
    "HTO": ( "保登", "ほと" ),
    "NAG": ( "永江池", "ながえいけ" ),
    "WKS": ( "若狭島", "わかさじま" ),
    "YRH": ( "由利本荘", "ゆりほんじょう" ),
    # 船
    "SH1": ( "ship#1", "しっぷ１" ), # ふぁぼ丸 @ 津
    "SH3": ( "ship#3", "しっぷ３" ), # ? @ しきみ島
    # その他私鉄・貨物など
    "DAM": ( "大明神前", "だいみょうじんまえ" ),
    "FUO": ( "藤が丘", "ふじがおか" ),
    "HAI": ( "はるアイコン", "はるあいこん" ),
    "HIC": ( "姫子市", "ひめこし" ),
    "HII": ( "姫子遺跡", "ひめこいせき" ),
    "KOS": ( "神津島", "こうづしま" ),
    "NIS": ( "西砂丘村", "にしすなおかむら" ),
    "REH": ( "れいかハウス", "れいかはうす" ),
    "RYS": ( "竜ヶ崎", "りゅうがさき" ),
    "SHI": ( "しきみ島", "しきみじま" ),
    "TSI": ( "月山神社地下遺跡", "つきやまじんじゃちかいせき" ), # もともとは名無し
    "TYE": ( "東調布", "ひがしちょうふ" ),
    "YUH": ( "ゆっくりハウス", "ゆっくりはうす" ),
    "YUK": ( "ゆっくりライン貨物ターミナル", "ゆっくりらいんかもつたーみなる" ),
}

# 駅コードは他路線と共有しているが, 特別な駅名が存在する駅の一覧
station_special_names = {
    "ET": {
        "NMU": ( "中村本町", "なかむらほんまち" ),
    },
    "EC": {
        "NMU": ( "中村本町", "なかむらほんまち" ),
        "MCT": ( "メガネケエスタワー", "めがねけえすたわー" ),
    },
    "LT": {
        "CCN": ( "環鉄新長府", "かんてつしんちょうふ" ),
    },
    "MM": {
        "HHH": ( "役場前(東梅田)", "やくばまえ（ひがしうめだ）" ),
    },
    "RT": {
        "TSB": ( "新線筑波", "しんせんつくば" ),
    },
    "RJ": {
        "EEE": ( "EFB城", "えたーなるふぉーすぶりざーどじょう" ),
    },
    "RS": {
        "EEE": ( "EFB城", "えたーなるふぉーすぶりざーどじょう" ),
    },
    "SC": {
        "EEE": ( "EFB城", "えたーなるふぉーすぶりざーどじょう" ),
        "HHH": ( "新役場", "しんやくば" ),
    },
    "SN": {
        "HHH": ( "新役場", "しんやくば" ),
    },
    "ZI": {
        "HHH": ( "旧役場前", "きゅうやくばまえ" ),
    },
    # 飛行場系
    "AT": {
        "TTT": ( "津ヘリポート", "つへりぽーと" ),
    },
    "AS": {
        "SHI": ( "しきみ島空港", "しきみじまくうこう" ),
    },
    "AO": {
        "OMR": ( "大室飛行場", "おおむろひこうじょう" ),
    },
    # 船系
    "B2": {
        "SH3": ( "ship3 #2", "しっぷ３＃２" ),
    },
    "B3": {
        "SH3": ( "ship3 #3", "しっぷ３＃３" ),
    },
}
