import requests,os,sys,argparse,re,threading,random,socket,re
from colorama import Fore, Style
from bs4 import BeautifulSoup



if len(sys.argv) != 2:
    print("\n\nKullanım: python drl.py 12.12.12.12\n\n")
    sys.exit()

ip = sys.argv[1].split(".")



ip_1 = str(ip[0])
ip_2 = str(ip[1])
ip_3 = str(ip[2])
ip_4 = str(ip[3])

turkcell = "Turkcell Iletisim Hizmetleri A.S"
tt_mobil = "TT Mobil Iletisim Hizmetleri A.S"
noc_bilisim = "NOC BILISIM LIMITED SIRKETI"
vodofone = "Vodafone Telekomunikasyon A.S."
erhan_mahmut = "Erhan Mahmut trading as 'Aysima Bilisim Teknolojileri Erhan Mahmut'"
turksat = "Turksat Uydu Haberlesme ve Kablo TV Isletme A.S."
grid = "Grid Bilisim Teknolojileri A.S."
metronet = "Metronet Iletisim Teknoloji A.S."
vodofone_net = "VODAFONE NET ILETISIM HIZMETLERI ANONIM SIRKETI"
net_factor = "NETFACTOR TELEKOMINIKASYON VE TEKNOLOJI HIZMETLERI SANAYI VE JSC"
superonline = "Superonline Iletisim Hizmetleri A.S."
turkticaret = "TURKTICARET.NET YAZILIM HIZMETLERI SAN. ve TIC. A.S."
demiroren = "DEMIROREN TV DIGITAL PLATFORM ISLETMECILIGI A.S."
premier_dc = "PremierDC Veri Merkezi Anonim Sirketi"
radore = "Radore Veri Merkezi Hizmetleri A.S."
turknet = "TurkNet Iletisim Hizmetleri A.S."
gold_surf = "GOLDSURF INTERNET LTD"
cyport = "Cyport Communication Ltd"
dgn = "DGN TEKNOLOJI A.S."
dora = "Dora Telekomunikasyon Hizmetleri AS"
brodmax = "Broadmax Iletisim Ltd"
finansbank = "QNB Finansbank A.S."
teknotel = "TEKNOTEL TELEKOMUNIKASYON SANAYI VE TICARET A.S."
netdirekt = "Netdirekt A.S."
niobe = "Niobe Bilisim Teknolojileri Yazilim San. Tic. Ltd. Sti."
ugur_pala = "FiberSunucu internet Hizmetleri Ugur Pala"
aydogan = "Aydogan Communication LTD."
national_aca = "National Academic Network and Information Center"
ankara_universty = "Ankara University"
doruk_iletisim = "Doruk Iletisim ve Otomasyon Sanayi ve Ticaret A.S."
alkim_basin = "ALKIM BASIN YAYIN ILETISIM LTD. STI."
net_online = "Netonline Bilisim Sirketi LTD"
inetmar = "Inetmar internet Hizmetleri San. Tic. Ltd. Sti"
ispro = "Ispro Iletisium Hiz Ve Yazilim San Tic A S"
cizgi = "CIZGI TELEKOMUNIKASYON ANONIM SIRKETI"
net_internet = "Netinternet Bilisim Teknolojileri AS"
is_net = "Is Net Elektonik Bilgi Uretim Dagitim Ticaret ve Iletisim Hizmetleri A.S."
tamer_telekom = "TAMER TELEKOM TELEKOMUNIKASYON BILGISAYAR, ELEKTRONIK, YAZILIM, DONANIM SANAYI VE TICARET LIMITED SIRKETI"
medyabim = "MEDYABIM INTERNET HIZMETLERI"
eskisehir_bilisim = "Eskisehir Bilisim Iletisim San. ve Tic. A.S."
fbs = "FBS BILISIM COZUMLERI TIC LTD STI."
eczacibasi = "Eczacibasi Bilisim San.ve Tic. A.S."
ttnet = "TTNet A.S."
fix_net = "FIXNET Telekomunikasyon Limited Sirketi"
vital = "VITAL TEKNOLOJI TELEKOMUNIKASYON BILGISAYAR HIZMETLERI VE SANAYI TICARET LTD SIRKETI"
ihs = "IHS Telekomunikasyon Ltd"
sabanci = "Sabanci University"
istanbul = "Istanbuldc Veri Merkezi Ltd Sti"
vestel = "Vestel Elektronik Sanayi ve Ticaret A.S."
hurriyet = "Hurriyet Gazetecilik & Matbacilik A.S."
mynet = "MYNET A.S."
hscb = "HSBC BANK ANONIM SIRKETI"
ihlas = "Ihlas Net A.S."
axa = "AXA Holding A.S."
garanti = "Garanti Bilisim Teknolojisi ve Ticaret T.A.S."
akbank = "AKBANK TAS"
kibris = "KIBRIS MOBILE TELEKOMUNIKASYON LTD."
none = "None"
turktelekom = "Turk Telekomunikasyon Anonim Sirketi"
tellcom = "TELLCOM ILETISIM HIZMETLERI A.S."
telnet = "TELNET TELEKOM HIZMETLERI ANONIM SIRKETI"
global_i = "Global Iletisim Hizmetleri A.S."
veri_teknik = "VERITEKNIK BILISIM BASIN VE YAYIN LIMITED SIRKETI"
enson = "Enson Net Ltd Sti"
vargo = "Vargonen Teknoloji ve Bilisim Sanayi Ticaret Anonim Sirketi"
markum = "Markum Bilisim Teknolojileri Tic. Ltd. Sti."
datate = "Datatelekom Telekomunikasyon Hiz. Dis Tic. Ltd. Sti."
ortadogu = "Orta Dogu Yazilim Hizmetleri A. S."
sparkle = "TI Sparkle Turkey Telekomunukasyon A.S"
teletek = "Teletek Bulut Bilisim ve Iletisim Hizmetleri A.S."
adanet = "ADA-NET Internet ve Iletisim Hizmetleri Tic. A.S."
eser = "Eser Telekom"
atlas = "ATLAS ON-LINE"
atp = "ATP"
teksil = "TEKSTIL BANKASI A.S."
sistem = "Sistem Co. Ltd."
nano = "Nano Iletisim Bilisim Hizmetleri Teknoloji Sistemleri Sanayi ve Ticaret Ltd Sirketi"
turk_ekonomi = "Turk Ekonomi Bankasi Anonim Sirketi"
nortel = "Nortel Networks Netas Telekomunikasyon A.S."
isik = "ISIK Bilgisayar Internet ve Yayincilik Hizmetleri"





