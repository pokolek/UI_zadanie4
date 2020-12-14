import random
import time
import matplotlib.pyplot as plt
import math


class Priestor:
    def __init__(self):
        # pociatocnych 20 bodov pre graf
        self.pociatocne_body = {
            'R': [(-4500, -4400), (-4200, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
            'G': [(4500, -4400), (4200, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
            'B': [(-4500, 4400), (-4200, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
            'P': [(4500, 4400), (4200, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
        }

        # rozsahy tried R,G,B,P
        # aby sme sa vyhli zapornym cislam, posunuli sme hranice intervalu z 5000 na 10 000
        self.rozsahy = {
            "rx": (0, 5500),
            "ry": (0, 5500),
            "gx": (4500, 10000),
            "gy": (0, 5500),
            "bx": (0, 5500),
            "by": (4500, 10000),
            "px": (4500, 10000),
            "py": (4500, 10000),

        }

        # premenna na zistenie poctu rozdielnych bodov pri klasifikacii
        self.rozdielne_body_po_klasifikacii = 0

    # funkcia na vygenerovanie bodov s parametrom n, co je pocet bodov pre jednotlivu triedu
    def generuj_n_bodov(self, n):
        # pre kazdu triedu mame vytvoreny set
        generovane_body = []
        R = set()
        G = set()
        B = set()
        P = set()

        # rozsah_x a rozsah_y sluzia na urcenie rozsahu farby, z ktoreho chceme generovat bod
        rozsah_x = ()
        rozsah_y = ()

        # i sluzi na rozoznanie ktoru farbu ukladame
        # 0 = R
        # 1 = G
        # 2 = B
        # 3 = P
        for i in range(4):
            # postupne striedame triedy RGBP
            # urcujeme v ktorom rozsahu sa nachadzame
            if i == 0:
                rozsah_x = self.rozsahy["rx"]
                rozsah_y = self.rozsahy["ry"]
            elif i == 1:
                rozsah_x = self.rozsahy["gx"]
                rozsah_y = self.rozsahy["gy"]
            elif i == 2:
                rozsah_x = self.rozsahy["bx"]
                rozsah_y = self.rozsahy["by"]
            elif i == 3:
                rozsah_x = self.rozsahy["px"]
                rozsah_y = self.rozsahy["py"]

            # generujeme presny pocet unikatnych bodov pre kazdu triedu n bodov
            pocet_bodov = 0
            while pocet_bodov != n:
                # testovanie pravdepodobnosti 1 alebo 99 percent
                pravdepodobnost = random.randint(1, 100)

                # ak je pravdepodobnost 1 percento, tak generujeme bod z lubovolneho intervalu
                if pravdepodobnost == 1:
                    #  nahodne generujeme lubovolny bod
                    x = random.randint(0, 10000)
                    y = random.randint(0, 10000)

                    # docasna premenna pre bod
                    tmp_suradnice = (x, y)
                    # kontrolujeme ci je bod unikatny
                    if tmp_suradnice not in generovane_body \
                            and tmp_suradnice not in R \
                            and tmp_suradnice not in G \
                            and tmp_suradnice not in B \
                            and tmp_suradnice not in P:
                        # ak je tak podla i ho priradime do tried
                        if i == 0:
                            R.add(tmp_suradnice)
                        elif i == 1:
                            G.add(tmp_suradnice)
                        elif i == 2:
                            B.add(tmp_suradnice)
                        elif i == 3:
                            P.add(tmp_suradnice)
                        pocet_bodov += 1

                # ak je pravdepodobnost 99 percent, tak generujeme cislo z pozadovaneho intervalu
                else:
                    # nahodne generujeme bod z rozsahu
                    x = random.randint(rozsah_x[0], rozsah_x[1])
                    y = random.randint(rozsah_y[0], rozsah_y[1])

                    # docasna premenna pre bod
                    tmp_suradnice = (x, y)
                    # kontrolujeme ci je bod unikatny
                    if tmp_suradnice not in generovane_body \
                            and tmp_suradnice not in R \
                            and tmp_suradnice not in G \
                            and tmp_suradnice not in B \
                            and tmp_suradnice not in P:
                        # ak je tak podla i ho priradime do tried
                        if i == 0:
                            R.add(tmp_suradnice)
                        elif i == 1:
                            G.add(tmp_suradnice)
                        elif i == 2:
                            B.add(tmp_suradnice)
                        elif i == 3:
                            P.add(tmp_suradnice)
                        pocet_bodov += 1

        # po vygenerovani bodov ich zapisujeme do suboru cisla.txt
        f = open("cisla.txt", "w")

        index_bodu = 0
        # zapis bodov do zoznamu generovanych bodov postupne podla tried aby sa nam triedy neopakovali za sebou
        while index_bodu != n:
            generovane_body.append(list(R)[index_bodu])
            generovane_body.append(list(G)[index_bodu])
            generovane_body.append(list(B)[index_bodu])
            generovane_body.append(list(P)[index_bodu])

            index_bodu += 1

        # zapisanie do suboru na zaciatok pociatocne body, cize ich na konci budeme mat n + 20
        for i in range(5):
            f.write("R" + " " + (self.pociatocne_body["R"][i][0] + 5000).__str__() + " " + (
                    self.pociatocne_body["R"][i][1] + 5000).__str__() + "\n")
            f.write("G" + " " + (self.pociatocne_body["G"][i][0] + 5000).__str__() + " " + (
                    self.pociatocne_body["G"][i][1] + 5000).__str__() + "\n")
            f.write("B" + " " + (self.pociatocne_body["B"][i][0] + 5000).__str__() + " " + (
                    self.pociatocne_body["B"][i][1] + 5000).__str__() + "\n")
            f.write("P" + " " + (self.pociatocne_body["P"][i][0] + 5000).__str__() + " " + (
                    self.pociatocne_body["P"][i][1] + 5000).__str__() + "\n")

        flag = 0
        # zapisujeme generovane body s typom triedy(farby) na zaciatku riadka
        # riadok pre bod vyzera takto: farba x y\n
        for i in generovane_body:
            typ_farby = ''
            if flag == 0:
                typ_farby = 'R'
            elif flag == 1:
                typ_farby = 'G'
            elif flag == 2:
                typ_farby = 'B'
            elif flag == 3:
                typ_farby = 'P'

            f.write(typ_farby + " " + i[0].__str__() + " " + i[1].__str__() + "\n")
            flag += 1
            if flag == 4:
                flag = 0
        f.close()
        # na koniec vypiseme pocet generovanych bodov co by nam malo dat n*4, pretoze mame 4 farby
        print("Pocet vygenerovanych bodov: ", generovane_body.__len__())

    # funkcia na klasifikovanie bodu s parametrami zoznam_bodov, x, y, k-pocet susediacich bodov podla ktorych klasifikujeme
    # kNN algoritmus
    def classify(self, zoznam_bodov, x, y, k):
        # budeme is zapisovat body aj s ohodnotenim, co je vzdialenost medzi bodom zo zoznamu a  bodom co chceme klasifikovat
        zoznam_bodov_ohodnoteny = []
        # kedze sme si posunuli hranice, tak chceme uz uvazovat skutocne suradnice
        x -= 5000
        y -= 5000

        # pre kazdy bod zo zoznamu vypocitame vzdialenost od nasho bodu
        # bod zo zoznamu: [farba, x, y]
        for bod in zoznam_bodov:
            bod_x = int(bod[1]) - 5000
            bod_y = int(bod[2]) - 5000
            # podla vzorca pre euklidovu vzdialenost si vypocitame vzdialenost bodov
            euklid = math.sqrt((bod_x - x) ** 2 + (bod_y - y) ** 2)
            # pridame ohodnoteny bod do zoznamu ohodnotenych bodov
            # bod z ohodnoteneho zoznamu: [farba, x, y, vzdialenost od nasho bodu]
            zoznam_bodov_ohodnoteny.append([bod[0], x, y, euklid])

        # zoradenie bodov podla vzdialenosti
        zoznam_bodov_ohodnoteny.sort(key=lambda dlzka: int(dlzka[3]))

        # nechame si v zozname len k potrebnych bodov
        zoznam_bodov_ohodnoteny = zoznam_bodov_ohodnoteny[:k]

        # slovnik pre pocet vyskytov farieb
        farby_v_okoli = {
            "R": 0,
            "G": 0,
            "B": 0,
            "P": 0
        }

        # spocitame si pocet vyskytov farieb
        for bod in zoznam_bodov_ohodnoteny:
            if bod[0] == "R":
                farby_v_okoli["R"] += 1
            elif bod[0] == "G":
                farby_v_okoli["G"] += 1
            elif bod[0] == "B":
                farby_v_okoli["B"] += 1
            elif bod[0] == "P":
                farby_v_okoli["P"] += 1

        # najdeme si maximum
        max_vzdialenost = max(farby_v_okoli.values())
        # ak je ich viac tak vyberieme najblizsiu
        max_farby = [k for k, v in farby_v_okoli.items() if v == max_vzdialenost]

        # vratime farbu
        return max_farby[0]

    # funkcia na preklasifikovanie bodov pomocou kNN algoritmu
    def preklasifikuj_body(self, k):
        f = open("cisla.txt", "r")
        zoznam_bodov = []

        # opat prvych 20 bodov si len nahrame a neklasifikujeme
        for i in range(20):
            tmp = f.readline().split()
            zoznam_bodov.append(tmp)

        # 21. bod a dalsie uz klasifikujeme
        for riadok in f:
            tmp = riadok.split()
            # pomocou kNN algoritmu najdeme farbu
            farba = self.classify(zoznam_bodov, int(tmp[1]), int(tmp[2]), k)

            # ak sa lisi vygenerovana farba s klasifikovanou tak ju zmenime a pripocitame k rozdielnym bodom
            if tmp[0] != farba:
                self.rozdielne_body_po_klasifikacii += 1
                tmp[0] = farba
            zoznam_bodov.append(tmp)
        f.close()

        # klsaifikovane body zapiseme do suboru klasifikovane_cisla.txt
        f = open("klasifikovane_cisla.txt", "w")

        for i in zoznam_bodov:
            pass
            f.write(i[0] + " " + i[1].__str__() + " " + i[2].__str__() + "\n")
        f.close()

    # funkcia na vykreslenie pomocou matplotlib s dvoma moznostami vykreslenia
    def vykresli(self, subor, nazov_suboru):
        R = []
        G = []
        B = []
        P = []

        if subor == 1:
            f = open("cisla.txt", "r")
        elif subor == 2:
            f = open("klasifikovane_cisla.txt", "r")

        for riadok in f:
            tmp = riadok.split()
            if tmp[0] == 'R':
                R.append(tmp)
            elif tmp[0] == 'G':
                G.append(tmp)
            elif tmp[0] == 'B':
                B.append(tmp)
            elif tmp[0] == 'P':
                P.append(tmp)

        plt.scatter([int(bod[1]) - 5000 for bod in R], [int(bod[2]) - 5000 for bod in R], s=0.1, c="r")
        plt.scatter([int(bod[1]) - 5000 for bod in G], [int(bod[2]) - 5000 for bod in G], s=0.1, c="g")
        plt.scatter([int(bod[1]) - 5000 for bod in B], [int(bod[2]) - 5000 for bod in B], s=0.1, c="b")
        plt.scatter([int(bod[1]) - 5000 for bod in P], [int(bod[2]) - 5000 for bod in P], s=0.1, c="m")
        plt.axis([-5000, 5000, -5000, 5000])

        plt.savefig(nazov_suboru, dpi=300)
        # plt.show()
        return

    # testovacie sceenare pre 5020 bodov a pre 20 020 bodov
    # vo vypisoch su neni pripocitane pociatocne body, pretoze sme generovali len 5000, alebo 20 000
    def vsetky_testy(self):
        # 5000 bodovy test pre k = 1,3,15
        print("-" * 100)
        print("Test pre 5000 bodov")
        print("-" * 100)

        n = 1250
        start_time = time.time()
        self.generuj_n_bodov(n)
        print("Generacia bodov:  %s sec" % (time.time() - start_time))

        print("┌-----┐")
        print("|K = 1|")
        print("└-----┘")
        start_time = time.time()
        self.preklasifikuj_body(1)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(1,"graf_5000.png")
        self.vykresli(2,"graf_5000_K1_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        print("┌-----┐")
        print("|K = 3|")
        print("└-----┘")
        start_time = time.time()
        self.preklasifikuj_body(3)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(2, "graf_5000_K3_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        print("┌-----┐")
        print("|K = 7|")
        print("└-----┘")
        start_time = time.time()
        self.preklasifikuj_body(7)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(2, "graf_5000_K7_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        print("┌------┐")
        print("|K = 15|")
        print("└------┘")
        start_time = time.time()
        self.preklasifikuj_body(15)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(2, "graf_5000_K15_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        # 20000 bodovy test pre k = 1,3,15
        print("-" * 100)
        print("Test pre 20000 bodov")
        print("-" * 100)

        n = 5000
        start_time = time.time()
        self.generuj_n_bodov(n)
        print("Generacia bodov:  %s sec" % (time.time() - start_time))

        print("┌-----┐")
        print("|K = 1|")
        print("└-----┘")
        start_time = time.time()
        self.preklasifikuj_body(1)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(1, "graf_20000.png")
        self.vykresli(2, "graf_20000_K1_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        print("┌-----┐")
        print("|K = 3|")
        print("└-----┘")
        start_time = time.time()
        self.preklasifikuj_body(3)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(2, "graf_20000_K3_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        print("┌-----┐")
        print("|K = 7|")
        print("└-----┘")
        start_time = time.time()
        self.preklasifikuj_body(7)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(2, "graf_20000_K7_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0

        print("┌------┐")
        print("|K = 15|")
        print("└------┘")
        start_time = time.time()
        self.preklasifikuj_body(15)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)
        self.vykresli(2, "graf_20000_K15_klasifikovany.png")
        self.rozdielne_body_po_klasifikacii = 0



    # zaciatok
    def __str__(self):
        self.vsetky_testy()
        return " "


print(Priestor())
