def rupiah(nilai: int):
    angka_str = str(int(nilai))
    reversed_str = angka_str[::-1]

    slice = [
        reversed_str[i : i + 3] for i in range(0, len(reversed_str), 3)
    ]

    hasil = ".".join(slice)[::-1]

    return f"Rp{hasil}"
