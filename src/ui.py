from tkinter import Tk, Label, Button, Entry, messagebox

root = Tk()
root.title('Email Response System')

# Styling
root.configure(bg='#F0F0F0')

# Welcome Label
label = Label(root, text='Welcome to the Email Response System!', font=('Arial', 24), bg='#F0F0F0')
label.pack(pady=20)

# Email Entry
email_entry = Entry(root, font=('Arial', 16))
email_entry.pack(pady=10)

# Generate Response Button
button = Button(root, text='Generate Response', font=('Arial', 16), bg='#4CAF50', fg='white', command=generate_response)
button.pack(pady=10)

# Function to generate response
def generate_response():
    email = email_entry.get()
    if email:
        response = response_generator.generate_response(email)
        messagebox.showinfo('Response', response)
    else:
        messagebox.showwarning('Warning', 'Please enter an email address.')

root.mainloop()