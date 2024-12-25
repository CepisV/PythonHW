import tkinter as tk
import tkinter.messagebox as mb
import re

def required(value, message):
    if not value:
        raise ValueError(message)
    return value

def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)
    return value

class Contact:
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    phone_regex = re.compile(r"\([0-9]{3}\)\s[0-9]{7}")

    def __init__(self, lastname, firstname, email, phone):
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.phone = phone

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = required(value, "Фамилия обязательна")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = matches(value, self.email_regex, "Некорректный email формат")

class ContactList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="#f7f9fc", **kwargs)
        self.lb = tk.Listbox(self, selectmode=tk.MULTIPLE, font=("Arial", 12), bg="white", fg="#333", selectbackground="#cce5ff", borderwidth=0)
        scroll = tk.Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def insert(self, contact, index=tk.END):
        text = f'{contact.lastname}, {contact.firstname}'
        self.lb.insert(index, text)

    def delete(self, indices):
        for index in reversed(indices):  
            self.lb.delete(index)

    def update(self, contact, index):
        self.delete([index])
        self.insert(contact, index)

    def get_selected_indices(self):
        return self.lb.curselection()

class ContactForm(tk.LabelFrame):
    fields = ('Фамилия', 'Имя', 'Почта', 'Телефон')

    def __init__(self, master, contact_list, **kwargs):
        super().__init__(master, text='Контактная форма', font=("Arial", 14, "bold"), bg="#e3f2fd", fg="#007bff", padx=15, pady=15, **kwargs)
        self.frame = tk.Frame(self, bg="#e3f2fd")
        self.entries = list(map(self.create_field, enumerate(self.fields)))

        self.button_frame = tk.Frame(self.frame, bg="#e3f2fd")
        self.add_button = tk.Button(self.button_frame, text='Добавить', font=("Arial", 12), bg="#007bff", fg="white", activebackground="#0056b3", activeforeground="white", command=self.add_contact)
        self.delete_button = tk.Button(self.button_frame, text='Удалить', font=("Arial", 12), bg="#dc3545", fg="white", activebackground="#c82333", activeforeground="white", command=self.delete_contact)

        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.contact_list = contact_list
        self.button_frame.grid(row=4, columnspan=2, pady=10)
        self.frame.pack()

    def add_contact(self):
        try:
            contact = self.get_detail()
            if contact:
                self.contact_list.insert(contact)
                self.clear()
        except ValueError as e:
            mb.showerror('Ошибка валидации', str(e), parent=self)

    def delete_contact(self):
        selected_indices = self.contact_list.get_selected_indices()
        if not selected_indices:
            mb.showwarning("Удаление контакта", "Выберите контакт(ы) для удаления", parent=self)
        else:
            self.contact_list.delete(selected_indices)

    def create_field(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text, font=("Arial", 12), bg="#e3f2fd", fg="#333")
        entry = tk.Entry(self.frame, width=30, font=("Arial", 12), bg="white", fg="#333", borderwidth=2, relief="groove")
        label.grid(row=position, column=0, pady=5, sticky="e")
        entry.grid(row=position, column=1, pady=5, sticky="w")
        return entry

    def load_details(self, contact):
        values = (contact.lastname, contact.firstname, contact.email, contact.phone)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def get_detail(self):
        values = [e.get() for e in self.entries]
        try:
            return Contact(*values)
        except ValueError as e:
            mb.showerror('Ошибка валидации', str(e), parent=self)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Контакты")
    root.configure(bg="#f7f9fc")
    root.geometry("500x600")

    contact_list = ContactList(root)
    contact_list.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

    contact_form = ContactForm(root, contact_list)
    contact_form.pack(padx=15, pady=15, fill=tk.BOTH)

    root.mainloop()
