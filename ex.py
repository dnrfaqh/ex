import random

def main():
    saldo = 10000
    print("Selamat datang di TEBAK ANGKA UNTUNG-UNTUNGAN!")
    print("Tebak angka dari 1 sampai 10. Taruhan: 2000 koin tiap kali main.\n")

    while saldo >= 2000:
        try:
            tebakan = int(input("Masukkan angka tebakanmu (1-10): "))
            if tebakan < 1 or tebakan > 10:
                print("Angka harus antara 1-10!\n")
                continue
        except ValueError:
            print("Input harus angka!\n")
            continue

        saldo -= 2000
        angka_asli = random.randint(1, 10)

        # Sistem curang: jika tebakan benar, ubah angka_asli
        if tebakan == angka_asli:
            angka_asli = (angka_asli % 10) + 1  # pasti berbeda dari tebakan

        print(f"Angka yang keluar: {angka_asli}")
        if tebakan == angka_asli:
            print("Kamu menang! +4000 koin\n")
            saldo += 4000
        else:
            print("Kamu kalah.\n")

        print(f"Sisa saldo: {saldo} koin\n")

    print("Saldo kamu habis. Terima kasih sudah bermain (dan kalah).")

if __name__ == "__main__":
    main()
