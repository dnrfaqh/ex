import random

def main():
    saldo = 15000
    ronde = 0
    print("🎰 Selamat datang di TEBAK ANGKA PALSU!")
    print("Tebak angka dari 1 sampai 10. Taruhan: 2000 koin setiap ronde.\n")

    while saldo >= 2000:
        try:
            tebakan = int(input("Tebakanmu (1-10): "))
            if tebakan < 1 or tebakan > 10:
                print("Angka harus antara 1-10!\n")
                continue
        except ValueError:
            print("Input tidak valid!\n")
            continue

        saldo -= 2000
        ronde += 1
        angka_asli = random.randint(1, 10)

        # Manipulasi sistem
        if saldo < 3000:
            # Biarkan menang, tapi hanya kasih hadiah kecil
            if tebakan == angka_asli:
                hadiah = 1000
                print("Kamu MENANG... Tapi cuma dapet 1000 koin.\n")
                saldo += hadiah
                print(f"Saldo sekarang: {saldo} koin\n")
                continue
            else:
                angka_asli = (tebakan % 10) + 1  # pastikan beda biar kalah

        elif ronde % 5 == 0:
            # Buat pemain menang, tapi hadiahnya tetap lebih kecil
            angka_asli = tebakan
            hadiah = 1500
            print("Kamu MENANG! (Hadiah spesial) +1500 koin\n")
            saldo += hadiah
            print(f"Saldo sekarang: {saldo} koin\n")
            continue

        else:
            # Kalahkan pemain
            if tebakan == angka_asli:
                angka_asli = (angka_asli % 10) + 1

        print(f"Angka keluar: {angka_asli}")
        if tebakan == angka_asli:
            print("Kamu menang! +4000 koin\n")
            saldo += 4000
        else:
            print("Kamu kalah.\n")

        print(f"Saldo sekarang: {saldo} koin\n")

    print("Saldo kamu habis. Coba top up? 😏")

if __name__ == "__main__":
    main()