class_5 = {
    11:turkcell,
    24:turkcell,
    46:tt_mobil,
    104:kibris,
    176:tt_mobil,
    226:vodofone,
    229:vodofone,
    250:erhan_mahmut
}

class_24 = {
    133:turksat
}


class_31 = {
    6:grid,
    44:metronet,
    140:turkcell,
    145:vodofone_net,
    155:vodofone_net,
    169:net_factor,
    176:superonline,
    177:vodofone,
    186:turkticaret,
    200:demiroren,
    206:vodofone_net,
    223:turknet,
}


class_37 = {
    34:kibris,
    72:gold_surf,
    77:grid,
    122:metronet,
    123:metronet,
    130:none,
    154:tt_mobil,
    218:cyport,
    247:dgn,
}


class_46 = {
    1:none,
    2:vodofone_net,
    25:radore,
    104:tt_mobil,
    106:vodofone,
    154:vodofone,
    196:turksat,
    221:vodofone,
    234:vodofone_net,
    252:brodmax,
}


class_77 = {
    79:grid,
    223:netdirekt,
    245:niobe,


}


class_78 = {
    111:ugur_pala,
    160:turktelekom,
}


class_79 = {
    123:national_aca
}


class_80 = {
    93:ugur_pala,
    251:ankara_universty,
}


class_81 = {
    6:vodofone,
    8:vodofone_net,
    21:doruk_iletisim,
    22:dora,
    91:alkim_basin,
    212:turktelekom,

}


class_82 = {
    97:none,
    145:net_online,
    150:vodofone_net,
    151:doruk_iletisim,
    222:tellcom,
}


class_83 = {
    66:demiroren,
}

class_84 = {
    17:telnet,
    44:vodofone_net,
    51:global_i,

}

class_85 = {
    29:tellcom,
    95:inetmar,
    96:turktelekom,
    153:superonline,

}

class_86 = {
    108:turkcell,
}

class_87 = {
    251:ispro,
}

class_88 = {
    224:turktelekom,
}

class_89 = {
    19:cizgi,
    106:grid,
}

class_90 = {
    158:is_net,
}

