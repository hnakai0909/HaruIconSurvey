﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

stations = {
    # 特定大規模駅
    "AAA": "はる空港",
    "CCC": "長府",
    "EEE": "EFB城",
    "HHH": "はるアイコン鯖役場",
    "JJJ": "城南",
    "SSS": "下関",
    "TTT": "津港",
    "YYY": "雪見町",
    # メガネケエスタワー(特殊扱い)
    "MCT": "メガネケエスタワー(メガネケエスタワー南)",
    "MCW": "メガネケエスタワー西",
    "MCE": "メガネケエスタワー東",
    # 新幹線
    "CCN": "新長府",
    "NGO": "名古屋",
    "WKN": "稚内",
    # harutrak・ムメイ高速鉄道
    "AAN": "空港北",
    "AOH": "青木ヶ原",
    "FUT": "古谷",
    "GEJ": "善通寺",
    "GES": "南善通寺",
    "IKP": "いくら港",
    "JIC": "中辞林",
    "JIR": "辞林",
    "JOT": "城東",
    "KAD": "楓",
    "KAM": "春日野道",
    "KAN": "北香住",
    "KAS": "香住",
    "KIS": "北砂漠",
    "KOZ": "古津賀",
    "KUY": "久野山",
    "MEH": "明北",
    "NEM": "練馬",
    "NIT": "新津",
    "NMU": "中村",
    "NNO": "中野",
    "NUM": "中海町",
    "OMR": "大室",
    "OTP": "大津港",
    "OIW": "追分",
    "SHE": "東北沢(下北沢東)",
    "SHK": "湘南海岸",
    "SHZ": "下北沢",
    "SIB": "新橋",
    "SKV": "鮭の子村",
    "TOJ": "藤治湖",
    "TSB": "筑波",
    "TSI": "津入口",
    "TSU": "土浦",
    "TYF": "調布",
    "YAA": "宿木",
    "YAB": "北宿木",
    "YAC": "旧宿木",
    "YAD": "西宿木",
    "YOZ": "夜築町",
    "YTH": "宿津平原",
    # はるレール(東環線含む)
    "GOJ": "五条",
    "KEE": "刑務所東",
    "KIM": "北森",
    "KYS": "京ヶ瀬",
    "MIH": "三原",
    "MIN": "北三原",
    "MOS": "森下",
    "NTS": "中津",
    "SAB": "西原",
    "SUB": "水原",
    "TAI": "絶海池",
    "TSH": "筑波高原",
    # はる急行鉄道(りんかい線含む)
    "AOM": "青宮",
    "CTS": "千歳",
    "HAS": "浜坂",
    "HGZ": "星川銀座",
    "HIZ": "雲雀坂",
    "IBY": "伊吹山",
    "ICJ": "一条",
    "JOH": "城北",
    "KAI": "上砂",
    "KIH": "北見平原",
    "KOT": "こむぎこタワー",
    "MOY": "守山",
    "NAF": "南海埠頭",
    "OAR": "大洗",
    "SAN": "作並",
    "SAT": "桜土浦",
    "SHT": "新都心",
    "SIM": "東雲",
    "SNM": "スノーマン前",
    "TEK": "天竜峡",
    "TOT": "鳥取",
    "TSS": "月山神社",
    "TSD": "筑波大学",
    "TYS": "月屋根沢",
    "YUB": "結上橋",
    "YUO": "雪見温泉",
    # はる近郊鉄道
    "SAO": "ささみ温泉",
    "SHJ": "しきみ城",
    # こむレール
    "CTK": "千歳海岸",
    "CTM": "南千歳",
    "DAS": "大山",
    "FUK": "船越",
    "HIO": "光が丘",
    "KUM": "国見",
    "MIS": "水無瀬",
    "NIZ": "西塚",
    "ODW": "小田原",
    "OTK": "大月",
    "SOG": "蘇我",
    "TAS": "高瀬",
    #比那名居電鉄
    "YAE":"元宿木",
    "TKN":"筍",
    "HGW":"雛川",
    "VTX":"暴龍天山",
    "KUS":"釧路",
    "KRM":"桐間",
    "TTM":"戸津美",
    "UJM":"宇治松",
    "KFH":"香風ヶ丘",
    "TDB":"天々座湾",
    "HTO":"保登",
    "NAG":"永江池",
    "WKS":"若狭島",
    #船
    "SH1":"ship#1", # ふぁぼ丸 @ 津
    "SH3":"ship#3", # ? @ しきみ島
    # その他私鉄・貨物など
    "DAM": "大明神前",
    "FUO": "藤が丘",
    "HAI": "はるアイコン",
    "HIC": "姫子市",
    "HII": "姫子遺跡",
    "KOS": "神津島",
    "NIS": "西砂丘村",
    "REH": "れいかハウス",
    "RYS": "竜ヶ崎",
    "SHI": "しきみ島",
    "TSI": "月山神社地下遺跡", # もともとは名無し
    "TYE": "東調布",
    "YUH": "ゆっくりハウス",
    "YUK": "ゆっくりライン貨物ターミナル",
}
