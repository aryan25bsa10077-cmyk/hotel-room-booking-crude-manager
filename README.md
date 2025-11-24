This project uses Python's Tkinter library for the graphical user interface (GUI) to create a basic CRUD (Create, Read, Update, Delete) application. It is intended to handle hotel reservations, making it simple for a user to add new reservations, view current ones, modify booking information, and remove records.

The application is stateful and permits data retention between sessions because all booking data is stored in a local JSON file called bookings.json.

The following essential features are offered by the application:

Create (Add Booking): Add a new booking record that includes the customer's name, phone number, room type, check-in and check-out dates, and a unique ID. includes validation to make sure the Booking ID is unique and all fields are filled out.

Read (Load Table/View Booking):

View Booking: Enter the Booking ID of a specific booking to search for and see its details in the input fields.

Load Table: Use Treeview to automatically display all current booking records in an understandable tabular format.

Update (Update Booking): Change an existing booking's details (Name, Phone, Room Type, Dates) using its Booking ID.

Delete (Delete Booking): Using its Booking ID, remove a booking record from the database.

Clear Fields: For a fresh start, reset all input fields to be empty.

Python 3 is the primary language.

Tkinter (a standard Python library) is the GUI library.

JSON is used for data storage (bookings.json).

Typical Modules:

The styled Treeview table widget uses tkinter.ttk.

json: Data can be read from and written to the JSON file.

os: Used to determine whether the data file is present.

Requirements: Make sure Python 3 is installed on your computer. A standard Python installation comes with Tkinter and the standard library modules.

Save or download the code: The supplied Python code should be saved in a file called aryan129.py (or any other.py file name).

Launch the program: Run the following command after opening your terminal or command prompt and going to the directory where you saved the file:

hotel room booking crude manager.py in Python

Initial State: The window for the application will open. When you add your first booking, a bookings.json file will be created automatically if one does not already exist. The program will load the current data into the table if the file already exists.
