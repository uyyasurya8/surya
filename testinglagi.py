def input_data_karyawan():
    nama = input("Masukkan nama: ")
    kota = input("Masukkan kota: ")
    jabatan = input("Masukkan jabatan: ")
    gaji = int(input("Masukkan gaji: "))

    data_karyawan = {
        "Nama" : nama,
        "Kota" : kota,
        "Jabatan" : jabatan,
        "Gaji" : gaji
    }

    return data_karyawan

hasil = input_data_karyawan()
print(hasil)


def data_karyawan(nama, kota, jabatan, gaji, tipe):
    biodata = {
        "nama": nama,
        "kota": kota,
        "jabatan": jabatan,
        "gaji" : gaji,
        "tipe": tipe,
    }
    return biodata

inputan = data_karyawan("Jordan","Jaksel","dirut",123000789,"organik pengennya")

print(inputan)