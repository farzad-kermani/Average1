import tkinter as tk
from tkinter import messagebox

# لیست برای ذخیره مقادیر
list1 = []

def submit():
    try:
        # دریافت مقدار از Entry
        value = float(entry.get())
        list1.append(value)  # اضافه کردن مقدار به لیست
        entry.delete(0, tk.END)  # پاک کردن Entry
    except ValueError:
        messagebox.showerror("خطا", "لطفاً یک عدد معتبر وارد کنید.")

def calculate_average():
    if list1:  # بررسی اینکه لیست خالی نیست
        average = sum(list1) / len(list1)
        messagebox.showinfo("میانگین", f"میانگین مقادیر: {average}")
    else:
        messagebox.showwarning("هشدار", "لیست خالی است!")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه میانگین")
root.geometry('350x200')

# ایجاد Entry
entry = tk.Entry(root,font=('Arial',15),bg='#e17fef')
entry.pack(pady=30)

# دکمه Submit
submit_button = tk.Button(root, text="ثبت", command=submit,font=('Arial',18),width=3,height=1)
submit_button.pack(pady=5)

# دکمه Average
average_button = tk.Button(root, text="میانگین", command=calculate_average,font=('Arial',18),width=10,height=1)
average_button.pack(pady=5)


# اجرای حلقه اصلی
root.mainloop()
