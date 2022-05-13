
sachovnice = []
kacko = [-1, -1]


def nacti_sachovnici():
    global kacko
    with open("vstup.txt") as soubor:
        deskatext = soubor.read()
        radky = deskatext.split("\n")
        r = 0
        for radek in radky:
            mista = []
            m = 0
            for jednotka in radek:
                if(jednotka == "K"):
                    kacko = [r, m]
                mista.append(jednotka)
                m = m + 1
            r = r + 1
            sachovnice.append(mista)


def napis_sousedy():
    if(kacko[0] == -1 or kacko[1] == -1): return None
    pozice = [[kacko[0] + 2, kacko[1] - 1], [kacko[0] + 2, kacko[1] + 1],
    [kacko[0] - 2, kacko[1] - 1], [kacko[0] - 2, kacko[1] + 1],
    [kacko[0] + 1, kacko[1] - 2], [kacko[0] + 1, kacko[1] + 2],
    [kacko[0] - 1, kacko[1] - 2], [kacko[0] - 1, kacko[1] + 2]]
    for jednotka in pozice:
        try:
            if(sachovnice[jednotka[0]][jednotka[1]] and sachovnice[jednotka[0]][jednotka[1]] != "X") and jednotka[0] >= 0 and jednotka[1] >= 0:
                sachovnice[jednotka[0]][jednotka[1]] = "1"
        except:
            None
        

def vypis_to():
    for radek in sachovnice:
        print("".join(radek))

nacti_sachovnici() 
napis_sousedy()
vypis_to()

