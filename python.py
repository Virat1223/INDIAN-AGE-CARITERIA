import random
import sys
import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
import io

def show_angry_dog_popup():
    # Use the image you gave
    url = "https://images.hindustantimes.com/img/2023/01/25/550x309/Enraged-aggressive--angry-dog--Grin-jaws-with-fang_1674676145665.jpg"
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    # Load image into Tkinter
    image = Image.open(io.BytesIO(raw_data))
    root = tk.Tk()
    root.title("Access Denied! 🛑")
    root.geometry("550x309")
    
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

    msg = tk.Label(root, text="❌ You are not human! Get out! 🐶", font=("Arial", 16), fg="red", bg="black")
    msg.place(relx=0.5, rely=0.05, anchor="n")

    root.mainloop()

# ---- Captcha Logic ---- #
print("\033[91mINDIA AGE CRITERIA TEST.\033[0m")

print("\n\033[92mWELCOME THIS IS INDIA AGE CRITERIA TEST. THIS TOOL IS SPECIALLY MADE FOR FOR FOREIGNERS COMING IN INDIA FOR FIRST TIME.IT TELL THEM WHAT THEY CAN DO OR CAN NOT DO IN OUR COUNTRY INDIA. AS BEING A INDIAN I WELCOM YOU TO MY COUNTRY INDIA.\033[0m")
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
op = random.choice(['+', '-'])
correct = num1 + num2 if op == '+' else num1 - num2


print("\033[91mcomplete this captcha befor processding to our program.\033[0m")
print(f"Captcha: What is {num1} {op} {num2}?")
try:
    ans = int(input("Your answer: "))
except:
    print("Invalid input! You are robot or AI.")
    show_angry_dog_popup()
    sys.exit()

if ans != correct:
    print("❌ You are robot or AI. Access Denied!")
    show_angry_dog_popup()
    sys.exit()

# ---- If Passed ---- #
print("✅ You are human.\n")
name = input("Your name: ")
age = int(input("Your age: "))

if age >= 18:
    print(f"{name} is eligible to vote in India.")
    print(f"{name} is eligible to drive in India.")
    print(f"{name} is eligible to do transactions in India.")
else:
    print(f"{name} is not eligible to vote yet in India.")
    print(f"{name} is not eligible to drive yet in India.")
    print(f"{name} is not eligible to do transactions yet in india.")


print("\033[91mTHIS COUNTRY AGE CRITERIA TEST IS MADE FOR INDIA ONLY. THIS MAY VARY IN OTHER COUNTRIES.\033[0m")
print("\n\033[92mTHANKS FOR USING.\033[0m")
