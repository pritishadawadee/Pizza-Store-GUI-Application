'''
Starter template for programming coursework.

You must build your app by writing code for  the functions listed below.

Code for some of the functions has been provided.

The whole app is a composition of functions.

No GLOBAL variables and button functionality managed by use of lambda functions.

Student Name: Pritisha Dawadi

Student ID: w2148849
'''

# Import required libraries
import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Load pizza names and prices from a CSV file
def load_pizza_prices(csv_file):
    pizza_prices = {}
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price = row
                pizza_prices[name] = float(price)  # Store name-price pairs
    except Exception as e:
        print(f"Error reading pizza prices CSV: {e}")
    return pizza_prices

# Load all pizza images from the given folder and store in a dictionary
def save_images(path, image_dict):
    VALID_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    for file in os.listdir(path):
        if file.lower().endswith(VALID_IMAGE_EXTENSIONS):
            name = os.path.splitext(file)[0]
            try:
                img = Image.open(os.path.join(path, file)).resize((60, 40))
                image_dict[name] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Failed to load image {file}: {e}")

# Display pizza images as buttons
def pizza_images_as_buttons(btn1, btn2, images, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    for widget in pizza_item_details_frame.winfo_children():
        widget.destroy()  # Clear previous pizza buttons
    for i, (name, image) in enumerate(images.items()):
        button = tk.Button(pizza_item_details_frame, image=image, text=name, compound='top',
                           command=lambda n=name: load_image_in_frame(n, image, item_details_frame, order_details_frame, pizza_cart, pizza_prices))
        button.grid(row=i // 5, column=i % 4, padx=10, pady=10)

# Display selected pizza image and its details (name, price, quantity input, buttons)
def load_image_in_frame(name, image, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    for widget in item_details_frame.winfo_children():
        widget.destroy()  # Clear previous details

    # Show pizza image
    img_label = tk.Label(item_details_frame, image=image, bg="black")
    img_label.grid(row=0, column=0, padx=10, pady=10, rowspan=3)
    img_label.image = image  # Prevent garbage collection

    # Pizza name
    name_label = tk.Label(item_details_frame, text=name, fg="white", bg="black", font=("Times New Roman", 14, "bold"))
    name_label.grid(row=0, column=1, columnspan=2, sticky="w", pady=(10, 5))

    # Pizza price
    price_label = tk.Label(item_details_frame, text=f"Price: £{pizza_prices.get(name, 0):.2f}", fg="white", bg="black", font=("Times New Roman", 12))
    price_label.grid(row=2, column=0, columnspan=2, sticky="w", pady=5)

    # Quantity label and input
    tk.Label(item_details_frame, text="Quantity:", fg="white", bg="black", font=("Times New Roman", 12)).grid(row=2, column=1, sticky="e", pady=5)
    quantity_spinbox = tk.Spinbox(item_details_frame, from_=1, to=10, width=5)
    quantity_spinbox.grid(row=2, column=2, sticky="w", pady=5)

    # Add selected pizza to cart
    def add_to_cart():
        qty = int(quantity_spinbox.get())
        pizza_cart[name] = {"quantity": qty, "price": pizza_prices[name], "image": image}
        for widget in item_details_frame.winfo_children():
            widget.destroy()  # Clear after adding
        update_order_details_frame(order_details_frame, pizza_cart)

    # Add to cart button
    add_to_cart_button = ttk.Button(item_details_frame, text="Add to Cart", command=add_to_cart)
    add_to_cart_button.grid(row=4, column=1, columnspan=2, pady=10)

    # Cancel button
    cancel_button = ttk.Button(item_details_frame, text="Cancel", command=lambda: clear_frame(item_details_frame))
    cancel_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Show cart details with image, quantity, total and buttons to confirm/cancel
def update_order_details_frame(order_details_frame, pizza_cart):
    for widget in order_details_frame.winfo_children():
        widget.destroy()

    cart_label = tk.Label(order_details_frame, text="Your order details:", font=("Times New Roman", 14, "bold"))
    cart_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    row = 1
    total_price = 0.0

    # Loop through items in cart
    for name, details in pizza_cart.items():
        quantity = details["quantity"]
        price = details["price"]
        line_total = quantity * price
        total_price += line_total

        img_label = tk.Label(order_details_frame, image=details["image"])
        img_label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

        name_label = tk.Label(order_details_frame, text=name, font=("Times New Roman", 12))
        name_label.grid(row=row, column=0, padx=0, pady=2, sticky="w")

        quantity_label = tk.Label(order_details_frame, text=f"Qty: {quantity}", font=("Times New Roman", 12))
        quantity_label.grid(row=row, column=2, padx=5, pady=2, sticky="e")

        line_total_label = tk.Label(order_details_frame, text=f"Total: £{line_total:.2f}", font=("Times New Roman", 12))
        line_total_label.grid(row=row, column=3, padx=5, pady=2, sticky="e")

        row += 1

    # Grand total
    grand_total_label = tk.Label(order_details_frame, text=f"Grand Total: £{total_price:.2f}", font=("Times New Roman", 14, "bold"))
    grand_total_label.grid(row=row, column=0, columnspan=4, padx=10, pady=10, sticky="e")

    # Cancel and Confirm buttons
    ttk.Button(order_details_frame, text="Cancel", style="big.TButton", width=12,
               command=lambda: clear_cart(order_details_frame, pizza_cart)).grid(row=row + 1, column=2, pady=10, sticky="e")
    
    ttk.Button(order_details_frame, text="Confirm", style="big.TButton", width=12,
               command=lambda: confirm_order(order_details_frame, pizza_cart)).grid(row=row + 1, column=3, pady=10, sticky="e")

# Clear all frames (menu, details, cart)
def clear_all_frames(btn1, btn2, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart):
    clear_frame(pizza_item_details_frame)
    clear_frame(item_details_frame)
    clear_cart(order_details_frame, pizza_cart)
    item_details_frame.configure(bg="red")
    order_details_frame.configure(bg="red")

# Utility to clear a frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Utility to clear cart and show message
def clear_cart(order_details_frame, pizza_cart):
    pizza_cart.clear()
    clear_frame(order_details_frame)
    tk.Label(order_details_frame, text="Your cart is empty", bg="green", font=("Times New Roman", 12)).pack(pady=20)

# Show confirmation message and reset cart
def confirm_order(order_details_frame, pizza_cart):
    pizza_cart.clear()
    clear_frame(order_details_frame)
    tk.Label(order_details_frame, text="Order successfully placed!", bg="green", font=("Times New Roman", 12, "bold")).pack(pady=20)

# Placeholder for "Add New" functionality
def add_pizza():
    print("Add pizza button activated")

# Placeholder for "Delete" functionality
def del_pizza():
    print("Delete button activated")

# Confirm quit dialog
def quitApp(myApp):
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        myApp.destroy()

# Define custom button styles
def configure_style():
    style = ttk.Style()
    style.configure("big.TButton", font=("Times New Roman", 12))

# Create GUI layout frames
def create_frames(myApp):
    frames = {}
    frames["menu"] = tk.Frame(myApp, bg="skyblue")
    frames["menu"].pack(side="top", fill="x")

    main_frame = tk.Frame(myApp)
    main_frame.pack(side="top", fill="both", expand=True)

    frames["pizza"] = tk.Frame(main_frame, bg="red", width=100)
    frames["pizza"].pack(side="left", fill="both", expand=True)

    frames["details"] = tk.Frame(main_frame, bg="black", width=100)
    frames["details"].pack(side="left", fill="both", expand=True)

    frames["cart"] = tk.Frame(myApp, bg="green", height=250)
    frames["cart"].pack(side="bottom", fill="x")

    return frames

# Add top menu buttons with functionality
def create_buttons(frame, myApp, allPizzaDict, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    font_settings = ("Times New Roman", 10)

    tk.Label(frame, font=("Times New Roman", 10, "bold"), bg="skyblue").grid(row=0, column=0, columnspan=5, padx=10, pady=5)

    button_frame = tk.Frame(frame, bg="skyblue")
    button_frame.grid(row=0, column=0, pady=5)

    # Show pizzas
    tk.Button(button_frame, text="Show All Pizzas", font=font_settings, bg="skyblue",
              command=lambda: pizza_images_as_buttons(None, None, allPizzaDict, pizza_item_details_frame,
                                                      item_details_frame, order_details_frame,
                                                      pizza_cart, pizza_prices)).grid(row=0, column=0, padx=5)

    # Clear screen
    tk.Button(button_frame, text="Clear All Pizzas", font=font_settings, bg="skyblue",
              command=lambda: clear_all_frames(None, None,
                                               pizza_item_details_frame,
                                               item_details_frame,
                                               order_details_frame,
                                               pizza_cart)).grid(row=0, column=1, padx=5)

    # Add New, Delete, Quit buttons
    tk.Button(button_frame, text="Add New", font=font_settings, bg="skyblue", command=add_pizza).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Delete", font=font_settings, bg="skyblue", command=del_pizza).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Quit", font=font_settings, bg="skyblue", command=lambda: quitApp(myApp)).grid(row=0, column=4, padx=5)

# Entry point for the app
def main():
    myApp = tk.Tk()
    myApp.title("Online Pizza Store by Student-w2148849")
    myApp.geometry("1000x700")
    myApp.resizable(False, False)
    myApp.configure(background="red")

    configure_style()
    frames = create_frames(myApp)

    pathAllPizza = 'allPizza/'  # Folder where images are stored
    pizza_prices_csv = "pizza_prices.csv"  # CSV file with prices

    allPizzaDict, pizza_cart = {}, {}
    pizza_prices = load_pizza_prices(pizza_prices_csv)
    save_images(pathAllPizza, allPizzaDict)
    print(f"Number of pizza images: {len(allPizzaDict)}")

    create_buttons(frames["menu"], myApp, allPizzaDict, frames["pizza"], frames["details"], frames["cart"], pizza_cart, pizza_prices)

    myApp.mainloop()

# Run the application
main()
