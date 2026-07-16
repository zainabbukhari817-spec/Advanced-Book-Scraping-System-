import tkinter as tk
from tkinter import messagebox
import subprocess
import os


def run_scraper():
    subprocess.run(["python", "scraper.py"])
    messagebox.showinfo("Done", "Scraping Completed!")


def run_analysis():
    subprocess.run(["python", "analysis.py"])
    messagebox.showinfo("Done", "Analysis Completed!")


def run_search():
    subprocess.run(["python", "search.py"])


def run_export():
    subprocess.run(["python", "export_data.py"])
    messagebox.showinfo("Done", "Excel & JSON Exported!")


def open_charts():
    folder = os.path.join(os.getcwd(), "charts")

    if os.path.exists(folder):
        os.startfile(folder)
    else:
        messagebox.showerror("Error", "Charts folder not found!")


root = tk.Tk()

root.title("Advanced Book Scraping System")

root.geometry("450x450")

root.resizable(False, False)

title = tk.Label(
    root,
    text="Advanced Book Scraping System",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)

tk.Button(
    root,
    text="📥 Run Scraper",
    width=30,
    height=2,
    command=run_scraper
).pack(pady=5)

tk.Button(
    root,
    text="📊 Run Analysis",
    width=30,
    height=2,
    command=run_analysis
).pack(pady=5)

tk.Button(
    root,
    text="🔍 Search Books",
    width=30,
    height=2,
    command=run_search
).pack(pady=5)

tk.Button(
    root,
    text="📁 Export Excel & JSON",
    width=30,
    height=2,
    command=run_export
).pack(pady=5)

tk.Button(
    root,
    text="📈 Open Charts",
    width=30,
    height=2,
    command=open_charts
).pack(pady=5)

tk.Button(
    root,
    text="❌ Exit",
    width=30,
    height=2,
    command=root.destroy
).pack(pady=20)

root.mainloop()
