import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator || Developed By Sambhav Banihal")
        self.root.geometry("800x500")
        self.root.configure(bg="#2C3E50") 

        # Employee Details Section
        self.details_frame = tk.Frame(root)
        self.details_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.label_root=tk.Label(bg="#FFE5B4")
        # Create labels and entries for employee details
        self.label_emp_id = tk.Label(self.details_frame, text="Employee ID")
        self.label_emp_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_emp_id = tk.Entry(self.details_frame, width=30)
        self.entry_emp_id.grid(row=0, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.details_frame, text="Name")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.details_frame, width=30)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_department = tk.Label(self.details_frame, text="Department")
        self.label_department.grid(row=2, column=0, padx=5, pady=5)
        self.entry_department = tk.Entry(self.details_frame, width=30)
        self.entry_department.grid(row=2, column=1, padx=5, pady=5)

        self.label_designation = tk.Label(self.details_frame, text="Designation")
        self.label_designation.grid(row=3, column=0, padx=5, pady=5)
        self.entry_designation = tk.Entry(self.details_frame, width=30)
        self.entry_designation.grid(row=3, column=1, padx=5, pady=5)

        # Buttons to generate and clear the QR code
        self.generate_button = tk.Button(self.details_frame, text="QR Generate", command=self.generate_qr_code)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.clear_button = tk.Button(self.details_frame, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=0, columnspan=2, pady=10)

        # QR Code Display Section
        self.qr_frame = tk.Frame(root)
        self.qr_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        self.qr_label = tk.Label(self.qr_frame, text="Employee QR Code")
        self.qr_label.pack()

        self.qr_image_label = tk.Label(self.qr_frame, text="No QR Available", bg="white", width=200, height=200)
        self.qr_image_label.pack(pady=10)

        # Save Button
        self.save_button = tk.Button(self.qr_frame, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack(pady=10)

        self.qr_image = None
        self.qr_image_obj = None  # For saving the actual image

    def generate_qr_code(self):
        emp_id = self.entry_emp_id.get()
        name = self.entry_name.get()
        department = self.entry_department.get()
        designation = self.entry_designation.get()

        if not emp_id or not name or not department or not designation:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        # Combine employee details to encode in the QR code
        qr_data = f"Employee ID: {emp_id}\nName: {name}\nDepartment: {department}\nDesignation: {designation}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image from the QR code
        self.qr_image_obj = qr.make_image(fill='black', back_color='white')

        # Resize the image for display
        display_image = self.qr_image_obj.resize((150, 150))  # Resize the image for better visibility
        self.qr_image = ImageTk.PhotoImage(display_image)

        # Update the label to show the QR code
        self.qr_image_label.config(image=self.qr_image, text="", bg="white")

    def save_qr_code(self):
        if self.qr_image_obj is None:
            messagebox.showwarning("Save Error", "No QR code generated to save.")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", ".png"), ("All files", ".*")]
        )
        if file_path:
            # Save the QR code image to file
            self.qr_image_obj.save(file_path)
            messagebox.showinfo("Save Successful", f"QR code saved to {file_path}")

    def clear_fields(self):
        # Clear all input fields and reset QR code display
        self.entry_emp_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_department.delete(0, tk.END)
        self.entry_designation.delete(0, tk.END)
        self.qr_image_label.config(image='', text="No QR Available", bg="white")
        self.qr_image = None
        self.qr_image_obj = None

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
