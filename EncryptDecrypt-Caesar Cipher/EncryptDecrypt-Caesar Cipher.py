from tkinter import *
from tkinter import messagebox

# Set up the Tkinter screen
screen = Tk()
screen.geometry("420x420")
screen.title("Caesar Cipher Encryption and Decryption")
screen.configure(bg="grey")

# Caesar cipher constants
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1


# Caesar cipher shift function
def caesar_shift(message, shift):
    result = ""
    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            # Adjust for wraparound within A-Z
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char  # Non-alphabetical characters are not changed

    return result


# Function to check for errors in both password and shift value
def validate_input(password, shift_value):
    # Check if the password is correct
    if password == "":
        messagebox.showerror("Error", "Please enter the secret key")
        return False

    if password != "12345":
        messagebox.showerror("Error", "Invalid secret key")
        return False


    # Validate the shift value
    try:
        shift_key = int(shift_value)
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")
        return False

    return True


# Encrypt function using Caesar cipher
def encrypt():
    password = code.get()
    shift_value = shift_slider.get()  # Get shift value from Entry widget

    if not validate_input(password, shift_value):
        return  # Stop further execution if validation fails

    shift_key = shift_value  # Convert shift value to integer after validation

    # Create a new window for encryption result
    screen1 = Toplevel(screen)
    screen1.title("Encryption")
    screen1.geometry("400x250")
    screen1.configure(bg="pink")

    message = text1.get(1.0, END)  # Get text from Text widget

    # Encrypt the message with Caesar cipher
    caesar_encrypted_message = caesar_shift(message, shift_key)

    Label(screen1, text="Code is Encrypted", font="Impact 10 bold").place(x=5, y=6)
    text2 = Text(screen1, font="30", bd=4, wrap=WORD)
    text2.place(x=2, y=30, width=390, height=180)
    text2.insert(END, caesar_encrypted_message)


# Decrypt function using Caesar cipher
def decrypt():
    password = code.get()
    shift_value = shift_slider.get()  # Get shift value from Entry widget

    if not validate_input(password, shift_value):
        return  # Stop further execution if validation fails

    shift_key = shift_value  # Convert shift value to integer after validation

    # Create a new window for decryption result
    screen2 = Toplevel(screen)
    screen2.title("Decryption")
    screen2.geometry("400x250")
    screen2.configure(bg="green")

    message = text1.get(1.0, END)  # Get text from Text widget

    # Decrypt the message with Caesar cipher
    caesar_decrypted_message = caesar_shift(message, -shift_key)

    Label(screen2, text="Code is Decrypted", font="Impact 10 bold").place(x=5, y=6)
    text2 = Text(screen2, font="30", bd=4, wrap=WORD)
    text2.place(x=2, y=30, width=390, height=180)
    text2.insert(END, caesar_decrypted_message)


# Reset the screen
def reset():
    text1.delete(1.0, END)
    code.set("")
    shift_slider.set(0)  # Clear the shift value entry


# Create widgets
Label(screen, text="Enter the text for Encryption and Decryption", font="Impact 14",bg="light blue").place(x=5, y=6)

# Text box for input
text1 = Text(screen, font="20")
text1.place(x=5, y=45, width=410, height=120)

# Label for secret key
Label(screen, text="Enter Secret Key", font="Impact 14",bg="grey").place(x=140, y=175)

# Label for shift value
Label(screen, text="Shift Value", font="Impact 14 ",bg="grey").place(x=150, y=239)
# slider for shift value (instead of entry widget)
shift_slider = Scale(screen,from_=-25,to=25,orient=HORIZONTAL,font="16",length=280)
shift_slider.place(x=70, y=265)

# Entry for secret key
code = StringVar()
Entry(textvariable=code, bd=2, font="16", show="*").place(x=90, y=200)

# Buttons for encryption, decryption, and reset
Button(screen, text="ENCRYPT", font="Arial 15 bold", bg="red", fg="white", command=encrypt).place(x=15, y=325,
                                                                                                  width=150)
Button(screen, text="DECRYPT", font="Arial 15 bold", bg="green", fg="white", command=decrypt).place(x=220, y=325,
                                                                                                    width=150)
Button(screen, text="RESET", font="Arial 15 bold", bg="blue", fg="white", command=reset).place(x=60, y=370, width=280)

# Run the mainloop to show the window
mainloop()
