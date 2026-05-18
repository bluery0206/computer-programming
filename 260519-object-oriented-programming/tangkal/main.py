from manok import Manok
from lugwa import Lugwa
from tangkal import Tangkal


if __name__ == "__main__":
    manok_1 = Manok("Bisaya")
    manok_2 = Manok("Bisaya")
    manok_3 = Manok("Bisaya")
    manok_4 = Manok("Tagalog")
    manok_5 = Manok("Tagalog")

    # lugwa
    lugwa_1 = Lugwa("Lugwa 1")
    lugwa_2 = Lugwa("Lugwa 2")
    lugwa_3 = Lugwa("Lugwa 3")

    # add ug manok sa lugwa
    lugwa_1.add_manok(manok_1)

    lugwa_2.add_manok(manok_2)
    lugwa_2.add_manok(manok_3)
    lugwa_2.add_manok(manok_4)

    lugwa_3.add_manok(manok_5)

    # tangal object and adding of lugwa
    tangkal = Tangkal("Tangkal 1")
    tangkal.add_lugwa(lugwa_1)
    tangkal.add_lugwa(lugwa_2)
    tangkal.add_lugwa(lugwa_3)

    print(tangkal.lugwas)
