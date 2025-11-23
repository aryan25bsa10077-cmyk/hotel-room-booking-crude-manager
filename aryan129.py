import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE = "bookings.json"

# ------------------ DATA HANDLING FUNCTIONS ------------------ #

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ MAIN APPLICATION ------------------ #

class HotelBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Room Booking Manager")
        self.root.geometry("800x500")

        # Main variables
        self.booking_id = tk.StringVar()
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.room = tk.StringVar()
        self.checkin = tk.StringVar()
        self.checkout = tk.StringVar()

        # UI Layout
        self.create_widgets()
        self.load_table()

    # ------------------ UI DESIGN ------------------ #
    def create_widgets(self):

        title = tk.Label(self.root, text="Hotel Room Booking CRUD Manager",
                         font=("Arial", 18, "bold"))
        title.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Labels & Entry
        labels = ["Booking ID", "Customer Name", "Phone", "Room Type", "Check-in Date", "Check-out Date"]
        vars = [self.booking_id, self.name, self.phone, self.room, self.checkin, self.checkout]

        for i in range(6):
            tk.Label(frame, text=labels[i], font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(frame, textvariable=vars[i], width=30).grid(row=i, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Booking", width=15, command=self.add_booking).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="View Booking", width=15, command=self.view_booking).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Update Booking", width=15, command=self.update_booking).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Delete Booking", width=15, command=self.delete_booking).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Clear", width=15, command=self.clear_fields).grid(row=0, column=4, padx=5)

        # Table for displaying data
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("id", "name", "phone", "room", "checkin", "checkout"),
                                 show="headings", height=8)

        headings = ["Booking ID", "Name", "Phone", "Room", "Check-in", "Check-out"]
        for i, col in enumerate(self.tree["columns"]):
            self.tree.heading(col, text=headings[i])
            self.tree.column(col, width=120)

        self.tree.pack()

    # ------------------ CRUD FUNCTIONS ------------------ #

    def add_booking(self):
        data = load_data()

        new_booking = {
            "id": self.booking_id.get(),
            "name": self.name.get(),
            "phone": self.phone.get(),
            "room": self.room.get(),
            "checkin": self.checkin.get(),
            "checkout": self.checkout.get()
        }

        # Validation
        if "" in new_booking.values():
            messagebox.showerror("Error", "All fields are required!")
            return

        # Prevent duplicate ID
        for b in data:
            if b["id"] == new_booking["id"]:
                messagebox.showerror("Error", "Booking ID already exists!")
                return

        data.append(new_booking)
        save_data(data)
        self.load_table()
        messagebox.showinfo("Success", "Booking added successfully!")
        self.clear_fields()

    def view_booking(self):
        booking_id = self.booking_id.get()
        data = load_data()

        for b in data:
            if b["id"] == booking_id:
                self.name.set(b["name"])
                self.phone.set(b["phone"])
                self.room.set(b["room"])
                self.checkin.set(b["checkin"])
                self.checkout.set(b["checkout"])
                messagebox.showinfo("Success", "Booking found!")
                return

        messagebox.showerror("Error", "Booking not found!")

    def update_booking(self):
        booking_id = self.booking_id.get()
        data = load_data()

        for b in data:
            if b["id"] == booking_id:
                b["name"] = self.name.get()
                b["phone"] = self.phone.get()
                b["room"] = self.room.get()
                b["checkin"] = self.checkin.get()
                b["checkout"] = self.checkout.get()

                save_data(data)
                self.load_table()
                messagebox.showinfo("Success", "Booking updated!")
                self.clear_fields()
                return

        messagebox.showerror("Error", "Booking not found!")

    def delete_booking(self):
        booking_id = self.booking_id.get()
        data = load_data()

        new_data = [b for b in data if b["id"] != booking_id]

        if len(new_data) == len(data):
            messagebox.showerror("Error", "Booking not found!")
        else:
            save_data(new_data)
            self.load_table()
            messagebox.showinfo("Success", "Booking deleted!")
            self.clear_fields()

    def clear_fields(self):
        self.booking_id.set("")
        self.name.set("")
        self.phone.set("")
        self.room.set("")
        self.checkin.set("")
        self.checkout.set("")

    # ------------------ LOAD TABLE ------------------ #
    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        data = load_data()
        for b in data:
            self.tree.insert("", tk.END, values=(b["id"], b["name"], b["phone"],
                                                 b["room"], b["checkin"], b["checkout"]))


# ------------------ MAIN LOOP ------------------ #

root = tk.Tk()
app = HotelBookingApp(root)
root.mainloop()