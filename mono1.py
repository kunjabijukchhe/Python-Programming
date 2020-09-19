from tkinter import *
from random import shuffle
from string import printable
Devanagari_alphabets =["ै","ौ","ृ","ु","ू","ि","ी","ो","ा","े","क","ख","ग","घ","ङ","च","छ","ज","झ","ण","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","व","स","श","ष","ह","ञ"]
English_alphabets=list(printable)

#GUI
root = Tk()
root.title("INDIVIDUAL PROJECT WORK")
root.geometry('400x380')
root.resizable(width=False, height=False)
color = 'gray77'
root.configure(bg=color)


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



#Maps for Devanagari_alphabets
keys_devanagari=list(Devanagari_alphabets)
shuffled_keys_devanagari=list(Devanagari_alphabets)
shuffle(shuffled_keys_devanagari)
 
#Maps for English_alphabets
keys_english=list(English_alphabets)
shuffled_keys_english=list(English_alphabets)
shuffle(shuffled_keys_english)
 
#dict for Devanagari_alphabets maps
maps_devanagari=dict(zip(keys_devanagari,shuffled_keys_devanagari))
reversed_maps_devanagari=dict(zip(shuffled_keys_devanagari,keys_devanagari))
 
#dict for English_alphabets maps
maps_english=dict(zip(keys_english,shuffled_keys_english))
reversed_maps_english=dict(zip(shuffled_keys_english,keys_english))
 
def encrypt(message):
    cipher=[]    
    for alphabets in message:
        if alphabets in Devanagari_alphabets:
                    cipher_devanagari=maps_devanagari[alphabets]
                    cipher.append(cipher_devanagari)
        elif alphabets in English_alphabets:
                    cipher_english=maps_english[alphabets]
                    cipher.append(cipher_english)
    return"".join(cipher)
 
def decrypt(ciphers):
    plaintext=[]
    for alphabets in ciphers:
        if alphabets in Devanagari_alphabets:
                    plaintext_devanagari=reversed_maps_devanagari[alphabets]
                    plaintext.append(plaintext_devanagari)
        elif alphabets in English_alphabets:
                    plaintext_english=reversed_maps_english[alphabets]
                    plaintext.append(plaintext_english)
    return"".join(plaintext)

label_heading = Label(root, text="Mono Alphabetic Cipher Encryption", bg=color, font=('Helvetica', 15, 'bold'))
label_heading.place(x=35, y=20)

label_entry = Label(root, text="Plain Text:", bg=color, font='Helvetica')
label_entry.place(x=40, y=80)

enter = Text(root, height=2, width=20)
enter.place(x=160, y=75)

label_output = Label(root, text="Encrypted Text:", bg=color, font='Helvetica')
label_output.place(x=40, y=160)

output = Text(root, height=2, width=20)
output.place(x=160, y=155)

label_output1 = Label(root, text="Decrypted Text:", bg=color, font='Helvetica')
label_output1.place(x=40, y=240)

output1 = Text(root, height=2, width=20)
output1.place(x=160, y=235)

button = Button(root, text="Encrypt", command=lambda: get_value_encrypt(), width=10, height=2,
                font='Helvetica')
button.place(x=40, y=300)

button1 = Button(root, text="Decrypt", command=lambda: get_value_decrypt(), width=10, height=2,
                 font='Helvetica')
button1.place(x=160, y=300)

button_clear = Button(root, text="Clear", command=lambda: get_clear(), width=10, height=2, font='Helvetica')
button_clear.place(x=280, y=300)
 
# a=encrypt("मेरो देश नेपाल हो!, I'm kunja!")
# print("Encrypted Letters is: ",a)
# b=decrypt(a)
# print("Decrypted Letters is:",b)

root.mainloop()