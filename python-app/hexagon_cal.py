import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import math
from PIL import Image, ImageTk
import os

class HexagonCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hexagon Calculator by Udayanga")
        self.master.geometry("1060x700")
        self.master.minsize(1060, 700)
        self.master.resizable(True, True)

        self.style = ttk.Style(theme='darkly')
        self.style.configure("TButton", font=("Helvetica", 11))
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # --- Main Frames ---
        self.description_frame = ttk.Frame(self.master, padding=20)
        self.description_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.description_frame.grid_columnconfigure(0, weight=1)

        self.calculator_frame = ttk.Frame(self.master, padding=20)
        self.calculator_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.calculator_frame.grid_columnconfigure(1, weight=1)

        # --- Description Content ---
        ttk.Label(
            self.description_frame,
            text="About the Hexagon",
            font=("Helvetica", 16, "bold"),
            bootstyle="info"
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        ttk.Label(
            self.description_frame,
            text=(
                "A hexagon is a six-sided polygon with equal sides and angles in a "
                "regular hexagon. It has several important measurements that define "
                "its geometry."
            ),
            wraplength=400,
            justify=LEFT,
            font=("Helvetica", 11)
        ).grid(row=1, column=0, sticky="w", pady=(0, 10))

        ttk.Label(
            self.description_frame,
            text="Measurements",
            font=("Helvetica", 14, "bold"),
            bootstyle="info"
        ).grid(row=2, column=0, sticky="w", pady=(10, 5))

        # --- Image Integration ---
        script_dir = os.path.dirname(__file__)
        image_path = os.path.join(script_dir, "hexagon-diagram.png")

        try:
            original_image = Image.open(image_path)
            max_width = 250
            width_percent = (max_width / float(original_image.size[0]))
            hsize = int((float(original_image.size[1]) * float(width_percent)))
            resized_image = original_image.resize((max_width, hsize), Image.Resampling.LANCZOS)
            self.hexagon_image = ImageTk.PhotoImage(resized_image)

            ttk.Label(
                self.description_frame,
                image=self.hexagon_image
            ).grid(row=3, column=0, sticky="w", pady=(0, 10))
        except FileNotFoundError:
            ttk.Label(
                self.description_frame,
                text=f"[Hexagon Diagram Image Not Found at: {image_path}]",
                font=("Helvetica", 11, "italic"),
                bootstyle="danger"
            ).grid(row=3, column=0, sticky="w", pady=(0, 10))
        except Exception as e:
            ttk.Label(
                self.description_frame,
                text=f"[Error loading image: {e}]",
                font=("Helvetica", 11, "italic"),
                bootstyle="danger"
            ).grid(row=3, column=0, sticky="w", pady=(0, 10))
        # --- End Image Integration ---

        measurements_text = [
            "Side (a): The length of one side of the hexagon.",
            "Long Diagonal (d): The distance between two opposite vertices, equal to 2 times the side.",
            "Short Diagonal (s): The distance between two non-adjacent vertices, equal to √3 times the side.",
            "Circumcircle Radius (R): The radius of the circle that passes through all the vertices of the hexagon, equal to the side length.",
            "Apothem (r): The perpendicular distance from the center to one side, equal to (√3/2) * a.",
            "Area: The total surface area of the hexagon, calculated as (3√3/2) * a².",
            "Perimeter: The total length of all six sides, equal to 6 times the side length."
        ]
        for i, text in enumerate(measurements_text):
            ttk.Label(
                self.description_frame,
                text=text,
                wraplength=500,
                justify=LEFT,
                font=("Helvetica", 11)
            ).grid(row=4 + i, column=0, sticky="w", pady=2)


        # --- Calculator Content ---
        ttk.Label(
            self.calculator_frame,
            text="Calculate Hexagon Measurements",
            font=("Helvetica", 16, "bold"),
            bootstyle="info"
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.entries = {}
        input_fields = [
            ("side", "Side (a):"),
            ("longDiagonal", "Long Diagonal (d):"),
            ("shortDiagonal", "Short Diagonal (s):"),
            ("circumcircleRadius", "Circumcircle Radius (R):"),
            ("apothem", "Apothem (r):"),
            ("area", "Area:"),
            ("perimeter", "Perimeter:")
        ]

        current_row = 1
        for i, (id_name, label_text) in enumerate(input_fields):
            ttk.Label(
                self.calculator_frame,
                text=label_text,
                bootstyle="light",
                font=("Helvetica", 11)
            ).grid(row=current_row, column=0, sticky="w", pady=5, padx=(0, 10))

            entry = ttk.Entry(
                self.calculator_frame,
                bootstyle="dark",
                width=30,
                font=("Helvetica", 11)
            )
            entry.grid(row=current_row, column=1, sticky="ew", pady=5)
            entry.bind("<KeyRelease>", self.calculate)
            self.entries[id_name] = entry
            current_row += 1

        # --- Reset Button (Moved Here) ---
        ttk.Button(
            self.calculator_frame,
            text="Reset",
            command=self.reset_calculator,
            bootstyle="primary"
        ).grid(row=current_row, column=0, columnspan=2, sticky="ew", pady=(20, 0))
        current_row += 1

        # --- Formulas Used (Moved After Reset Button) ---
        ttk.Label(
            self.calculator_frame,
            text="Formulas Used",
            font=("Helvetica", 14, "bold"),
            bootstyle="info"
        ).grid(row=current_row, column=0, columnspan=2, sticky="w", pady=(20, 5))
        current_row += 1

        formulas_text = [
            "◦ Long Diagonal (d) = 2 x a",
            "◦ Short Diagonal (s) = √3 x a",
            "◦ Circumcircle Radius (R) = a",
            "◦ Apothem (r) = (√3/2) x a",
            "◦ Area = (3√3/2) x a²",
            "◦ Perimeter = 6 x a"
        ]
        for i, text in enumerate(formulas_text):
            ttk.Label(
                self.calculator_frame,
                text=text,
                wraplength=400,
                justify=LEFT,
                font=("Helvetica", 11)
            ).grid(row=current_row + i, column=0, columnspan=2, sticky="w", pady=2)

    def calculate(self, event=None):
        active_widget_id = self.master.focus_get().winfo_id()
        active_entry_name = None
        for name, entry_widget in self.entries.items():
            if entry_widget.winfo_id() == active_widget_id:
                active_entry_name = name
                break

        if not active_entry_name:
            return

        try:
            input_value = float(self.entries[active_entry_name].get())
            if input_value < 0:
                raise ValueError("Input cannot be negative.")
        except ValueError:
            self.reset_calculator()
            return

        a = None

        if active_entry_name == 'side':
            a = input_value
        elif active_entry_name == 'longDiagonal':
            a = input_value / 2
        elif active_entry_name == 'shortDiagonal':
            a = input_value / math.sqrt(3)
        elif active_entry_name == 'circumcircleRadius':
            a = input_value
        elif active_entry_name == 'apothem':
            a = (2 * input_value) / math.sqrt(3)
        elif active_entry_name == 'area':
            if input_value <= 0:
                self.reset_calculator()
                return
            a = math.sqrt((2 * input_value) / (3 * math.sqrt(3)))
        elif active_entry_name == 'perimeter':
            a = input_value / 6

        if a is None or math.isnan(a) or a <= 0:
            self.reset_calculator()
            return

        d = 2 * a
        s = math.sqrt(3) * a
        R = a
        r = (math.sqrt(3) / 2) * a
        A = (3 * math.sqrt(3) / 2) * (a ** 2)
        P = 6 * a

        results = {
            'side': a,
            'longDiagonal': d,
            'shortDiagonal': s,
            'circumcircleRadius': R,
            'apothem': r,
            'area': A,
            'perimeter': P
        }

        for name, value in results.items():
            if name != active_entry_name:
                self.entries[name].delete(0, END)
                self.entries[name].insert(0, f"{value:.2f}")

    def reset_calculator(self):
        """
        Clears all input fields in the calculator.
        """
        for entry in self.entries.values():
            entry.delete(0, END)

if __name__ == "__main__":
    app_window = ttk.Window()
    HexagonCalculatorApp(app_window)
    app_window.mainloop()
