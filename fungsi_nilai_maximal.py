#fungsi mencari nilai maximal
def max (angka1, angka2, angka3):
    if ((angka1>angka2) and  (angka1>angka2)):
        return angka1
    elif ((angka2>angka1) and (angka2>angka3)):
        return angka2
    else:
        return angka3
    
a= int(input("masukkan angka1: "))
b= int(input("masukkan angka2: "))
c= int(input("masukkan angka3: "))

cek_max = max(a,b,c)
print("nilai maximal dari ", a,"dan",b,"dan",c,"adalah",cek_max)
