import json
from client import UDPClient
import tkinter as tk
from tkinter import Frame, Scrollbar, Listbox, Entry, Button



class MessengerApp:
    def __init__(self, root):
        self.client = UDPClient(self.receive_message)
        self.client.start()


        self.root = root
        self.root.title("Messagerie")

        self.message_listbox = Listbox(self.root, width=40, height=10, relief=tk.SOLID)
        self.message_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        scrollbar = Scrollbar(self.root, command=self.message_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.message_listbox.config(yscrollcommand=scrollbar.set)

        # Zone de saisie des messages
        self.message_entry = Entry(self.root, width=30)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Boutons pour envoyer et recevoir des messages
        send_button = Button(self.root, text="Envoyer", command=self.send_message)
        send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.mainloop()

    
    def send_message(self):
        message = self.message_entry.get()
        message = json.dumps(f"{self.client.pseudo}: {message}")
        self.client.send(message)
        self.message_listbox.insert(tk.END, message)
        self.message_entry.delete(0, tk.END)
    
    def receive_message(self, message):
        self.message_listbox.insert(tk.END, message)
        self.message_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MessengerApp(root)
        