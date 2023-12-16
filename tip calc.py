print("bahsis hesaplamaya hos geldiniz")
total_bill = float(input("hesap ne kadar"))
bahsis_yuuzdesi = int(input("yuzde kac bahsis vermek istersiniz"))
kisi_sayisi = int(input("masada kac kisisiniz"))
bahsisle_total = (total_bill * bahsis_yuuzdesi / 100) + total_bill
kisibasi = round(bahsisle_total / kisi_sayisi, 2)
duzenli_bahsisle_total = round(bahsisle_total, 2)
print(f"bahsisle beraber toplan {duzenli_bahsisle_total} tl tuttu")
print(f"kisi basi {kisibasi}tl odeyebilirisniz")