from utils import *
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")


def menu_biodata():
    cls()
    print("--------- Biodata Mahasiswa ---------")
    pilihan = input("Lihat Biodata atau Input Biodata? (1/2): ")
    cls()

    if pilihan == "1":
        data = get_biodata()
        if not data:
            print("data mahasiswa belum diinput")
        else:
            print("Nama :", data["nama"])
            print("NIM  :", data["nim"])

    elif pilihan == "2":
        nama = input("Nama : ")
        nim = input("NIM  : ")
        set_biodata(nama, nim)
        print("berhasil ditambahkan")

    else:
        print("Pilihan tidak valid")

    input("")


def input_sks_cli():
    print("--------- Input SKS ---------")

    data = list(map(int, input("SKS: ").split()))
    set_sks(data)
    print("berhasil ditambahkan")


def input_nilai():
    if not get_sks():
        print("SKS belum diinput")
        return

    print("--------- Input Nilai Mahasiswa ---------")
    pilihan = input("Input angka atau huruf? (1/2): ")

    if pilihan == "1":
        nilai = list(map(float, input("Nilai: ").split()))
        if len(nilai) != len(get_sks()):
            print("Jumlah nilai tidak sesuai jumlah SKS")
            return
        set_nilai_dari_angka(nilai)

    elif pilihan == "2":
        nilai = input("Nilai: ").split()
        if len(nilai) != len(get_sks()):
            print("Jumlah nilai tidak sesuai jumlah SKS")
            return
        set_nilai_dari_huruf(nilai)

    else:
        print("Pilihan tidak valid")
        return

    print("berhasil ditambahkan")


def lihat_nilai():
    data = get_biodata()
    if not data:
        print("Biodata belum diinput")
        return
    if not get_nilai():
        print("Nilai belum diinput")
        return

    print("--------- Nilai Mahasiswa ---------")
    print("Nama:", data["nama"])
    print("NIM :", data["nim"])
    print("Nilai:", get_nilai_huruf())


def hitung_ip_cli():
    data = get_biodata()
    if not data or not get_sks() or not get_nilai():
        print("Data belum lengkap")
        return

    ip = hitung_ip()
    print("--------- Index Prestasi (IP) Mahasiswa ---------")
    print(f"Mahasiswa: {data['nim']} {data['nama']}")
    print(round(ip, 2))


