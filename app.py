from tkinter import *
from tkinter.font import *
import requests
from tkinter.messagebox import *

# Global Variables

query_description = ""
descriptions = ""


# Functions
def Message():
   value = showinfo("Success", "Click Ok To Show Data")
   if value == "ok":
       desc.delete('1.0', END)
       query.set(query_description.upper())
       desc.insert(END,f"""{descriptions}""")

def PleaseWait():
    showinfo("Wait!", "Please Wait! for Almost 3-5 Seconds")


def GETRESPONSE():
    PleaseWait()
    text = search_entry.get()
    api = requests.get(f"https://descriptionapi.herokuapp.com/api?query={text}").json()
    description = api['Description']
    query = api['Query']
    global query_description
    query_description = query
    global descriptions
    descriptions = description
    Message()

root = Tk()


# Selecting Font
fontStyle = Font(family="Lucida Grande", size=30)
# Font For Entry
fontEntry = Font(family="Lucida Grande")
# Query Font
queryFont = Font(family="Lucida Grande", size = 20)
# Description Font
descriptionFont = Font(family="Lucida Grande", size = 10)

# Creating Variables
query = StringVar()

# Making Size of Window
root.geometry(("800x615"))

# Setting Title
root.title("Searchify")

# Adding Background
root.configure(bg="#1c2833")

# Setting Min And Max Size
root.maxsize(800, 615)
root.minsize(800, 615)

# Logo Frame Header
header = Frame(root,bg="#1c2833",width="800",height="50")
header.place(x=0,y=0)

# Header LOGO
header_label = Label(header, text="Searchify", fg="white", bd="0", bg="#1c2833", font=fontStyle)
header_label.grid(row=0, column=0, padx=305,pady=10)

# Bar Frame Header
bar = Frame(root,bg="#1c2833",width="800",height="50")
bar.place(x=100,y=55)

# Search Bar
search_entry = Entry(bar, bg="white", bd="0", font=fontEntry)
search_entry.grid(row=0,column=0,pady = 10, ipadx = 150, ipady = 12)

# Search Event Button
search_button = Button(bar, text="",bg="#1e8449", fg="#ffffff", bd="0", cursor="heart", command=GETRESPONSE)
search_button.grid(row=0,column=1, ipadx = 20, ipady = 9)
search_button['text'] = "Go!"

#Query Frame
query_frame = Frame(root, bg = "#1c2833", width="800",height="40")
query_frame.place(x=0,y=110)

#Query Header
query_label = Label(query_frame, textvariable = query, fg="white", bd="0", bg="#1c2833", font=queryFont)
query_label.grid(row=0, column=0, ipadx = 10, ipady = 40)

#Content Frame
content_frame = Frame(root, bg="#1c2833", width="800")
content_frame.place(x=0,y=195)


# Query Description
desc = Text(content_frame, bg="#ffffff", fg="#000", width="98", font=descriptionFont, bd="0")
desc.grid(row=0, column=0, padx=5)



root.mainloop()