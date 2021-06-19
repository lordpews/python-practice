class Dad:
    basketball = 233


class Son(Dad):
    dance = 32
    basketball = 32

    def isd(self):
        print(f"i dance like a nitch {self.dance}")


class Grandson(Son):
    dance = 2

    def isd(self):
        print(f"i dance like a ditch balle balle romance on the bhangra floor"
              f"{self.dance}")


daddyji = Dad()

saddyji = Son()

gaddy = Grandson()

gaddy.isd()

saddyji.isd()

print(gaddy.basketball)
# grandson class will first check itself for the basketball attribute if no such attribute is found then it'll check
# the upper level in this case the Son class if there's no such attribute in the upper class then it'll look
# even further but in this case since Son class had the attribute Basketball so it inherited Basketball from Son instead
# of Dad

