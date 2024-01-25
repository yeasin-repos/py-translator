from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Translator')
        self.root.geometry('500x600')
        self.root.config(bg='#18122B')

        self.create_widgets()

    def create_widgets(self):
        lbl_txt = Label(self.root, text="Let's translate", font=("Time New Roman", 30, 'bold'), bg='#443C68', fg='#FDE2F3')
        lbl_txt.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        lbl_src = Label(self.root, text="Source Text", font=("Time New Roman", 20, 'bold'), bg='#443C68', fg='#FDE2F3')
        lbl_src.grid(row=1, column=0, columnspan=3, pady=(10, 5))

        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_rowconfigure(1, weight=3)

        self.sor_txt = Text(self.root, font=('Time New Roman', 16), bg='#443C68', fg='#FDE2F3', height=5, width=40)
        self.sor_txt.grid(row=2, column=0, columnspan=3, padx=10, pady=(0, 10))

        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_rowconfigure(2, weight=3)

        lst_txt = list(LANGUAGES.values())

        self.combo_sor = ttk.Combobox(self.root, value=lst_txt, state="readonly")
        self.combo_sor.set("English")
        self.combo_sor.configure(style="Combo.TCombobox")
        self.combo_sor.grid(row=3, column=0, padx=10, pady=(0, 10))

        self.button_change = Button(self.root, text="Translate", relief=RAISED, command=self.data)
        self.button_change.grid(row=3, column=1, padx=10, pady=(0, 10))

        self.combo_dest = ttk.Combobox(self.root, value=lst_txt, state="readonly")
        self.combo_dest.configure(style="Combo.TCombobox")
        self.combo_dest.grid(row=3, column=2, padx=10, pady=(0, 10))

        lbl_dest = Label(self.root, text="Destination Text", font=("Time New Roman", 20, 'bold'), bg='#443C68', fg='#FDE2F3')
        lbl_dest.grid(row=4, column=0, columnspan=3, pady=(10, 5))

        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_rowconfigure(4, weight=3)

        self.dest_txt = Text(self.root, font=("Time New Roman", 20), bg='#443C68', fg='#FDE2F3', height=5, width=40)
        self.dest_txt.grid(row=5, column=0, columnspan=3, padx=10, pady=(0, 10))

        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_rowconfigure(5, weight=3)

        s = ttk.Style()
        s.configure("Combo.TCombobox", fieldbackground='#ffece3', foreground='#443C68')

    def change(self, text='type', src='English', dest="Bengali"):
        trans = Translator()
        try:
            trans1 = trans.translate(text, src=src, dest=dest)
            return trans1.text
        except Exception as e:
            print(f"Translation error: {e}")
            return "Translation failed"

    def data(self):
        s = self.combo_sor.get()
        d = self.combo_dest.get()
        msg = self.sor_txt.get(1.0, END)
        textget = self.change(text=msg, src=s, dest=d)
        self.dest_txt.delete(1.0, END)
        self.dest_txt.insert(END, textget)

if __name__ == "__main__":
    root = Tk()
    app = TranslatorApp(root)
    root.mainloop()