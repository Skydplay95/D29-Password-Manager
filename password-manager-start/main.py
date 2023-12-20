from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def random_password():

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  random_letter = [password_list.append(random.choice(letters)) for char in range(nr_letters)]

  random_symbol = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

  random_number = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
  #get the value of all entry
  website_save = website_entry.get().lower()
  mail_save = mail_entry.get()
  password_save = password_entry.get()

  new_data = {website_save: { 
              "email": mail_save, 
               "password": password_save
            }
  }

  if len(website_save) == 0 or len(password_save) == 0:
      messagebox.showinfo(title="Empty entry", message="Please don't leave fields empty")
  else:
     #save the value into a file 
      try:
        with open("./password-manager-start/save_password.json", mode= "r") as data_file:
          #read old data from json file
          data = json.load(data_file) 
      except FileNotFoundError:
        with open("./password-manager-start/save_password.json", mode= "w") as data_file:    
          #read old data from json file
          json.dump(new_data, data_file, indent=4)
      else:
          #update data on json file
          data.update(new_data)
          with open("./password-manager-start/save_password.json", mode= "w") as data_file: 
            #saving update data 
            json.dump(data, data_file, indent=4)
      finally:
          #clear the entry of website and password
          website_entry.delete(0, "end")
          password_entry.delete(0, "end")

def find_password():
  website_search = website_entry.get().lower()
  
  try:
    with open("./password-manager-start/save_password.json", mode= "r") as data_file: 
        data = json.load(data_file) 

  except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
  else:
      if website_search in data:
        email = data[website_search]["email"]
        password = data[website_search]["password"]

        messagebox.showinfo(title={website_search}, message=f"Email: {email}\n Password: {password}")
      else:
         messagebox.showinfo(title="Error", message="No details for this website")
      
     
         












# ---------------------------- UI SETUP ------------------------------- #
#create and setup all part of the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white", highlightthickness=0)

#create the canva
logo_canva= Canvas(width=200, height=200, bg="white", highlightthickness=0 )

#add image into var to use print it with canva 
logo_img = PhotoImage(file="./password-manager-start/logo.png")

#put the image in the midde of the canva 
logo_canva.create_image(100, 100, image=logo_img)

logo_canva.grid(column=1, row=0)


#create label
website_label = Label(text="Website: ", bg="white", fg="black")
mail_label = Label(text="Email/Username: ", bg="white", fg="black")
password_label = Label(text="Password: ", fg="black", bg="white")


#Place all label with grid
website_label.grid(column=0, row=1)

mail_label.grid(column=0, row=2)

password_label.grid(column=0, row=3)


#create all entry
website_entry = Entry(width=18, bg="white", highlightthickness=0, fg="black")
website_entry.focus()

mail_entry = Entry(width=35, bg="white", highlightthickness=0, fg="black")
mail_entry.insert(END, "mail@gmail.com")

password_entry = Entry(bg="white", highlightthickness=0, width=18, fg="black")


#Place all entry with grid 
website_entry.grid(row=1, column=1, padx=0, pady=3)

mail_entry.grid(row=2, column=1, columnspan=2, padx=0, 
pady=3)

password_entry.grid(row=3, column=1, padx=0, pady=3)


#create a generate password button
random_password_button = Button(text="Generate Password",bg="white", highlightbackground="white", width=13, command=random_password)

#create a seach button
search_button = Button(text="Search", bg="white", highlightbackground="white", width=13, command=find_password)

#create a add to local txt manager 
add_to_file = Button(text="Add", width=36, bg="white", highlightbackground="white", command=save_password)

#place all buttons with grid 
random_password_button.grid(row=3, column=2, padx=0, pady=3)

search_button.grid(row=1, column=2, padx=0, pady=3)

add_to_file.grid(row=4, column=1, columnspan=2)


#keep the window open
window.mainloop()