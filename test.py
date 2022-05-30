# # import openpyxl
# #
# # book = openpyxl.Workbook()
# # sheet = book.active
# # for row in range(1, 10):
# #     step_col = 1
# #     for col in range(1, 10):
# #         sheet.cell(row, step_col).value = "{} * {}".format(col, row)
# #         sheet.cell(row, step_col + 1).value = "{}".format(col * row)
# #         step_col += 2
# # book.save("test.xlsx")
# # book.close()
# #
# # # import openpyxl
# # #
# # # users = []
# # # users_book = openpyxl.open("test.xlsx")
# # # sheet = users_book.active
# # # user = input("enter name: ")
# # # users.append(user)
# # # print("added")
# # # sheet[1][0].value = user
# # # row = 2
# # # while True:
# # #     choice = input("continue or no?: ")
# # #     if choice == "no":
# # #         break
# # #     else:
# # #         user = input("enter name: ")
# # #         users.append(user)
# # #         sheet[row][0].value = user
# # #         print("added")
# # #         row += 1
# # #
# # # users_book.save("test.xlsx")
# # # users_book.close()
# #
# from datetime import datetime
#
#
# class Express:
#     def __init__(self, name, surname, passport_seriya, ketuvchi_st, boruvchi_st, vagon_turi, masofa):
#         self.name = name
#         self.surname = surname
#         self.passport_seriya = passport_seriya
#         self.ketuvchi_st = ketuvchi_st
#         self.boruvchi_st = boruvchi_st
#         self.dateTime = datetime.now()
#         self.vagon_turi = vagon_turi
#         self.masofa = masofa
#
#     def bilet_narxi(self):
#         return self.masofa * 0.2
#
#     def vaqti(self):
#         return int(self.masofa) // 60
#
#
# vagonlar = {"plastkart": 20, "Ekonom": 10, "Lyuks": 30}
# stansiyalar = ["Qongirot", "Uchkoprik", "Samarqand", "Baxt", "Sirdaryo", "Buxoro", "Xiva"]
#
# birinchi_name = input("yuboruvchi ismi: ")
# birinchi_surname = input("yuboruvchi familiyasi: ")
# birinchi_pas_seriya = input("yuboruvchi Passport seriyasi: ")
#
# print("Ketuvchi stansiyani tanlang")
# for i, stansiya in enumerate(stansiyalar, 1):
#     print("{}. {}".format(i, stansiya))
# choice = int(input("stansiyani tanlang: "))
# birinchi_ketuvchi_st_name = stansiyalar[choice - 1]
#
# stansiyalar.remove(birinchi_ketuvchi_st_name)
#
# print("Boruvchi stansiyani tanlang")
# for i, stansiya in enumerate(stansiyalar, 1):
#     print("{}. {}".format(i, stansiya))
# choice = int(input("stansiyani tanlang: "))
# birinchi_boruvchi_st_name = stansiyalar[choice - 1]
#
# print("vagon turini tanlang")
# for i, vagon in enumerate(vagonlar, 1):
#     print("{}. {}".format(i, vagon))
# choice = int(input("vagonni tanlang: "))
# for i, vagon in enumerate(vagonlar, 1):
#     if choice == i:
#         birinchi_vagon_turi = vagon
# birinchi_vagon_turi = "plastkart"
#
# birinchi_masofa = int(input("masofani kiriting (km): "))
#
# A1 = Express(birinchi_name, birinchi_surname, birinchi_pas_seriya, birinchi_ketuvchi_st_name, birinchi_boruvchi_st_name, birinchi_vagon_turi, birinchi_masofa,)
#
# print("=========================================")
# print(f"Hurmatli {A1.name, A1.surname} Sizning yukingiz jonatildi!!!")
# print("Info: ")
# print(f"Yo'lovchi F.I: {A1.name, A1.surname}")
# print(f"Passport seriyasi: {A1.passport_seriya}")
# print(f"Vagon turi: {A1.vagon_turi}")
# print(f"Ketuvchi stansiya: {A1.ketuvchi_st}")
# print(f"Boruvchi stansiya: {A1.boruvchi_st}")
# print(f"Masofa: {A1.masofa}")
# print("==============================================")
# print(f"Yo'lda yurish Vaqti: {A1.vaqti()} soat")
# print(f"Bilet narxi: ${A1.bilet_narxi() + vagonlar[birinchi_vagon_turi]}")


from datetime import datetime


class Diskor:
    def __init__(self, name, jonatuvchi_st_name, vagon_turi, yuk_turi, massa, sostav, qabul_qiluvchi_st_name, km):
        self.name = name
        self.jonatuvchi_st_name = jonatuvchi_st_name
        self.vagon_turi = vagon_turi
        self.yuk_turi = yuk_turi
        self.massa = massa
        self.sostav = sostav
        self.qabul_qiluvchi_st_name = qabul_qiluvchi_st_name
        self.km = km
        self.dateTime = datetime.now()

    def umumiy_narxi(self):
        return str(int(self.km) * 5 + int(self.massa) * 0.5)

    def yuk_narxi(self):
        return str(int(self.massa) * 0.5)

    def vaqti(self):
        return str(int(self.km) // 60 - self.dateTime.hour)


yuklar = ["Neft", "komir", "benzin", "oltin", "kumush"]
vagonlar = ["sisterna", "yopiq vagon", "yarim ochiq", "ochiq", "platforma"]

birinchi_name = input("yuboruvchi F.I.O: ")
birinchi_jonatuvchi_st_name = input("jonatuvchi_st_name: ")

print("yuk_turini tanlang")
for i, yuk in enumerate(yuklar, 1):
    print("{}. {}".format(i, yuk))
choice = int(input("yukni tanlang: "))
birinchi_yuk_turi = yuklar[choice - 1]

print("vagon turini tanlang")
for i, vagon in enumerate(vagonlar, 1):
    print("{}. {}".format(i, vagon))
choice = int(input("vagonni tanlang: "))
birinchi_vagon_turi = vagonlar[choice - 1]

birinchi_massa = input("massa: ")
birinchi_sostav = input("sostav: ")
birinchi_qabul_qiluvchi_st_name = input("qabul_qiluvchi_st_name: ")
birinchi_masofa = input("masofani kititing (km): ")

A1 = Diskor(birinchi_name, birinchi_jonatuvchi_st_name, birinchi_vagon_turi, birinchi_yuk_turi, birinchi_massa,
            birinchi_sostav, birinchi_qabul_qiluvchi_st_name, birinchi_masofa)

print("=========================================")
print(f"Hurmatli {A1.name} Sizning yukingiz jonatildi!!!")
print("Info: ")
print(f"Jo'natilivchi stansiya nomi: {A1.jonatuvchi_st_name}")
print(f"Qabul qiluvchi stansiya nomi: {A1.qabul_qiluvchi_st_name}")
print(f"Vagon turi: {A1.vagon_turi}")
print(f"Yuk turi: {A1.yuk_turi}")
print(f"Yuk og'irligi: {A1.massa}")
print(f"Sostav: {A1.sostav}")
print(f"Masofa: {A1.km}")
print("==============================================")
print(f"Yuk yetkazish vaqti: {A1.vaqti()} soat")
print(f"Yukning ogirligiga qarab narxi: ${A1.yuk_narxi()}")
print(f"Umumiy narxi: ${A1.umumiy_narxi()}")