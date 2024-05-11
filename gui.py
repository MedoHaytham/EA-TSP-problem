import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

#All pages
class Page(tk.Frame):
    def __init__(self, parent, controller, title):
        tk.Frame.__init__(self, parent, bg='#000000')
        self.controller = controller
        
        label = tk.Label(self, text=title, bg='#041618', fg="white", font=("Helvetica", 32), width=20, height=2)
        label.pack(pady=0, padx=10)

        if not isinstance(self, StartPage):
            button_back = tk.Button(self, text="Back", width=10, height=1, bg='white', command=lambda: controller.show_frame(StartPage))
            button_back.pack(pady=5, padx=10)

#home page
class StartPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Choose Algorithm")

        button1 = tk.Button(self, text="Simulated Annealing", width=20, height=2, bg='white', command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="PSO", width=20, height=2, bg='white', command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=10, padx=10)


# Simulated Annealing page 
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Simulated Annealing")
        
            # Text widget to display file contents
        self.text_area = tk.Text(self, wrap="word", height=1, width=30)
        self.text_area.pack(pady=50)

    # Display file contents when the page is initialized
        self.display_file_contents()

    def display_file_contents(self):
        # Open and read the contents of the file
        file_path = "best_route.txt"
        with open(file_path, "r") as file:
            file_contents = file.read()

        # Display the contents in the text area
        self.text_area.insert(tk.END, file_contents)
        
        # Label widget to display the image
        self.image_area = tk.Label(self)
        self.image_area.pack(pady=10)
        
        # Display image when the page is initialized
        self.display_image_contents()

 
    def display_image_contents(self):
        # Open and display the image
        file_path = "./image/best_routeSA.png"
        image = Image.open(file_path)
        self.photo = ImageTk.PhotoImage(image)  
        
        # Display the image in the Label widget
        self.image_area.config(image=self.photo)
        self.image_area.image = self.photo

        
class PageTwo(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "PSO")
   
            # Text widget to display file contents
        self.text_area = tk.Text(self, wrap="word", height=1, width=30)
        self.text_area.pack(pady=10)

    # Display file contents when the page is initialized
        self.display_file_contents()

    def display_file_contents(self):
        # Open and read the contents of the file
        file_path = "best_routePSO.txt"
        with open(file_path, "r") as file:
            file_contents = file.read()

        # Display the contents in the text area
        self.text_area.insert(tk.END, file_contents)
        
        # Label widget to display the image
        self.image_area = tk.Label(self)
        self.image_area.pack(pady=10)
        
        # Display image when the page is initialized
        self.display_image_contents()

 
    def display_image_contents(self):
        # Open and display the image
        file_path = "./image/best_routePSO.png"
        image = Image.open(file_path)
        self.photo = ImageTk.PhotoImage(image)  
        
        # Display the image in the Label widget
        self.image_area.config(image=self.photo)
        self.image_area.image = self.photo

    
class TSPApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")  
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            if F == PageOne:  
                frame = F(container, self) 
            else:
                frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = TSPApp()
    app.mainloop()
