import tkinter as tk
from tkinter import messagebox
import json, os

DATA_FILE = "contacts.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def refresh_list():
    listbox.delete(0, tk.END)
    for i, c in enumerate(contacts):
        listbox.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    addr = entry_addr.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and phone are required!")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": addr})
    save_data()
    refresh_list()
    clear_fields()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_addr.delete(0, tk.END)

def view_contact():
    try:
        idx = listbox.curselection()[0]
        c = contacts[idx]
        messagebox.showinfo("Contact Details",
                            f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
    except IndexError:
        messagebox.showwarning("Select", "Please select a contact!")

def delete_contact():
    try:
        idx = listbox.curselection()[0]
        del contacts[idx]
        save_data()
        refresh_list()
    except IndexError:
        messagebox.showwarning("Select", "Please select a contact!")

def update_contact():
    try:
        idx = listbox.curselection()[0]
        contacts[idx] = {
            "name": entry_name.get().strip(),
            "phone": entry_phone.get().strip(),
            "email": entry_email.get().strip(),
            "address": entry_addr.get().strip()
        }
        save_data()
        refresh_list()
        clear_fields()
    except IndexError:
        messagebox.showwarning("Select", "Please select a contact to update!")

def search_contact():
    query = entry_search.get().lower().strip()
    listbox.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c["name"].lower() or query in c["phone"]:
            listbox.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

contacts = load_data()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_addr = tk.Entry(root)
entry_addr.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="View", width=10, command=view_contact).grid(row=0, column=3, padx=5)

tk.Label(root, text="Search by Name/Phone").pack()
entry_search = tk.Entry(root)
entry_search.pack()

tk.Button(root, text="Search", command=search_contact).pack(pady=5)
tk.Button(root, text="Show All", command=refresh_list).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

refresh_list()
root.mainloop()
