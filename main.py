# class talaba:
#     def __init__(self, ism, fm):
#         self.ism = ism
#         self.fm = fm
#     def chiqar(self ):
#         return f"{self.ism} {self.fm}"
#
#     def faqat_ism(self):
#         return self.ism
#
# a = talaba('islom', 'baxtiyorov')
# print(a.chiqar())



class Chiqar:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def Tekshir(self):
        return f"{self.ism} {self.familiya}"

    def faqat_ism(self):
        return self.ism

a = Chiqar(ism='ALi', familiya="Jabborov")
print(a.faqat_ism())