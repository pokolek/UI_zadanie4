import random
import time
import matplotlib.pyplot as plt
import math


class Priestor:
    def __init__(self):
        self.pociatocne_body = {
            'R': [(-4500, -4400), (-4200, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
            'G': [(4500, -4400), (4200, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
            'B': [(-4500, 4400), (-4200, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
            'P': [(4500, 4400), (4200, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
        }

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

        self.rozdielne_body_po_klasifikacii = 0

    def generuj_n_bodov(self, n):
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

            pocet_bodov = 0
            while pocet_bodov != n:
                # pravdepodobnost je nahodna ak je 1 tak ideme mimo pozadovany interval pre farbu
                pravdepodobnost = random.randint(1, 100)

                # testovanie pravdepodobnosti 1 alebo 99 percent

                if pravdepodobnost == 1:  # ak je pravdepodobnost 1 percento, tak generujeme bod z lubovolneho intervalu
                    x = random.randint(0, 10000)
                    y = random.randint(0, 10000)

                    tmp_suradnice = (x, y)
                    if tmp_suradnice not in generovane_body \
                            and tmp_suradnice not in R \
                            and tmp_suradnice not in G \
                            and tmp_suradnice not in B \
                            and tmp_suradnice not in P:
                        if i == 0:
                            R.add(tmp_suradnice)
                        elif i == 1:
                            G.add(tmp_suradnice)
                        elif i == 2:
                            B.add(tmp_suradnice)
                        elif i == 3:
                            P.add(tmp_suradnice)
                        pocet_bodov += 1

                else:  # ak je pravdepodobnost 99 percent, tak generujeme cislo z pozadovaneho intervalu
                    x = random.randint(rozsah_x[0], rozsah_x[1])
                    y = random.randint(rozsah_y[0], rozsah_y[1])

                    tmp_suradnice = (x, y)
                    if tmp_suradnice not in generovane_body \
                            and tmp_suradnice not in R \
                            and tmp_suradnice not in G \
                            and tmp_suradnice not in B \
                            and tmp_suradnice not in P:
                        if i == 0:
                            R.add(tmp_suradnice)
                        elif i == 1:
                            G.add(tmp_suradnice)
                        elif i == 2:
                            B.add(tmp_suradnice)
                        elif i == 3:
                            P.add(tmp_suradnice)
                        pocet_bodov += 1

        f = open("cisla.txt", "w")

        index_bodu = 0
        while index_bodu != n:
            generovane_body.append(list(R)[index_bodu])
            generovane_body.append(list(G)[index_bodu])
            generovane_body.append(list(B)[index_bodu])
            generovane_body.append(list(P)[index_bodu])

            index_bodu += 1

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
        print("Pocet vygenerovanych bodov: ", generovane_body.__len__())

    def classify(self, zoznam_bodov, x, y, k):
        zoznam_bodov_ohodnoteny = []
        x -= 5000
        y -= 5000

        for bod in zoznam_bodov:
            bod_x = int(bod[1]) - 5000
            bod_y = int(bod[2]) - 5000
            euklid = math.sqrt((bod_x - x) ** 2 + (bod_y - y) ** 2)
            zoznam_bodov_ohodnoteny.append([bod[0], x, y, euklid])

        # zoradenie bodov podla vzdialenosti
        zoznam_bodov_ohodnoteny.sort(key=lambda dlzka: int(dlzka[3]))

        zoznam_bodov_ohodnoteny = zoznam_bodov_ohodnoteny[:k]

        farby_v_okoli = {
            "R": 0,
            "G": 0,
            "B": 0,
            "P": 0
        }

        for bod in zoznam_bodov_ohodnoteny:
            if (bod[0] == "R"):
                farby_v_okoli["R"] += 1
            elif (bod[0] == "G"):
                farby_v_okoli["G"] += 1
            elif (bod[0] == "B"):
                farby_v_okoli["B"] += 1
            elif (bod[0] == "P"):
                farby_v_okoli["P"] += 1

        max_vzdialenost = max(farby_v_okoli.values())
        max_farby = [k for k, v in farby_v_okoli.items() if v == max_vzdialenost]

        return max_farby[0]

    def preklasifikuj_body(self, k):
        f = open("cisla.txt", "r")
        zoznam_bodov = []

        for i in range(20):
            tmp = f.readline().split()
            zoznam_bodov.append(tmp)

        for riadok in f:
            tmp = riadok.split()
            farba = self.classify(zoznam_bodov, int(tmp[1]), int(tmp[2]), k)

            if tmp[0] != farba:
                self.rozdielne_body_po_klasifikacii += 1
                tmp[0] = farba
            zoznam_bodov.append(tmp)
        f.close()

        f = open("klasifikovane_cisla.txt", "w")

        for i in zoznam_bodov:
            pass
            f.write(i[0] + " " + i[1].__str__() + " " + i[2].__str__() + "\n")
        f.close()

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
        if subor == 1:
            plt.savefig(nazov_suboru, dpi=300)
        elif subor == 2:
            plt.savefig("graf_klasifikovany.png", dpi=300)
        # plt.show()
        return

    def vsetky_testy(self):
        print("Test pre 5000 bodov")
        print("-" * 100)
        start_time = time.time()
        n = 1250
        self.generuj_n_bodov(n)
        print("Generacia bodov:  %s sec" % (time.time() - start_time))
        self.preklasifikuj_body(3)
        print("Klasifikacia bodov:  %s sec" % (time.time() - start_time))
        percentualna_zhoda = self.rozdielne_body_po_klasifikacii / (n * 4 + 20)
        percentualna_zhoda *= 100
        percentualna_zhoda = 100 - percentualna_zhoda
        print("Percentualna odlisnost od vygenerovanych cisiel po klasifikacii: %.2f %%" % percentualna_zhoda)
        print("Pocet ozdielnych bodov po klasifikacii: %d" % self.rozdielne_body_po_klasifikacii)


        self.vykresli(1,"graph.png")

    # zaciatok
    def __str__(self):
        self.vsetky_testy()
        return " "


print(Priestor())
