﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

lines = {
    #凡例: "路線コード": ( "会社名", "路線名", "#RRGGBB(ラインカラー)" ),

    # H: harutrak - @fubukiefsf
    "HA": ( "harutrak", "A線", "#000000" ),
    "HB": ( "harutrak", "B線", "#000000" ),
    "HC": ( "harutrak", "C線", "#000000" ),
    "HD": ( "harutrak", "D線", "#000000" ),
    "HE": ( "harutrak", "E線", "#000000" ),
    "HF": ( "harutrak", "F線", "#000000" ),
    "HG": ( "harutrak", "G線", "#000000" ),
    "HH": ( "harutrak", "H線", "#000000" ),
    "HI": ( "harutrak", "I線", "#000000" ),
    "HJ": ( "harutrak", "J線", "#000000" ),
    "HZ": ( "harutrak", "空港連絡線", "#000000" ),

    # R: はるレール - @ayafmy
    "RN": ( "はるレール", "南北快速線", "#89A4D0" ),
    "RJ": ( "はるレール", "城南線", "#AB10D2" ),
    "RT": ( "はるレール", "新津線", "#AB10D2" ),
    "RS": ( "はるレール", "城津線(西城線)", "#86B3BD" ),

    # E: はる急行鉄道 - @karno
    "ET": ( "はる急行鉄道", "月沢本線", "#FF0000" ),
    "EX": ( "はる急行鉄道", "月沢急行線", "#BF0000" ),
    "EN": ( "はる急行鉄道", "南海急行線", "#006B33" ),
    "EK": ( "はる急行鉄道", "北見線", "#4210D2" ),
    "EH": ( "はる急行鉄道", "北越線", "#4210D2" ),
    "EE": ( "はる急行鉄道", "北越急行線", "#4210D2" ),
    "ES": ( "はる急行鉄道", "参宮線", "#E4007F" ),
    "EC": ( "はる急行鉄道", "中部丘陵線", "#A0522D" ),

    # S: はる高速旅客鉄道(新幹線) - @karno
    "SC": ( "はる高速旅客鉄道", "中央新幹線", "#F5A500" ),
    "SN": ( "はる高速旅客鉄道", "南北新幹線", "#007BC7" ),

    # M: ムメイ高速鉄道 - @mumei_himazin
    "MM": ( "ムメイ高速鉄道", "ムメイ高速鉄道本線", "#FF4500" ),
    "MK": ( "ムメイ高速鉄道", "香住ライトレール線", "#F7BC9B" ),

    # N: はる近郊鉄道 - @hnakai0909
    "NI": ( "はる近郊鉄道", "内環線", "#DBCC75" ),
    "NA": ( "はる近郊鉄道", "空港線", "#DBCC75" ),

    # K: こむぎ娘レールウェイ - @flour4445
    "KC": ( "こむぎ娘レールウェイ", "千歳線", "#969182" ),
    "KK": ( "こむぎ娘レールウェイ", "海岸線", "#969182" ),
    "KS": ( "こむぎ娘レールウェイ", "作長線", "#969182" ),
    "KT": ( "こむぎ娘レールウェイ", "東海線", "#969182" ),
    "KO": ( "こむぎ娘レールウェイ", "東西線", "#969182" ),

    # L: 東部環状鉄道 - @ayafmy
    "LT": ( "東部環状鉄道", "東部環状線", "#B7D120" ),

    # T: 筑波臨海高速鉄道 - @karno
    "TR": ( "筑波臨海高速鉄道", "りんかい線", "#047391" ),
    "TT": ( "筑波臨海高速鉄道", "つくば線", "#4210D2" ),
    "TS": ( "筑波臨海高速鉄道", "下関線", "#5A3D1C" ),

    # G: 竜ヶ崎臨海鉄道 - (unknown)
    "GR": ( "竜ヶ崎臨海鉄道", "竜ヶ崎線", "#FFEB7C" ),

    # C: ささみ鉄道 - @sasamijp
    "CC": ( "ささみ鉄道", "ちくわエクスプレス線", "#D59758" ),

    # W: 比那名居電鉄 - @kb10uy
    "WS": ( "比那名居電鉄", "釧結線", "#67C6E2" ),
    "WY": ( "比那名居電鉄", "百合線", "#E03A23" ),
    "WH": ( "比那名居電鉄", "保宿線", "#9CD1A8" ),
    "WW": ( "比那名居電鉄", "南海佐倉線", "#925b0f" ), # 旧称若狭島線につきWW

    # A: はる航空 - @fubukiefsf
    "AO": ( "はる航空", "はる空港-大室線", "#00A884" ),
    "AS": ( "はる航空", "はる空港-しきみ島線", "#00A884" ),
    "AT": ( "はる航空", "はる空港-津港ヘリポート線", "#00A884" ),

    # B: 船便?(船間のテレポート) - @fubukiefsf (色未定,決まり次第修正)
    "B1": ( "船便", "ship#1-ship#3線", "#00A884" ),
    "B2": ( "船便", "大津港-ship#3線", "#00A884" ),
    "B3": ( "船便", "いくら港-ship#3線", "#00A884" ),

    # Z: その他(短距離区間・個人路線など)
    "ZC": ( "ふりかけ鉄道", "Capital Line", "#F3A6A3" ), # - @hu2r
    "ZG": ( "SRH", "外環線", "#71E700" ), # - @hadsn
    "ZH": ( "かき地下鉄", "姫子線", "#5E53A1" ), # - @kakiht
    "ZI": ( "" , "遺跡線", "#000000"), # - (unknown)
    "ZK": ( "キルミー鉄道", "ゆっくりライン", "#F472D0" ), # - @yukkuri_sinai
    "ZS": ( "鮭の子村交通局", "寿司線", "#CB4E51" ), # - @ikr7
    "ZT": ( "はる地下鉄", "調布市地下鉄線", "#9C0065" ), # - (unknown)
    "ZZ": ( "", "その他", "#000000"),
}

company_author = {
    #凡例: "会社名": "会社所有者",

    "harutrak": "fubukiefsf",
    "はるレール": "ayafmy",
    "はる急行鉄道": "karno",
    "はる高速旅客鉄道": "karno",
    "ムメイ高速鉄道": "mumei_himazin",
    "はる近郊鉄道": "hnakai0909",
    "こむぎ娘レールウェイ": "flour4445",
    "東部環状鉄道": "ayafmy",
    "筑波臨海高速鉄道": "karno",
    "竜ヶ崎臨海鉄道": "(unknown)",
    "ささみ鉄道": "sasamijp",
    "比那名居電鉄": "kb10uy",
    "はる航空": "fubukiefsf",
    "船便": "fubukiefsf",
    "ふりかけ鉄道": "hu2r",
    "SRH": "hadsn",
    "かき地下鉄": "kakiht",
    "キルミー鉄道": "yukkuri_sinai",
    "鮭の子村交通局": "ikr7",
    "": "(unknown)",
}

airline = [ "AO", "AS", "AT" ]

ship = [ "B1", "B2", "B3" ]
