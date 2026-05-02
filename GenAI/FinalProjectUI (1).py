import tkinter as tk
from tkinter import ttk, messagebox
import math
# from ImageGenerator import generateImage
from PIL import Image,ImageTk

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")



        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack(pady=10)



        # Dropdown for shapes
        self.shape_var = tk.StringVar()
        self.dropdown = ttk.Combobox(root, textvariable=self.shape_var, state="readonly")
        self.dropdown['values'] = ("Circle", "Rectangle", "Square", "Hexagon")
        self.dropdown.current(0)
        self.dropdown.pack(pady=5)
        
        # Theme entry
        theme_label = tk.Label(root, text="Map Theme:")
        theme_label.pack()
        self.theme_entry = tk.Entry(root)
        self.theme_entry.pack(pady=5)
        self.theme_entry.insert(0, "")  # leave empty to default to "Forest"

        # Text input field
        theme_label = tk.Label(root, text="Additional Features!")
        theme_label.pack()
        self.text_entry = tk.Entry(root)
        self.text_entry.pack(pady=5)

        # Create text button
        text_button = tk.Button(root, text="Create Text", command=self.create_text)
        text_button.pack(pady=5)

        # Output button
        output_button = tk.Button(root, text="Generate", command=self.output_summary)
        output_button.pack(pady=5)

        # Store draggable objects
        self.draggable_objects = []

        # Store current shape
        self.current_shape = None

        # Theme placeholder
        self.theme = "Forest"

        # Drag data
        self.drag_data = {"x": 0, "y": 0, "item": None}

        # Bind events
        self.canvas.bind("<ButtonPress-1>", self.on_drag_start)
        self.canvas.bind("<B1-Motion>", self.on_drag_motion)
        self.canvas.bind("<Button-3>", self.on_right_click)

        img = ImageTk.PhotoImage(Image.open("download.png").resize((500, 500)))
        self.canvas.create_image(250, 250, image=img)


    def create_text(self):
        label = self.text_entry.get()
        x, y = 200, 200
        text_id = self.canvas.create_text(x, y, text=label, font=("Arial", 14), tags="draggable", fill="black")
        self.draggable_objects.append({
            "id": text_id,
            "text": label,
            "x": x,
            "y": y
        })

    def on_drag_start(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if "draggable" in self.canvas.gettags(item):
            self.drag_data["item"] = item[0]
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
        else:
            self.drag_data["item"] = None

    def on_drag_motion(self, event):
        if self.drag_data["item"] is not None:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            self.canvas.move(self.drag_data["item"], dx, dy)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

            for obj in self.draggable_objects:
                if obj["id"] == self.drag_data["item"]:
                    obj["x"] += dx
                    obj["y"] += dy
                    break

    def on_right_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if "draggable" in self.canvas.gettags(item):
            item_id = item[0]
            self.canvas.delete(item_id)
            self.draggable_objects = [
                obj for obj in self.draggable_objects if obj["id"] != item_id
            ]

    def output_summary(self):
        self.theme = self.theme_entry.get().strip() or "Forest"
        self.current_shape = self.shape_var.get()
        
        center_x, center_y = 300, 200
        
        output = f"Theme: {self.theme}\n"
        output += f"Shape: {self.current_shape if self.current_shape else 'None'}\n"
        output += "Objects:\n"

        for obj in self.draggable_objects:
            x, y = obj["x"], obj["y"]

            if abs(x - center_x) <= 100 and abs(y - center_y) <= 100:
                location = "center"
            elif x < center_x and y < center_y:
                location = "upper left"
            elif x >= center_x and y < center_y:
                location = "upper right"
            elif x < center_x and y >= center_y:
                location = "lower left"
            else:
                location = "lower right"

            output += f"  '{obj['text']}' in {location}\n"


        messagebox.showinfo("Canvas Summary", output)        
        print(output)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root)

    #generateImage(1, 2, 3)
    # img = ImageTk.PhotoImage(Image.open("download.png").resize((500, 500)))

    # app.canvas.create_image(250, 250, image=img)
    root.mainloop()
