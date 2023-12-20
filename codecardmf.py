#Converter Mifare Classic
import tkinter
import pyperclip
class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Converter MF access card")
        self.main_window.geometry('300x150')
        self.label = tkinter.Label(self.main_window, text="Enter s/n card:")
        self.label.pack()
        self.entry_input = tkinter.Entry(self.main_window)
        self.entry_input.pack()
        self.button_output = tkinter.Button(self.main_window, text="Convert", command=self.output)
        self.button_output.pack()
        self.text = tkinter.StringVar()
        self.stext = tkinter.Label(self.main_window, text="Code of card:")
        self.stext.pack()
        self.entry_output = tkinter.Entry(self.main_window, textvariable=self.text)
        self.entry_output.pack()
        tkinter.mainloop()
    def output(self):
        number_card = int(self.entry_input.get())
        to_hex = ('{0:x}'.format(number_card))
        temp = to_hex[2:]
        card_code = int(temp , 16)
        pyperclip.copy(card_code)
        self.text.set(card_code)
new_window = MyGui()
