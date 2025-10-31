class  TreasureKey:
    pass

class Pirate:
    def __init__(self, name, key):
        self.name = name
        self.key = key


class Treasure:
    def __init__(self, _secret_treasure, _secret_treasure_key):
        self.secret_treasure = _secret_treasure
        self.treasure_key = _secret_treasure_key

    def open_treasure_box(self, pirate):
        if pirate.key != self.secret_treasure:
            print("Klick klick klick")



treasure_key_1 = TreasureKey()
treasure_key_2 = TreasureKey()
treasure_key_3 = TreasureKey()
treasure_key_4 = TreasureKey()

treasure = Treasure("Gold", treasure_key_3)

pirate_1 = Pirate("Jack Sparrow", treasure_key_3)
pirate_2 = Pirate("Max Boulevard", treasure_key_4)
pirate_3 = Pirate("Mickael Jackson", treasure_key_2)
pirate_4 = Pirate("Allan Dolmen", treasure_key_1)


pirates = [pirate_1, pirate_2, pirate_3, pirate_4]
for pirate in pirates:
    treasure.open_treasure_box(pirate)