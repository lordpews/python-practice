class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.mail = f"{self.fname}.{self.lname}@jongu.coom"

    def explain(self):
        return f"my name is {self.fname} {self.lname}"

    @property
    def mail(self):
        if self.fname == None or self.lname == None:
            return f"email is not set"
        return f"{self.fname}.{self.lname}@jongu.coom"

    @mail.setter
    def mail(self, str):
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @mail.deleter
    def mail(self):
        self.fname = None
        self.lname = None


hsp = Employee("holo", "jholo")
lsp = Employee("lolo", "jholo")

hsp.fname = "mosco"

# hsp.mail = "lua.mua@dhuan.com"
print(hsp.mail)
print(hsp.fname)
print(hsp.lname)
del hsp.mail
print(hsp.mail)
