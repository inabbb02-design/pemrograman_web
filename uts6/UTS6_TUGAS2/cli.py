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
        lihat_biodata()
    elif pilihan == "2":
        input_biodata()
    else:
        print("Pilihan tidak valid")

    input("")


def kumpulan_menu():
    while True:
        cls()
        print("--------- Menu Utama ---------")
        print("1. Biodata")
        print("2. SKS")
        print("3. Input Nilai")
        print("4. Lihat Nilai")
        print("5. Lihat IP")
        print("6. Keluar")

        pilihan = input("Pilihan: ")
        cls()

        if pilihan == "1":
            menu_biodata()

        elif pilihan == "2":
            input_sks()
            input("")

        elif pilihan == "3":
            input_nilai()
            input("")

        elif pilihan == "4":
            lihat_nilai()
            input("")

        elif pilihan == "5":
            hitung_ip()
            input("")

        elif pilihan == "6":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")
            input("")
