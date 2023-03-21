class Creature:
    _health :int
    _stamina :int
    _weigth :int
    _melee :int

    def __init__(self, health :int, stamina :int, weigth :int, melee :int) -> None:
        self._health = health
        self._stamina = stamina
        self._weigth = weigth
        self._melee = melee

    def Get_Health(self) ->int:
        return self._health
    
    def Get_Stamina(self) ->int:
        return self._stamina
    
    def Get_Weigth(self) ->int:
        return self._weigth
    
    def Get_Melee(self) ->int:
        return self._melee
    
    def Set_Health(self) ->int:
        return self._health
    
    def Set_Stamina(self) ->int:
        return self._stamina
    
    def Set_Weigth(self) ->int:
        return self._weigth
    
    def Set_Melee(self) ->int:
        return self._melee
    


def AddCreature() -> Creature:
    gender=input("Creature gender:")
    healt=input("Creature healt:")
    stamina=input("Creature stamina:")
    weight=input("Creature weight:")
    melee=input("Creature melee:")
    return Creature(healt, stamina, weight, melee)


def main():
    creatures = []
    while True:
        creatures.append(AddCreature())
        print('\n')
        creatures.append(AddCreature())
        
        word="Healt"
        for min,max in zip(creatures[0].Get_Health(),creatures[1].Get_Health()):
            if max<min:
                print(f"{word} {min} creature1")
            elif max>min:
                print(f"{word} {max} creature2")
            else:
                print(f"{word} {max} same")

            if word=="Healt":
                word=word.replace("Healt", "Stamina")
            elif word=="Stamina":
                word=word.replace("Stamina","Weight")
            else:
                word=word.replace("Weight","Melee")

            if word=="Healt":
                word=word.replace("Healt", "Stamina")
            elif word=="Stamina":
                word=word.replace("Stamina","Weight")
            else:
                word=word.replace("Weight","Melee")

if __name__ == "__main__":
    main()