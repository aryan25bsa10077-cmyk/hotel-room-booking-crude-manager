#This Python code creates a straightforward desktop application called Hotel Room Booking Manager, which uses Tkinter to carry out common CRUD (Create, Read, Update, Delete) operations on booking records.
#Disorganized record-keeping frequently results from a small hotel or guesthouse's lack of an easy-to-use, local system for managing their room reservations.  Current solutions may be excessively costly or complicated.  The objective is to offer a simple Graphical User Interface (GUI) application that enables employees to efficiently and dependably:

 Add new booking records for customers.

 View and retrieve current booking information.

 Upon request, update the booking details.

 Remove reservations (such as cancellations or check-outs).

 Even when the application is closed, the system must guarantee data persistence using a local file format.
 
#With the following limitations, the scope is strictly restricted to creating a stand-alone desktop application:

 Technology: Python with the GUI's integrated Tkinter library.

 Bookings.json is the only local JSON file used for data storage.  There is no database integration (SQL, NoSQL, etc.) included.

 Functionality: Adding, viewing, updating, and deleting booking records using the fundamental CRUD functions.

 Exclusions

 No support for multiple users or networks.

 Dates are manually entered as text; there is no calendar date-picker widget.

 No intricate business logic (such as verifying room availability, processing payments, or generating reports).
 
#Those in charge of keeping track of reservations and client information in a small-scale hospitality setting are the main target users:

 Hotel/Guesthouse Reception Staff: Employees who must promptly input new reservations and retrieve client data during check-in and check-out.

 Small Business Owners: Owners of B&Bs or micro-hotels who require an easy-to-use, free reservation management tool instead of a sophisticated cloud-based system.
