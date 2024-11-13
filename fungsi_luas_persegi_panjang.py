#fungsi mencari luas persegi panjang
def luaspersegipanjang (panjang, lebar):
    return panjang*lebar

#funngsi mencari keliling persegi panjang
def kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang+lebar)

t=float(input("masukkan panjang :"))
i=float(input("masukkan lebar :"))

hasil_luas = luaspersegipanjang(t,i)
hasil_keliling = kelilingpersegipanjang(t,i)
print("luasnya adalah ", hasil_luas)
print("keliling adalah ", hasil_keliling)
