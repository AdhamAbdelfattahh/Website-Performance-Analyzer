import requests
import time
from tkinter import Tk, Label, Entry, Button, messagebox

class PerformanceAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Website Performance Analyzer")

        # Input field for URL
        self.url_label = Label(master, text="Enter Website URL:")
        self.url_label.pack()
        self.url_entry = Entry(master)
        self.url_entry.pack()

        # Analyze button
        self.analyze_button = Button(master, text="Analyze", command=self.analyze_performance)
        self.analyze_button.pack()

    def analyze_performance(self):
        url = self.url_entry.get()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        start_time = time.time()
        try:
            response = requests.get(url)
            load_time = time.time() - start_time
            status_code = response.status_code

            report = f"URL: {url}\nLoad Time: {load_time:.2f} seconds\nStatus Code: {status_code}"
            messagebox.showinfo("Performance Report", report)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to analyze website: {e}")

# Create the main application window
if __name__ == "__main__":
    root = Tk()
    app = PerformanceAnalyzerApp(root)
    root.mainloop()
