import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=yBmquVEmVaA&ab_channel=Maverick51")
img.save("yt.png")

