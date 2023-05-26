import customtkinter
import qrcode 
from PIL import Image
import time

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root= customtkinter.CTk()
root.geometry("500*350")

def qr_code():
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
    qr.add_data(entry1.get())
    qr.make(fit=True)
    img=qr.make_image(fill_color=entry3.get(),back_color=entry2.get())
    filename = f"qr_code_{int(time.time())}.png"
    img.save(filename)

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="QR-Code")
label.pack(pady=12,padx=10)

entry1=customtkinter.CTkEntry(master=frame,placeholder_text="URL")
entry1.pack(pady=12,padx=10)

entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Background Color")
entry2.pack(pady=12,padx=10)

entry3=customtkinter.CTkEntry(master=frame,placeholder_text="Foreground Color")
entry3.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=frame,text="Generate",command=qr_code)
button.pack(pady=12,padx=10)

root.mainloop()