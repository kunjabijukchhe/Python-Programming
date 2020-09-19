from tkinter import *
root = Tk()
root.title("Encryption")
root.geometry('300x300')
root.resizable(width=False, height=False)
color = '#f2f2f2'
root.configure(bg='gray77')

def Mono():
    mono=Toplevel()
    from random import shuffle
    from string import printable


    keys = list(printable)
    shuffle_keys = list(printable)
    shuffle(shuffle_keys) 

    maps = dict(zip(keys, shuffle_keys))
    reverse_map = dict(zip(shuffle_keys, keys))

    #GUI
    
    mono.title("Mono Alphabetic Cipher Encryption")
    mono.geometry('400x420')
    mono.resizable(width=False, height=False)
    color = 'gray77'
    mono.configure(bg=color)


    def get_value_encrypt():
        msg = enter.get("1.0",'end-1c')
        output.insert("1.0", encrypt(msg))

    def get_value_decrypt():
        msg = output.get("1.0",'end-1c')
        output1.insert("1.0", decrypt(msg))



    def get_clear():
        enter.delete("1.0", END)
        output.delete("1.0", END)
        output1.delete("1.0", END)

    label_entry=Label(mono,text="Plain Text:",bg=color,font='Helvetica')
    label_entry.place(x=40,y=30)

    enter = Text(mono,height=2,width=20)
    enter.place(x=160,y=30)

    label_output=Label(mono,text="Encrypted Text:",bg=color,font='Helvetica')
    label_output.place(x=40,y=110)

    output = Text(mono,height=2,width=20)
    output.place(x=160,y=110)

    label_output1=Label(mono,text="Decrypted Text:",bg=color,font='Helvetica')
    label_output1.place(x=40,y=190)

    output1 = Text(mono,height=2,width=20)
    output1.place(x=160,y=190)

    button = Button(mono, text="Encrypt", command=lambda: get_value_encrypt(), width=10, height=2,bg=color,font='Helvetica')
    button.place(x=40,y=270)

    button1 = Button(mono, text="Decrypt", command=lambda: get_value_decrypt(), width=10, height=2,bg=color,font='Helvetica')
    button1.place(x=160,y=270)

    button_clear = Button(mono, text="Clear", command=lambda: get_clear(), width=10, height=2,bg=color,font='Helvetica')
    button_clear.place(x=280,y=270)
    
    button_quit = Button(mono, text="Quit", command=mono.destroy, width=10, height=2,bg='#ff0303',font='Helvetica')
    button_quit.place(x=160,y=350)

    def encrypt(message):
        cipher = [] 
        for char in message:
            cipher_char = maps[char]
            cipher.append(cipher_char)
        return ''.join(cipher) 


    def decrypt(cipher):
        plain = [] 
        for cipher_char in cipher:
            plain_char = reverse_map[cipher_char]
            plain.append(plain_char)
        return ''.join(plain)

def Caser():
    caser=Toplevel()
    from random import shuffle
    from string import printable as letters
 #GUI
    
    caser.title("Caser Cipher Encryption")
    caser.geometry('400x420')
    caser.resizable(width=False, height=False)
    color = 'gray77'
    caser.configure(bg=color)


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

    label_entry=Label(caser,text="Plain Text:",bg=color,font='Helvetica')
    label_entry.place(x=40,y=30)

    enter = Text(caser,height=2,width=20)
    enter.place(x=160,y=30)

    label_key=Label(caser,text="Key:",bg=color,font='Helvetica')
    label_key.place(x=40,y=90)

    enter_key = Text(caser,height=2,width=5)
    enter_key.place(x=160,y=90)


    label_output=Label(caser,text="Encrypted Text:",bg=color,font='Helvetica')
    label_output.place(x=40,y=150)

    output = Text(caser,height=2,width=20)
    output.place(x=160,y=150)

    label_output1=Label(caser,text="Decrypted Text:",bg=color,font='Helvetica')
    label_output1.place(x=40,y=210)

    output1 = Text(caser,height=2,width=20)
    output1.place(x=160,y=210)

    button = Button(caser, text="Encrypt", command=lambda: get_value_encrypt(), width=10, height=2,bg=color,font='Helvetica')
    button.place(x=40,y=270)

    button1 = Button(caser, text="Decrypt", command=lambda: get_value_decrypt(), width=10, height=2,bg=color,font='Helvetica')
    button1.place(x=160,y=270)

    button_clear = Button(caser, text="Clear", command=lambda: get_clear(), width=10, height=2,bg=color,font='Helvetica')
    button_clear.place(x=280,y=270)

    button_quit = Button(caser, text="Quit", command=caser.destroy, width=10, height=2,bg='#ff0303',font='Helvetica')
    button_quit.place(x=160,y=350)

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

# Encrytion

button = Button(root, text="Caser Cipher Encryption",command=Caser, width=10, height=2,bg=color,font='Helvetica')
button.place(x=20,y=60,width=260)

button1 = Button(root, text="Mono Alphabetic Cipher Encryption",command=Mono, width=10, height=2,bg=color,font='Helvetica')
button1.place(x=20,y=140,width=260)

button_quit = Button(root, text="Quit", command=root.destroy, width=10, height=2,bg='#ff0303',font='Helvetica')
button_quit.place(x=100,y=220)


root.mainloop()