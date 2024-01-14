import customtkinter



class MyOptionMenu(customtkinter.CTkFrame):
    def __init__(self, master, values=["option 1", "option 2"], label_text="Options:", **kwargs):
        super().__init__(master)

        ## Label
        self.optionmenu_label = customtkinter.CTkLabel(self, text=label_text, font= customtkinter.CTkFont(size=15, weight="normal") , anchor="w")
        self.optionmenu_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        ## Drop down
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=values, **kwargs)
        self.optionmenu.grid(row=0, column=1, padx=5, pady=10, sticky="w")
        
    def set(self, value):
        self.optionmenu.set(value)

    def get(self):
        return self.optionmenu.get()
    
    def configure(self, require_redraw=False, **kwargs):
        self.optionmenu.configure(require_redraw = require_redraw, **kwargs)


class MyEntry(customtkinter.CTkFrame):
    def __init__(self, master, placeholder_text="CTkEntry", label_text="Entry:", **kwargs):
        super().__init__(master)

        ## Label
        self.entry_label = customtkinter.CTkLabel(self, text=label_text, font= customtkinter.CTkFont(size=15, weight="normal") , anchor="w")
        self.entry_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        ## Entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text=placeholder_text, **kwargs)
        self.entry.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    def get(self):
        return self.entry.get()
    
    def configure(self, require_redraw=False, **kwargs):
        self.entry.configure(require_redraw = require_redraw, **kwargs)
