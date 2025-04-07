import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkinter.simpledialog import Dialog

class PinDialog(Dialog):
    def __init__(self, parent, title, prompt):
        self.prompt = prompt
        self.result = None
        super().__init__(parent, title)
    
    def body(self, master):
        ttk.Label(master, text=self.prompt).pack(pady=10)
        self.entry = ttk.Entry(master, show="*")
        self.entry.pack(pady=5)
        return self.entry
    
    def validate(self):
        try:
            self.result = int(self.entry.get())
            return True
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return False
    
    def apply(self):
        self.result = int(self.entry.get())

class VirtualATM:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual ATM")
        self.root.geometry("400x500")
        self.root.resizable(False, False)  # Make window non-resizable
        self.root.configure(bg="#f0f0f0")
        
        self.balance = 0
        self.pin = None
        self.setup_initial_pin()
        
        self.create_widgets()
        
    def validate_pin(self, pin):
        if pin is None:
            return False
        try:
            pin = int(pin)
            return 1000 <= pin <= 9999  # Ensure 4-digit PIN
        except ValueError:
            return False
        
    def setup_initial_pin(self):
        while True:
            dialog = PinDialog(self.root, "Set PIN", "Set your 4-digit PIN:")
            pin = dialog.result
            if pin is None:
                self.root.destroy()
                return
            if self.validate_pin(pin):
                self.pin = pin
                messagebox.showinfo("Success", "PIN Set Successfully! Please remember it.")
                break
            else:
                messagebox.showerror("Error", "PIN must be a 4-digit number!")
    
    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Virtual ATM", 
                              font=("Arial", 20, "bold"))
        title_label.pack(pady=20)
        
        # Balance Display (initially hidden)
        self.balance_label = ttk.Label(main_frame, 
                                     text="Balance: ******",
                                     font=("Arial", 12))
        self.balance_label.pack(pady=10)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=20)
        
        # Buttons
        ttk.Button(buttons_frame, text="Check Balance", 
                  command=self.check_balance).pack(fill=tk.X, pady=5)
        ttk.Button(buttons_frame, text="Withdraw Money", 
                  command=self.withdraw_money).pack(fill=tk.X, pady=5)
        ttk.Button(buttons_frame, text="Deposit Money", 
                  command=self.deposit_money).pack(fill=tk.X, pady=5)
        ttk.Button(buttons_frame, text="Change PIN", 
                  command=self.change_pin).pack(fill=tk.X, pady=5)
        ttk.Button(buttons_frame, text="Exit", 
                  command=self.exit_atm).pack(fill=tk.X, pady=5)
    
    def verify_pin(self):
        while True:
            dialog = PinDialog(self.root, "Verify PIN", "Enter your PIN:")
            entered_pin = dialog.result
            if entered_pin is None:
                return False
            if self.validate_pin(entered_pin):
                return entered_pin == self.pin
            messagebox.showerror("Error", "PIN must be a 4-digit number!")
    
    def check_balance(self):
        if self.verify_pin():
            self.balance_label.config(text=f"Current Balance: Rs.{self.balance}")
        else:
            messagebox.showerror("Error", "Incorrect PIN! Access Denied")
            self.balance_label.config(text="Balance: ******")
    
    def withdraw_money(self):
        if not self.verify_pin():
            messagebox.showerror("Error", "Incorrect PIN! Access Denied")
            return
            
        while True:
            try:
                amount = simpledialog.askinteger("Withdraw", "Enter Amount to Withdraw:")
                if amount is None:
                    return
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    continue
                break
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")
                continue
            
        if amount > self.balance:
            messagebox.showerror("Error", "Insufficient Balance! Withdraw Failed")
        else:
            self.balance -= amount
            self.balance_label.config(text=f"Current Balance: Rs.{self.balance}")
            messagebox.showinfo("Success", 
                              f"Withdraw Successful! Remaining Balance: Rs.{self.balance}")
    
    def deposit_money(self):
        if not self.verify_pin():
            messagebox.showerror("Error", "Incorrect PIN! Access Denied")
            return
            
        while True:
            try:
                amount = simpledialog.askinteger("Deposit", "Enter Amount to Deposit:")
                if amount is None:
                    return
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    continue
                break
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")
                continue
            
        self.balance += amount
        self.balance_label.config(text=f"Current Balance: Rs.{self.balance}")
        messagebox.showinfo("Success", 
                          f"Deposit Successful! New Balance: Rs.{self.balance}")
    
    def change_pin(self):
        if not self.verify_pin():
            messagebox.showerror("Error", "Incorrect PIN! Access Denied")
            return
            
        while True:
            dialog = PinDialog(self.root, "Change PIN", "Enter New PIN:")
            new_pin = dialog.result
            if new_pin is None:
                return
            if self.validate_pin(new_pin):
                self.pin = new_pin
                messagebox.showinfo("Success", "PIN Changed Successfully")
                break
            else:
                messagebox.showerror("Error", "PIN must be a 4-digit number!")
    
    def exit_atm(self):
        if messagebox.askokcancel("Exit", "Thank You for using Virtual ATM\nGood Bye"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualATM(root)
    root.mainloop() 