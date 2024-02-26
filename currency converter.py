import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = from_var.get()
        to_currency = to_var.get()
        
        # Conversion rates (replace with actual rates)
        rates = {
        'USD': {'USD': 1, 'EUR': 0.89, 'GBP': 0.79, 'JPY': 150.76, 'CNY': 7.20, 'INR': 82.87},
    'EUR': {'USD': 1.081843, 'EUR': 1, 'GBP': 0.87, 'JPY': 163.57 , 'CNY': 7.81, 'INR': 89.93},
    'GBP': {'USD': 1.27, 'EUR': 1.17, 'GBP': 1, 'JPY': 191.15, 'CNY': 9.12, 'INR': 105.06},
    'JPY': {'USD': 0.0066, 'EUR': 0.0061, 'GBP': 0.0052, 'JPY': 1, 'CNY': 0.048, 'INR': 0.55},
    'CNY': {'USD': 0.14, 'EUR': 0.13, 'GBP': 0.11, 'JPY': 20.95, 'CNY': 1, 'INR': 11.73},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, 'JPY': 1.82, 'CNY': 0.085, 'INR': 1},
    'PKR': {'USD': 0.0036, 'EUR': 0.0033, 'GBP': 0.0028, 'JPY': 0.54, 'CNY': 0.026, 'INR': 0.30 , 'PKR':1}
}
        
        result = amount * rates[from_currency][to_currency]
        label_result.config(text="{:.2f} {}".format(result, to_currency))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except KeyError:
        messagebox.showerror("Error", "Please select currencies.")

def shutdown():
    root.destroy()

root = tk.Tk()
root.title("Currency Converter")

# Labels
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="From:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="To:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5)

# Entry widgets
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

# Dropdown menus
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'INR','PKR']  # Add more currencies here if needed
from_var = tk.StringVar(root)
from_var.set(currencies[0])
to_var = tk.StringVar(root)
to_var.set(currencies[1])

from_menu = tk.OptionMenu(root, from_var, *currencies)
from_menu.grid(row=1, column=1, padx=5, pady=5)
to_menu = tk.OptionMenu(root, to_var, *currencies)
to_menu.grid(row=2, column=1, padx=5, pady=5)

# Result label
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=1, padx=5, pady=5)

# Buttons
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")
btn_shutdown = tk.Button(root, text="Shutdown", command=shutdown)
btn_shutdown.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()
