import qrcode

data = input("Enter Text of URL: ").strip()
file_name = input("Enter file name for save qrcode: ")

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(data)

image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)

print(f"Your qrcode save as {file_name}")