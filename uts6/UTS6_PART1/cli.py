from utils import *
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def kumpulan_menu():
    while True:

        cls()

        print("Daftar Menu")
        print("1. Konversi nilai ke label")
        print("2. Konversi label ke bobot")
        print("3. Hitung total sks yang diambil")
        print("4. Hitung total nilai")
        print("5. Hitung IPS")
        print("6. Exit")

        pilihan = input("Pilih menu: ")

        cls()
        if pilihan == "1":
            nilai = float(input("Nilai Mahasiswa: "))
            label = konversi_nilai_ke_label(nilai)
            print("Label:", label)
            input("")

        
        elif pilihan == "2":
            label = input("Label Nilai Mahasiswa: ")
            bobot = konversi_label_ke_bobot(label)
            print("Bobot Nilai:", bobot)
            input("")

        elif pilihan == "3":
            total = hitung_total_sks()
            print("Total SKS:", total)
            input("")
        
        elif pilihan == "4":
            total = hitung_total_nilai()
            print("Total Nilai:", round(total, 2))
            input("")
        
        elif pilihan == "5":
            ips = hitung_ips()
            print("IPS:", round(ips, 2))
            input("")

        elif pilihan == "6":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")
