def check_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return "Kabisat"
    else:
        return "Bukan Kabisat"

print("output:", check_kabisat(1201))

