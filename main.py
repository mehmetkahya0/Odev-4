import tkinter as tk
from bubble import BubbleSort
from tkinter import Frame
from flappybird import *
import webbrowser
import tkinter.messagebox as messagebox


def start_bubble_sort():
    root.destroy()   
    BubbleSort()

def start_flappy_bird():
    root.destroy()
    gameUI()

def open_webpage():
    webbrowser.open('https://github.com/mehmetkahya0', new=2)  # Open the web page in a new tab
# Create a new function to show an "About" window
def show_about():
    messagebox.showinfo("Hakkında", "Bu uygulama, Mehmet Kahya - 230603035 tarafından 23 Mayıs 2024 tarihinde oluşturulmuştur ve Proje seçmek için kullanılmaktadır.")

# Create a new function to exit the application
def exit_app():
    root.destroy()
    
root = tk.Tk()
root.title("Home GUI")
root.geometry("500x300")
root.configure(bg='#0531a8')
root.resizable(False, False)   

# Create a new menu bar
menu_bar = tk.Menu(root)

# Create a "File" menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Çıkış", command=exit_app)
menu_bar.add_cascade(label="Dosya", menu=file_menu)

# Create a "Help" menu and add it to the menu bar
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Hakkında", command=show_about)
menu_bar.add_cascade(label="Yardım", menu=help_menu)

# Set the root window's menu bar
root.config(menu=menu_bar)

space = tk.Label(root, text="",bg='#0531a8', fg='whitesmoke')
space.pack()

header = tk.Label(root, text="Mehmet Kahya | Odev-4", font=('Helvetica', 20,"bold"),bg='#0531a8', fg='whitesmoke')
header.pack()

label = tk.Label(root, text="Proje seciniz:", font=('Helvetica', 12,"bold"),bg='#0531a8', fg='whitesmoke')
label.pack()

# Create a frame for the Bubble Sort button with a black background
bubble_sort_frame = tk.Frame(root, bg='black', bd=2)
bubble_sort_frame.place(x=150, y=100)

# Create the Bubble Sort button
bubble_sort_button = tk.Button(bubble_sort_frame, text="Bubble Sort Algorithm", bg='#0531a8', command=start_bubble_sort, width=20, height=2, font=('Helvetica', 12,"bold"), fg='whitesmoke')
bubble_sort_button.pack(fill='both', expand=True)  # Fill the frame

# Repeat the same for the Flappy Bird button
flappy_bird_frame = tk.Frame(root, bg='black', bd=2)
flappy_bird_frame.place(x=150, y=170)  # Increase the y coordinate

flappy_bird_button = tk.Button(flappy_bird_frame, text="Flappy Bird", bg='#0531a8', command=start_flappy_bird, width=20, height=2, font=('Helvetica', 12,"bold"), fg='whitesmoke')
flappy_bird_button.pack(fill='both', expand=True)  # Fill the frame

web_button_frame = tk.Frame(root, bg='black', bd=2)
web_button_frame.place(x=192, y=240)

web_button = tk.Button(web_button_frame, text="Github profilim!", command=open_webpage, bg='#0531a8', font=('Helvetica', 10, "bold"), fg='whitesmoke', width=15, height=1)
web_button.pack(fill='both', expand=True)

number = tk.Label(root, text="230603035", font=('Helvetica', 10),bg='#0531a8', fg='whitesmoke')
number.pack(side='bottom')

root.mainloop()