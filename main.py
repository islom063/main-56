class talaba:
    def __init__(self, ism, fm):
        self.ism = ism
        self.fm = fm
    def chiqar(self ):
        return f"{self.ism} {self.fm}"

a = talaba('islom', 'baxtiyorov')
print(a.chiqar())