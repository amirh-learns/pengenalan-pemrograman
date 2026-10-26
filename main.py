def main():
#     nama_barang = str(input("Nama Barang: "))
#     harga_satuan = int(input("Harga Barang: "))
#     jumlah_beli = int(input("Jumlah Barang: "))

#     subtotal = harga_satuan * jumlah_beli

#     print()
#     print(f"Harga yang harus dibayar untuk {jumlah_beli}x {nama_barang}: {rupiah(subtotal)}")
#
    nama_barang = str(input("Nama barang: "))
    harga_satuan = float(input("Harga barang: "))
    jumlah_beli = int(input("Jumlah barang: "))
    input_diskon = int(input("Masukkan diskon: "))
    syarat_diskon = int(input("Syarat diskon: "))

    subtotal = harga_satuan * jumlah_beli

    if (subtotal > syarat_diskon):
        diskon = subtotal * (input_diskon / 100)
        total = subtotal - diskon

        print("===============================")
        print(f"Subtotal: Rp{subtotal:,.0f}")
        print(f"Kamu mendapatkan diskon {input_diskon}%!")
        print(f"Harga   : Rp{total:,.0f}".replace(",", "."))
        print("===============================")
    else:
        print("===============================")
        print(f"Nama barang: {nama_barang}")
        print(f"Subtotal   : Rp{subtotal:,.0f}".replace(",", "."))
        print("===============================")

main()
