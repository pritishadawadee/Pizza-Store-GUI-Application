# 🍕 Online Pizza Ordering App

A desktop-based pizza ordering application built with Python and Tkinter as part of university programming coursework.

## 📋 Description

This app allows users to browse a pizza menu loaded from local image files and a CSV price list. Users can select pizzas, choose quantities, add them to a cart, and confirm or cancel their orders — all through a simple graphical interface.

## ✨ Features

- Browse full pizza menu with images
- View pizza name and price on selection
- Add pizzas to cart with custom quantity
- View order summary with grand total
- Confirm or cancel orders
- Clear menu and cart with one click

## 🛠️ Requirements

- Python 3.x
- Pillow library

Install dependencies:
```bash
pip install pillow
```

## 📁 Project Structure
```
project-folder/
│
├── pizza_template.py       # Main application file
├── pizza_prices.csv        # Pizza names and prices
└── allPizza/               # Folder containing pizza images
    ├── Margherita.png
    ├── Pepperoni.png
    └── ...
```

## 📄 CSV Format

The `pizza_prices.csv` file should follow this format (no headers):
```
Margherita,8.99
Pepperoni,10.99
BBQ Chicken,11.49
```

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to the project folder:
```bash
cd your-repo-name
```

3. Install dependencies:
```bash
pip install pillow
```

4. Add your pizza images to the `allPizza/` folder and set up `pizza_prices.csv`

5. Run the app:
```bash
python pizza_template.py
```

## 📸 Screenshots

*Add a screenshot of your running application here*

## 👩‍💻 Author

**Pritisha Dawadi**  
Student ID: w2148849

## 📝 License

This project was created for educational purposes as part of university coursework.
