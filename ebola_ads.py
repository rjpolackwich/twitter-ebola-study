# -*- coding: utf-8 -*-
liberia_uads = [u"Liberia", u"Monrovia", u"Nimba", u"River Cess", u"Rivercess", u"Sinoe", u"Bomi", u"Tubmanburg", u"Bong", u"Gbarnga", u"Gbarpolu", u"Bopulu", u"Grand Cape Mount", u"Robertsport", u"Grand Bassa", u"Buchanan", u"Grand Gedeh", u"Zwedru", u"Grand Kru", u"Barclayville", u"Lofa", u"Voinjama", u"Margibi", u"Kakata", u"Montserrado", u"Bensonville", u"Nimba", u"Sanniquellie", u"River Gee", u"Fish Town", u"Sinoe", u"Greenville"]
guinea_uads = [u"Guinea", u"Conakry", u"Kaloum", u"Dixinn", u"Ratoma", u"Matam", u"Matoto", u"Nzérékoré", u"N'Zérékoré", u"Kankan", u"Kindia", u"Boké", u"Labé", u"Faranah", u"Mamou", u"Guéckédou", u"Guékédou", u"Kissidougou"]
sierraleone_uads = [u"Sierra Leone", u"Bombali", u"Makeni", u"Koinadugu", u"Kabala", u"Port Loko", u"Tonkolili", u"Magburaka", u"Kambia", u"Kenema", u"Kono", u"Koidu", u"Kailahun", u"Bo", u"Bonthe", u"Mattru Jong", u"Pujehun", u"Moyamba", u"Freetown", u"Waterloo"]


liberia_ads = ["Liberia", "Monrovia", "Nimba", "River.*Cess", "Sinoe", "Bomi", "Tubmanburg", "Bong", "Gbarnga", "Gbarpolu", "Bopulu", "Grand.*Cape.*Mount", "Robertsport", "Grand.*Bassa", "Buchanan", "Grand.*Gedeh", "Zwedru", "Grand.*Kru", "Barclayville", "Lofa", "Voinjama", "Margibi", "Kakata", "Montserrado", "Bensonville", "Sanniquellie", "River.*Gee", "Fish.*Town", "Greenville"]
guinea_ads = ["Guinea", "Conakry", "Kaloum", "Dixinn", "Ratoma", "Matam", "Matoto", u"Nzérékoré", u"N'Zérékoré", "Nzérékoré", "N'Zérékoré", "n'zerekore", "Kankan", "Kindia", "Boké", u"Boké", "Boke", "Labe", u"Labé", "Labé", "Faranah", "Mamou", "Guéckédou", u"Guéckédou", "Guékédou", u"Guékédou", "Kissidougou"]
sierraleone_ads = ["Bombali", "Makeni", "Koinadugu", "Kabala", "Port.*Loko", "Tonkolili", "Magburaka", "Kambia", "Kenema", "Kono", "Koidu", "Kailahun", "Bo", "Bonthe", "Mattru.*Jong", "Pujehun", "Moyamba", "Freetown", "Waterloo", "Newton"]

Ld = dict()
Ld["Monrovia"]   =  {"coords": [6.3133,-10.8014], "population": 939542, "rthresh": 5,  "numresults": 96}
Ld["Gbarnga"]    =  {"coords": [6.996,-9.472],    "population": 45835,  "rthresh": 21, "numresults": 36}
Ld["Kakata"]     =  {"coords": [6.53, -10.352],   "population": 33945,  "rthresh": 5,  "numresults": 8}
Ld["Bensonville"]=  {"coords": [6.446, -10.613],  "population": 33188,  "rthresh": 5,  "numresults": 0}
Ld["Harper"]     =  {"coords": [4.376, -7.715],   "population": 32661,  "rthresh": 5,  "numresults": 25}
Ld["Vionjama"]   =  {"coords": [8.422, -9.748],   "population": 26594,  "rthresh": 5,  "numresults": 0}
Ld["Buchanan"]   =  {"coords": [5.881, -10.045],  "population": 25731,  "rthresh": 5,  "numresults": 0}

Sd = dict()
Sd["Freetown"]   =  {"coords": [8.484, -13.23],   "population": 802639, "rthresh": 5, "numresults": 100}
Sd["Bo"]         =  {"coords": [7.965, -11.738],  "population": 174354, "rthresh": 5, "numresults": 0}
Sd["Kenema"]     =  {"coords": [7.877, -11.188],  "population": 143137, "rthresh": 5, "numresults": 7}
Sd["Koidu"]      =  {"coords": [8.633, -10.983],  "population": 88000,  "rthresh": 21, "numresults": 7}
Sd["Makeni"]     =  {"coords": [8.883, -12.05],   "population": 87679,  "rthresh": 5, "numresults": 2} #However the search was no longer saturated at 21 km (47 results, 3 gps)
Sd["Port Loko"]  =  {"coords": [8.767, -12.783],  "population": 21308,  "rthresh": 11, "numresults": 0}
Sd["Waterloo"]   =  {"coords": [8.339, -13.071],  "population": 19750,  "rthresh": 5, "numresults": 2}

Gd = dict()
Gd["Conakry"]    =  {"coords": [9.538, -13.688],  "population": 1767200, "rthresh": 5, "numresults": 2}
Gd["Nzerekore"]  =  {"coords": [7.756, -8.818],   "population": 132728,  "rthresh": 5, "numresults": 1}
Gd["Kindia"]     =  {"coords": [10.057, -12.866], "population": 117062,  "rthresh": 21, "numresults": 5}
Gd["Kankan"]     =  {"coords": [10.385, -9.306],  "population": 114009,  "rthresh": 25, "numresults": 3}
Gd["Gueckedou"]  =  {"coords": [8.567, -10.134],  "population": 79140,   "rthresh": 17, "numresults": 5}
Gd["Port Kamsar"]=  {"coords": [10.667, -14.6],   "population": 61527,   "rthresh": 5, "numresults": 49}
Gd["Labe"]       =  {"coords": [11.318, -12.283], "population": 58649,   "rthresh": 12, "numresults": 22}
 