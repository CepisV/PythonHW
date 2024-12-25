import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import requests
import json
import os


class JsonPlaceholderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSONPlaceholder API Client")
        self.root.geometry("500x450")  
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.input_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        self.input_frame.pack(fill="x")

        self.id_label = ttk.Label(self.input_frame, text="Введите ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.id_entry = ttk.Entry(self.input_frame, width=20)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.get_button = ttk.Button(self.input_frame, text="Получить данные", command=self.fetch_data)
        self.get_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.output_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        self.output_frame.pack(fill="both", expand=True)

        self.result_text = tk.Text(self.output_frame, height=15, width=50, wrap="word", bg="#f5f5f5", fg="#333")
        self.result_text.pack(fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.output_frame, orient="vertical", command=self.result_text.yview)
        self.result_text["yscrollcommand"] = self.scrollbar.set
        self.scrollbar.pack(side="right", fill="y")

        self.save_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        self.save_frame.pack(fill="x")

        self.save_button = ttk.Button(self.save_frame, text="Сохранить данные", command=self.save_data)
        self.save_button.pack(pady=5)  

        self.data = None

    def fetch_data(self):
        post_id = self.id_entry.get().strip()
        if not post_id.isdigit():
            messagebox.showerror("Ошибка", "ID должен быть числом.")
            return

        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = response.json()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, json.dumps(self.data, indent=4, ensure_ascii=False))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")

    def save_data(self):
        if not self.data:
            messagebox.showwarning("Внимание", "Нет данных для сохранения.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON файлы", "*.json"), ("Все файлы", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(self.data, f, indent=4, ensure_ascii=False)
                messagebox.showinfo("Успех", f"Данные сохранены в файл: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = JsonPlaceholderApp(root)
    root.mainloop()