class_91 = {
    93:global_i,
    151:tamer_telekom,
    191:netdirekt,
}

class_92 = {
    44:tellcom,
    61:ankara_universty,
    63:net_online,

}

class_93 = {
    91:eczacibasi,
    155:ttnet,
    182:net_online,
    184:fix_net,
    186:vital,
}

class_94 = {
    54:turksat,
    73:cizgi,
    78:net_online,
    79:kibris,
    101:radore,
    103:veri_teknik,
}

class_95 = {
    0:turktelekom,
    65:vodofone_net,
    70:turknet,
    142:enson,
    183:national_aca,

}

class_109 = {
    228:none
}


class_141 = {
    196:turkcell,
}

class_149 = {
    0:vodofone,
    140:vodofone,
}

class_151 = {
    135:tt_mobil,
    250:tellcom,
}

class_159 = {
    20:sabanci,
    146:turknet,
    253:net_internet,
}

class_167 = {
    160:istanbul,

}

class_176 = {
    30:tt_mobil,
    33:tellcom,
    40:tellcom,
    53:radore,
    54:vodofone,
    88:superonline,
    89:turkcell,
    90:turkcell,
    216:vodofone,
    220:tt_mobil,
    227:turkcell,
    232:superonline,
    234:superonline,
    236:superonline,
    237:turkcell,
    238:turkcell,
    240:turksat,

}

class_178 = {
    18:vargo,
    210:markum,
    211:radore,
    233:turksat,
    240:turkcell,

}

class_188 = {
    3:vodofone_net,
    38:vodofone,
    41:tt_mobil,
    56:turkcell,
    119:turknet,
    124:vital,
    125:datate,
    132:premier_dc,
}

class_193 = {
    140:national_aca,
    192:turknet,
    243:vodofone_net,
    255:national_aca,
}

class_194 = {
    27:national_aca,
    54:turktelekom,
}
class_195 = {
    33:superonline,
    46:vodofone_net,
    87:vodofone_net,
    112:adanet,
    174:turktelekom,
    175:turktelekom,
}

class_212 = {
    2:doruk_iletisim,
    12:vodofone_net,
    15:vodofone_net,
    29:vestel,
    31:hurriyet,
    50:eser,
    57:tellcom,
    58:doruk_iletisim,
    64:atlas,
    65:vodofone,
    68:premier_dc,
    101:mynet,
    108:sistem,
    115:vodofone_net,
    125:turknet,
    127:hscb,
    133:vodofone_net,
    146:nano,
    154:turknet,
    156:turktelekom,
    174:turktelekom,
    175:turktelekom,
    252:superonline,
    253:superonline,

}

class_213 = {
    43:turkcell,
    74:superonline,
    128:radore,
    142:tamer_telekom,
    143:is_net,
    144:teknotel,
    148:turk_ekonomi,
    155:doruk_iletisim,
    161:is_net,
    186:vodofone_net,
    194:vodofone_net,
    211:tt_mobil,
    232:adanet,
    238:ihlas,
    248:vodofone_net,
    254:superonline,


}

class_217 = {
    17:alkim_basin,
    64:axa,
    65:none,
    68:garanti,
    78:nortel,
    116:isik,
    131:superonline,
    169:akbank,
    174:tt_mobil,
    195:ugur_pala,


}

