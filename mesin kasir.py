total = []

def format_rupiah(value):
    return f"Rp{value:,.0f}".replace(",", ".")

def daftar_barang():
    # Menggunakan dictionary untuk menyimpan barang dan harga
    items = {
        1: ("Roti", 7000),
        2: ("Kopi", 5500),
        3: ("Sabun", 4000),
        4: ("Gula", 12000),
        5: ("Beras", 19000)
    }
    
    print("--------------------------")
    print("         TOKO ANWAR      ")
    print("--------------------------")
    print(" No | Nama Barang  | Harga")
    print("--------------------------")
    for kode, (nama, harga) in items.items():
        print(f" {kode}  | {nama:<10} | {format_rupiah(harga)}")
    print("--------------------------")
    
    kode = input("Masukkan angka barang  : ")
    while not kode.isdigit() or int(kode) not in items:
        print("Kode barang tidak valid! Silakan masukkan angka yang valid.")
        kode = input("Masukkan angka barang  : ")

    kode = int(kode)
    jumlah = input(f"Masukkan jumlah {items[kode][0]}: ")
    while not jumlah.isdigit():
        print("Jumlah harus berupa angka. Silakan masukkan jumlah yang valid.")
        jumlah = input(f"Masukkan jumlah {items[kode][0]}: ")
    
    jumlah = int(jumlah)
    total_harga = items[kode][1] * jumlah
    total.append(total_harga)
    tanya()

def tanya():
    tanya = input("\n-------------------------------\nIngin tambah barang? [y/t] : ")
    while tanya.lower() not in ['y', 't']:
        print("Pilihan yang Anda masukkan salah! Silakan masukkan 'y' atau 't'.")
        tanya = input("Ingin tambah barang? [y/t] : ")
    
    if tanya.lower() == "y":
        daftar_barang()
    elif tanya.lower() == "t":
        akhir()

def akhir():
    subtotal = sum(total)
    print("\n-------------------------------")
    print(f"SubTotal         : {format_rupiah(subtotal)}")
    
    diskon = subtotal * 10 / 100 if subtotal > 10000 else 0 
    #jika harga total pembayaran lebih dari 10rb maka akan mendapatkan diskon 10%, jika tidak maka 0
    print(f"Potongan Harga   : {format_rupiah(diskon)}")
    total_akhir = subtotal - diskon
    print(f"Total            : {format_rupiah(total_akhir)}")
    print("-------------------------------")

    bayar = input("Bayar            :  ")
    while not bayar.isdigit():
        print("Jumlah bayar harus berupa angka. Silakan masukkan jumlah yang valid.")
        bayar = input("Bayar            :  ")
    
    bayar = int(bayar)
    kembalian = bayar - total_akhir
    print(f"Kembalian        : {format_rupiah(kembalian)}")
    print("-------------------------------")
    print("          Terima Kasih         ")
    print("          Datang lagi          ")
    print("-------------------------------")

# Jalankan program
daftar_barang()
