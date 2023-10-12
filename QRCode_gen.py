import qrcode as qr
text=input("Enter QR Data : ")
img= qr.make(text)
img.save("qrcode.png")