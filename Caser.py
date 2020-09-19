from tkinter import *
from random import shuffle
from string import printable as letters




#GUI
root = Tk()
root.title("Caser Cipher Encryption")
root.geometry('400x350')
root.resizable(width=False, height=False)
color = 'gray77'
root.configure(bg=color)


def get_value_encrypt():
    msg = enter.get("1.0",'end-1c')
    output.insert("1.0", encrypt(msg,int(enter_key.get('1.0','end-1c'))))

def get_value_decrypt():
    msg = output.get("1.0",'end-1c')
    output1.insert("1.0", decrypt(msg,int(enter_key.get('1.0','end-1c'))))


    

def get_clear():
    enter.delete("1.0", END)
    enter_key.delete("1.0", END)
    output.delete("1.0", END)
    output1.delete("1.0", END)

label_entry=Label(root,text="Plain Text:",bg=color,font='Helvetica')
label_entry.place(x=40,y=30)

enter = Text(root,height=2,width=20)
enter.place(x=160,y=30)

label_key=Label(root,text="Key:",bg=color,font='Helvetica')
label_key.place(x=40,y=90)

enter_key = Text(root,height=2,width=5)
enter_key.place(x=160,y=90)


label_output=Label(root,text="Encrypted Text:",bg=color,font='Helvetica')
label_output.place(x=40,y=150)

output = Text(root,height=2,width=20)
output.place(x=160,y=150)

label_output1=Label(root,text="Decrypted Text:",bg=color,font='Helvetica')
label_output1.place(x=40,y=210)

output1 = Text(root,height=2,width=20)
output1.place(x=160,y=210)

button = Button(root, text="Encrypt", command=lambda: get_value_encrypt(), width=10, height=2,bg=color,font='Helvetica')
button.place(x=40,y=270)

button1 = Button(root, text="Decrypt", command=lambda: get_value_decrypt(), width=10, height=2,bg=color,font='Helvetica')
button1.place(x=160,y=270)

button_clear = Button(root, text="Clear", command=lambda: get_clear(), width=10, height=2,bg=color,font='Helvetica')
button_clear.place(x=280,y=270)

def encrypt(message, key):
    cipher = [] 
    for c in message:
        position = letters.find(c)
        new_position = position + key % len(letters) 
        encrypted_char = letters[new_position]
        cipher.append(encrypted_char)

    return ''.join(cipher)


def decrypt(cipher, key):
    plain_text = []
    for c in cipher:
        position = letters.find(c)
        position = (position - key) % len(letters)
        plain_text.append(letters[position])
    return ''.join(plain_text)

print(type(enter_key))
root.mainloop()