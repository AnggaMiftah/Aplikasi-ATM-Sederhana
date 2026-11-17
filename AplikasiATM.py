saldo_atm = 1000000

while True :
    print("=== Aplikasi ATM SEDERHANA ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")
    print("")
    pilihan = (int(input("Pilih Menu 1-4 : ")))

    if pilihan == 1:
        print(f"Sisa Saldo Anda :{saldo_atm:,}")

    elif pilihan == 2:
        nominal2 = (int(input("Masukkan Nominal : ")))
        if nominal2 <= 0:
            print("Nominal Harus Lebih Dari 0!")
        elif saldo_atm <= nominal2:
            print("Saldo Anda Tidak Cukup")
            break
        else:
            saldo_atm -= nominal2
            print(f"Sisa Saldo Anda {saldo_atm:,}")
    elif pilihan == 3:

        nominal3 = (int(input("Masukkan Nominal : ")))
        if nominal3 <= 0:
            print("Nominal Harus Lebih Dari 0!")
        else:
            saldo_atm += nominal3
            print(f"Sisa Saldo Anda {saldo_atm:,}")
            
    elif pilihan == 4:
        break
    else:
        print("Menu Tidak Valid")
        break

    