import tkinter as tk
from PIL import Image,ImageTk
import string
import random
import pyperclip

root = tk.Tk()
root.config(bg="#000042")
root.title("PasswordGen")
root.geometry('400x400')
root.resizable(width=False, height=False)

image_icon = Image.open("logo_passgen.png")
image_icon = ImageTk.PhotoImage(image_icon)
root.iconphoto(False, image_icon)

def genrate():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    set_of_characters = small_alphabets + capital_alphabets + numbers + special_characters
    length_of_pass = int(length.get())
    
    exclude = Ex_char.get()
    preffered = char_preff.get()

    # Initialize the password list
    Password = []

    # Fill the password list with preferred characters
    for char in preffered:
        if len(Password) < length_of_pass:
            Password.append(char)
        else:
            break

    # If required length is not fulfilled, fill remaining with characters from set_of_characters
    if len(Password) < length_of_pass:
        remaining_length = length_of_pass - len(Password)
        if var.get() == "weak":
            set=''.join(char for char in small_alphabets if char not in exclude)
            Password += random.sample(set, remaining_length)
        elif var.get() == "medium":
            set=''.join(char for char in small_alphabets+capital_alphabets if char not in exclude)
            Password += random.sample(set, remaining_length)
        elif var.get() == "strong":
            set=''.join(char for char in set_of_characters if char not in exclude)
            Password += random.sample(set, remaining_length)

    # Shuffle the password list to ensure randomness
    random.shuffle(Password)

    gen_pass.config(text=''.join(Password))

def copy():
    credential=gen_pass.cget("text")
    pyperclip.copy(credential)

#specify length of Pass
pass_length=tk.Label(root,text="Length", font='helvetica 11 bold',bg='#000042',fg="#FFFFFF",height=1)
pass_length.place(x=25, y=35)
length = tk.Spinbox(root, from_=5, to_=18 ,justify="center", width=3, font=("poppins", 12, "bold"), bg='#F0E7D8',bd=0)
length.place(x=30, y=65)


#complexity of Pass
pass_complexity=tk.Label(root,text="Password Complexity", font='helvetica 13 bold',bg='#000042',fg="#FFFFFF",height=1)
pass_complexity.place(x=200, y=30)
# Radio button options
options = [("Weak", "weak"), ("Medium", "medium"), ("Strong", "strong")]
var = tk.StringVar()
var.set("weak")

# Create radio buttons
radio_buttons = []
for option_text, value in options:
    radio_button = tk.Radiobutton(root, text=option_text, variable=var, value=value,bg='#000042',fg="#F0E7D8",selectcolor="#528AAE")
    radio_buttons.append(radio_button)

# Place radio buttons
for i, radio_button in enumerate(radio_buttons):
    radio_button.place(x=200, y=50+ i * 25)

#character preference
character_prefference=tk.Label(root,text="Character Prefference", font='helvetica 11 bold',bg='#000042',fg="#FFFFFF",height=1)
character_prefference.place(x=25, y=145)
char_preff=tk.StringVar()
character_preff = tk.Entry(root, justify="center",width=20, font=("helvetica", 15, "bold"), bg='#F0E7D8',bd=0,textvariable=char_preff)
character_preff.place(x=30, y=170)


#exclude specific Character
Exclude_char=tk.Label(root,text="Exclude Characters", font='helvetica 11 bold',bg='#000042',fg="#FFFFFF",height=1)
Exclude_char.place(x=25, y=200)
Ex_char=tk.StringVar()
Exclude_charcters = tk.Entry(root, justify="center",width=20, font=("helvetica", 15, "bold"), bg='#F0E7D8',bd=0,textvariable=Ex_char)
Exclude_charcters.place(x=30, y=225)

gen_pass=tk.Label(root,text="", font='helvetica 10 bold',bg='#FFFFFF',height=2,width=30)
gen_pass.place(x=30, y=320)
clipboard_image=Image.open('clipboard.png')
clipboard_photo=ImageTk.PhotoImage(clipboard_image)
clipboard_button=tk.Button(root, image=clipboard_photo,borderwidth=0,cursor='arrow',command=copy)
clipboard_button.place(x=290,y=320)

button_generate = tk.Button(root, text='Generate', width=12, height=1, font='helvetica 10 bold', bg="#528AAE", fg="white",command=genrate)
button_generate.place(x=30, y=275)



root.mainloop()




