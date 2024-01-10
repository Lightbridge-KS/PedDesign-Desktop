import sys
from pathlib import Path

# sys.path.insert(1, str(Path(".").absolute() / "src"))

import tkinter  
import customtkinter  
import peddesign  
from module import *  
# from helper import Capturing  

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green


# Lookup Dict
study_type_dict = {
    "CT Chest": "chest",
    "CTWA": "whole_abd",
    "CT Chest + WA": "chest_whole_abd",
    "CTA Liver": "cta_liver",
}

is_first_study_dict = {"Not First Study": False, "First Study": True}

class MyInputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        # Logo Label
        self.logo_label = customtkinter.CTkLabel(
            self,
            text="Design Pediatric CT",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=10, pady=(20, 10))

        # Study Type
        self.optionmenu_study_type = MyOptionMenu(
            self, values=list(study_type_dict.keys()), label_text="Study type:"
        )
        self.optionmenu_study_type.grid(
            row=1, column=0, padx=10, pady=(0, 0), sticky="ew"
        )
        # self.optionmenu_study_type.configure(fg_color="transparent")
        # Age Group
        self.optionmenu_is_first_study = MyOptionMenu(
            self, values=list(is_first_study_dict.keys()), label_text="Occasion:"
        )
        self.optionmenu_is_first_study.grid(
            row=2, column=0, padx=10, pady=(0, 0), sticky="ew"
        )
        # self.optionmenu_is_first_study.configure(fg_color="transparent")
        # Weight (kg)
        self.entry_weight_kg = MyEntry(
            self, placeholder_text="kg", label_text="Weight (kg):"
        )
        self.entry_weight_kg.grid(row=3, column=0, padx=10, pady=(0, 0), sticky="ew")
        # self.entry_weight_kg.configure(fg_color="transparent")

    def get(self):
        out = {
            "study_type": study_type_dict[self.optionmenu_study_type.get()],
            "weight_kg": float(self.entry_weight_kg.get()),
            "is_first_study": is_first_study_dict[self.optionmenu_is_first_study.get()],
        }
        return out


class MyOutputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # self.grid_rowconfigure(4, weight=1)
        # Output TextBox
        self.output_textbox = customtkinter.CTkTextbox(self, width=400, height=300)
        self.output_textbox.grid(
            row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Design Pediatric CT")
        # self.geometry("700x390")
        self.minsize(700, 390)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=2)
        # Input Frame
        self.input_frame = MyInputFrame(self)
        self.input_frame.grid(row=0, column=0, sticky="nsew")

        # Output Frame
        self.output_frame = MyOutputFrame(self)
        self.output_frame.grid(row=0, column=1, sticky="nsew")

        # Button
        self.button = customtkinter.CTkButton(
            self, text="Generate", command=self.button_clicked
        )
        self.button.grid(
            row=1, column=0, columnspan=2, padx=20, pady=(20, 20), sticky="ew"
        )

    # Call back Fn when click button
    def button_clicked(self):
        self.print_inputs()
        print(self.get_text_output())
        self.render_text_output()

    # Print input to console
    def print_inputs(self):
        input_dict = self.input_frame.get()
        print(input_dict)

    # Get Text Output
    def get_text_output(self):
        input_dict = self.input_frame.get()
        # Design CT as String
        text_output = peddesign.design_ct_str(**input_dict)
        return text_output

    # Render Text Output
    def render_text_output(self):
        textbox = self.output_frame.output_textbox
        output_str = self.get_text_output()
        # with Capturing() as output:
        #     self.get_text_output()
            # print('hello')
            # print('world')
        # output_str = "\n".join(output)
        textbox.delete("0.0", "end")  # delete all text
        textbox.insert("0.0", output_str)


if __name__ == "__main__":
    app = App()
    app.mainloop()
