import tkinter as tk
from tkinter import messagebox

def checkSecondDigits(num):
    length = len(num)
    total = 0
    for i in range(length - 2, -1, -2):
        number = int(num[i])
        number *= 2
        if number > 9:
            strNumber = str(number)
            number = int(strNumber[0]) + int(strNumber[1])
        total += number
    return total

def odd_digits(num):
    length = len(num)
    sumOdd = 0
    for i in range(length - 1, -1, -2):
        sumOdd += int(num[i])
    return sumOdd

def c_length(num):
    length = len(num)
    if length >= 13 and length <= 16:
        if num[0] == "4" or num[0] == "5" or num[0] == "6" or (num[0] == "3" and num[1] == "7"):
            return True
    return False

def process_credit_card():
    cc = entry_cc_number.get()
    even = checkSecondDigits(cc)
    odd = odd_digits(cc)
    c_len = c_length(cc)
    tot = even + odd

    if c_len and tot % 10 == 0:
        result_label.config(text="Valid", fg="green")
    else:
        result_label.config(text="Invalid", fg="red")

# Create tkinter window
root = tk.Tk()
root.title("Credit Card Validator")

# Input credit card number
label_cc_number = tk.Label(root, text="Enter credit card number:")
label_cc_number.pack()
entry_cc_number = tk.Entry(root)
entry_cc_number.pack()

# Button to validate credit card
validate_button = tk.Button(root, text="Validate", command=process_credit_card)
validate_button.pack()

# Display validation result
result_label = tk.Label(root, text="", fg="black")
result_label.pack()

root.mainloop()

