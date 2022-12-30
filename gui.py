import customtkinter
import tkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("small example app")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")


        row3 = 1
        self.label_3 = customtkinter.CTkLabel(
                            text="a",
                            justify='left',
                            anchor='w',
                            master=app,
                            )
        self.label_3.grid(row=row3, column=0,padx=10, pady=5, sticky="w")

        self.button3 = customtkinter.CTkButton(
                        master=app,
                        text="as",
                       
                        )
        self.button3.grid(row=row3, column=1,padx=10,pady=5,stick="nsew")

        self.label_3_1 = customtkinter.CTkLabel(
                            text="a: 0",
                            master=app,
                            )
        self.label_3_1.grid(row=row3, column=2,padx=10, pady=5, sticky="w")


if __name__ == "__main__":
    app = App()
    app.mainloop()