# ------------------------------------------------------------------------------------------------------------------------------------
try:

    if ip_1 == str(5):
            if ip_2 == str(44):
                if ip_3 == str(80):
                    print(tt_mobil)
                elif ip_3 == str(144):
                    print(noc_bilisim)
            else:
                print(class_5[int(ip_2)])


    if ip_1 == str(24):
        print(class_24[int(ip_2)])


    if ip_1 == str(31):
            if ip_2 == str(210):
                if ip_3 == str(32):
                    print(premier_dc)
                elif ip_3 == str(64):
                    print(radore)
            else:
                print(class_31[int(ip_2)])

    if ip_1 == str(37):
        print(class_37[int(ip_2)])


    if ip_1 == str(46):
            if ip_2 == str(20):
                if ip_3 == str(0):
                    print(dgn)
                elif ip_3 == str(144):
                    print(dora)
            else:
                print(class_46[int(ip_2)])


    if ip_1 == str(77):
            if ip_2 == str(92):
                if ip_3 == str(96):
                    print(teknotel)
                elif ip_3 == str(128):
                    print(premier_dc)
            else:
                print(class_77[int(ip_2)])

    if ip_1 == str(78):
            if ip_2 == str(135):
                if ip_3 == str(16):
                    print(aydogan)
                elif ip_3 == str(32):
                    print(aydogan)
                elif ip_3 == str(64):
                    print(premier_dc)
            else:
                print(class_78[int(ip_2)])

    if ip_1 == str(79):
        print(class_79[int(ip_2)])

    if ip_1 == str(80):
        print(class_80[int(ip_2)])

    if ip_1 == str(81):
        print(class_81[int(ip_2)])

    if ip_1 == str(82):
        print(class_82[int(ip_2)])

    if ip_1 == str(83):
        print(class_83[int(ip_2)])

    if ip_1 == str(84):
        print(class_84[int(ip_2)])

    if ip_1 == str(85):
        print(class_85[int(ip_2)])

    if ip_1 == str(86):
        print(class_86[int(ip_2)])

    if ip_1 == str(87):
        print(class_87[int(ip_2)])

    if ip_1 == str(88):
        print(class_88[int(ip_2)])

    if ip_1 == str(89):
        if ip_2 == str(252):
            if ip_3 == str(128):
                print(net_internet)
            elif ip_3 == str(160):
                print(net_internet)
        else:
            print(class_89[int(ip_2)])


    if ip_1 == str(90):
        print(class_90[int(ip_2)])

    if ip_1 == str(91):
        print(class_91[int(ip_2)])

    if ip_1 == str(92):
        print(class_92[int(ip_2)])

    if ip_1 == str(93):
        if ip_2 == str(89):
            if ip_3 == str(16):
                print(medyabim)
            elif ip_3 == str(64):
                print(eskisehir_bilisim)
            elif ip_3 == str(224):
                print(fbs)
        else:
            print(class_93[int(ip_2)])

    if ip_1 == str(94):
        if ip_2 == str(102):
            if ip_3 == str(0):
                print(net_internet)
            elif ip_3 == str(64):
                print(doruk_iletisim)
        else:
            print(class_94[int(ip_2)])


    if ip_1 == str(95):
        if ip_2 == str(173):
            if ip_3 == str(0):
                print(tt_mobil)
            elif ip_3 == str(160):
                print(doruk_iletisim)
            elif ip_3 == str(224):
                print(none)
        else:
            print(class_95[int(ip_2)])


    if ip_1 == str(109):
        print(class_109[int(ip_2)])

    if ip_1 == str(141):
        print(class_141[int(ip_2)])

    if ip_1 == str(149):
        print(class_149[int(ip_2)])

    if ip_1 == str(151):
        print(class_151[int(ip_2)])

    if ip_1 == str(159):
        print(class_159[int(ip_2)])

    if ip_1 == str(167):
        print(class_167[int(ip_2)])

    if ip_1 == str(176):
        print(class_176[int(ip_2)])

    if ip_1 == str(178):
        print(class_178[int(ip_2)])

    if ip_1 == str(188):
        print(class_188[int(ip_2)])

    if ip_1 == str(193):
        print(class_193[int(ip_2)])

    if ip_1 == str(194):
        print(class_194[int(ip_2)])

    if ip_1 == str(195):
        if ip_2 == str(142):
            print(superonline)
        elif ip_2 == str(155):
            if ip_3 == str(0):
                print(ortadogu)
            elif ip_3 == str(64):
                print(sparkle)
            elif ip_3 == str(112):
                print(superonline)
            elif ip_3 == str(128):
                print(teletek)
            elif ip_3 == str(160):
                print(superonline)
        else:
            print(class_195[int(ip_2)])


    if ip_1 == str(212):
        if ip_2 == str(98):
            if ip_3 == str(0):
                print(is_net)
            elif ip_3 == str(192):
                print(vodofone_net)
        elif ip_2 == str(109):
            if ip_3 == str(96):
                print(atp)
            elif ip_3 == str(224):
                print(teksil)
        else:
            print(class_212[int(ip_2)])


    if ip_1 == str(213):
        if ip_2 == str(14):
            print(superonline)
        elif ip_2 == str(153):
            print(tellcom)
        elif ip_2 == str(243):
            print(demiroren)

        else:
            print(class_213[int(ip_2)])


    if ip_1 == str(217):
        if ip_2 == str(31):
            print(vodofone)
        else:
            print(class_217[int(ip_2)])
except:
    print("HATA !")






