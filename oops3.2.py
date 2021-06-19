class agent:
    rarity = "covert"
    def __init__(self,n,p,po):
        self.name = n
        self.price = p
        self.po = po

    def info(self):
        print(f"agent is {self.name} \n"
              f"price is {self.price} \n"
              f"rarity is {self.rarity} \n"
              f"possesion : {self.po} \n")

ava = agent("ava",500,"owned")
muhlik = agent("prof muhlik",23232 ,"not owned" )
# ava.price = 500
# ava.name = "ava"
# muhlik.name = "muhlik"
# muhlik.price = 21150
# muhlik.rarity = "epic"

# print(agent.__dict__)
(ava.info())
(muhlik.info())
