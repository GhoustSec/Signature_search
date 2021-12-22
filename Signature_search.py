png_sign = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

signature_base = {
    png_sign:'png',
}

def search():
    file = open("input", "rb")
    input_data = file.read()

    if png_sign in input_data:
        print(signature_base.get(png_sign), "started from byte", hex(input_data.index(png_sign)))

    file.close()

search()