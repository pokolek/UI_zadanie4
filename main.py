import random
import time


class Priestor:
    def __init__(self):
        self.pociatocne_body = {
            'R': [(-4500, -4400), (-4200, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
            'G': [(4500, -4400), (4200, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
            'B': [(-4500, 4400), (-4200, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
            'P': [(4500, 4400), (4200, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
        }

        self.vsetky_body = {
            'R': [(-4500, -4400), (-4200, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
            'G': [(4500, -4400), (4200, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
            'B': [(-4500, 4400), (-4200, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
            'P': [(4500, 4400), (4200, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
        }

        self.rozsahy = {
            "rx": (0, 5500),
            "ry": (4500, 10000),
            "gx": (4500, 10000),
            "gy": (4500, 10000),
            "bx": (0, 5500),
            "by": (0, 5500),
            "px": (4500, 10000),
            "py": (0, 5500),
        }

    def classify(self, x, y, k):
        print(x, y, k)
        return

    def generate_numbers(self, n):
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
            else:
                print("cicka")

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

        # print("Pocet generovanych bodov: ", pocet_bodov)

        f = open("cisla.txt", "w")

        index_bodu = 0
        while index_bodu != n:
            generovane_body.append(list(R)[index_bodu])
            generovane_body.append(list(G)[index_bodu])
            generovane_body.append(list(B)[index_bodu])
            generovane_body.append(list(P)[index_bodu])

            index_bodu += 1

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
        # print(R)
        # print(G)
        # print(B)
        # print(P)
        # print(generovane_body)
        print("Dlzka vygenerovaneho pola: ", generovane_body.__len__())

    # zaciatok
    def __str__(self):
        start_time = time.time()
        self.generate_numbers(5000)
        print("--- %s seconds ---" % (time.time() - start_time))
        return " "


print(Priestor())
