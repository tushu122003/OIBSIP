import tkinter as tk
from PIL import Image, ImageTk
import csv
import matplotlib.pyplot as plt

class MyApp(tk.Frame):
    def __init__(self, root):
        super().__init__(
            root,
            bg='WHITE'
        )
        self.root = root
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # Load the GIF
        gif_image = Image.open('snowfall.gif')
        self.gif_bg = ImageTk.PhotoImage(gif_image)

        # Create a canvas for the GIF
        self.canvas = tk.Canvas(
            self.main_frame,
            bg='WHITE',
            highlightthickness=0
        )
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.gif_bg)

        # Create widgets for BMI calculator
        label_bmi_calc = tk.Label(root, text="BMI calculator", font=('Arial', 18), bg="plum")
        label_bmi_calc.place(x=180, y=0)

        label_height = tk.Label(root, text="Height", font=('Arial', 10), bg="lightblue")
        label_height.place(x=35, y=80)

        label_weight = tk.Label(root, text="Weight", font=('Arial', 10), bg="lightblue")
        label_weight.place(x=270, y=80)

        self.Height = tk.StringVar()
        self.Weight = tk.StringVar()
        entry_height = tk.Entry(root, textvariable=self.Height, width=5, font='arial 50', bg='#fff', fg="#000", bd=0,
                                justify=tk.CENTER)
        entry_height.place(x=35, y=100)

        entry_weight = tk.Entry(root, textvariable=self.Weight, width=5, font='arial 50', bg='#fff', fg="#000", bd=0,
                                justify=tk.CENTER)
        entry_weight.place(x=270, y=100)

        def BMI():
            h = float(self.Height.get())
            w = float(self.Weight.get())
            # to convert height in meter
            m = h / 100
            bmi = w / m ** 2
            bmi = round(bmi, 2)
            return bmi

        def weight_cate(bmi):
            if bmi < 18.5:
                return "Your BMI is: {}\nYou are underweight".format(bmi)
            elif 18.5 <= bmi < 24.9:
                return "Your BMI is: {}\nYou have Healthy weight".format(bmi)
            elif 24.9 <= bmi < 30:
                return "Your BMI is: {}\nYou are overweight".format(bmi)
            elif bmi >= 30:
                return "Your BMI is: {}\nYou are obese".format(bmi)

        def calculate_and_display():
            # Check if height and weight are provided
            if not self.Height.get() or not self.Weight.get():
                emptylabel.config(text="Please enter valid height and weight.")
                return
            
            try:
                h = float(self.Height.get())
                w = float(self.Weight.get())
                
                # Check if height and weight are positive numbers
                if h <= 0 or w <= 0:
                    emptylabel.config(text="Height and weight must be non-zero positive numbers.")
                    return
                
                # Calculate BMI
                m = h / 100
                bmi = w / m ** 2
                bmi = round(bmi, 2)
                
                # Display BMI result
                result_message = weight_cate(bmi)
                emptylabel.config(text=result_message)
                
                # Write BMI value to a CSV file
                with open('bmi_records.csv', 'a', newline='') as csvfile:
                    fieldnames = ['Height', 'Weight', 'BMI']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header if file is empty
                    if csvfile.tell() == 0:
                        writer.writeheader()

                    # Write BMI record
                    writer.writerow({'Height': self.Height.get(), 'Weight': self.Weight.get(), 'BMI': bmi})
            except ValueError:
                emptylabel.config(text="Please enter valid numerical values for height and weight.")

        def display_bmi_graph():
    # Read BMI records from CSV file
            heights = []
            weights = []
            bmis = []
            with open('bmi_records.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    heights.append(float(row['Height']))
                    weights.append(float(row['Weight']))
                    bmis.append(float(row['BMI']))
    
    # Define colors for different BMI ranges
            colors = []
            for bmi in bmis[-5:]:
                if bmi < 18.5:
                    colors.append('blue')
                elif 18.5 <= bmi < 24.9:
                    colors.append('green')
                elif 24.9 <= bmi < 30:
                    colors.append('orange')
                else:
                    colors.append('red')
    
     # Plot BMI graph with lines connecting marker points
            plt.figure(figsize=(4.5, 2))
            for i in range(len(bmis[-5:])):
                plt.plot([i, i], [0, bmis[-5:][i]], marker='o', color=colors[i])  # Plot marker point
                if i > 0:
                    plt.plot([i-1, i], [bmis[-5:][i-1], bmis[-5:][i]], color=colors[i])  # Connect points with lines
        
            plt.xlabel('Records')
            plt.ylabel('BMI')
            plt.title('BMI Graph (Last 5 Records)')
            plt.xticks(range(5), ['Record {}'.format(i+1) for i in range(5)])  # Set x-axis labels
            plt.grid(True)  
            plt.tight_layout()
            plt.savefig('bmi_graph.png')
            plt.close()
    
    # Display graph image in tkinter
            graph_image = Image.open('bmi_graph.png')
            graph_image = ImageTk.PhotoImage(graph_image)
            graph_label = tk.Label(root, image=graph_image)
            graph_label.image = graph_image
            graph_label.place(x=25, y=375)


        button_calc = tk.Button(root, command=calculate_and_display, text="Calculate", width=12, height=1,
                                font='arial 10 bold', bg="#1f6e68", fg="white")
        button_calc.place(x=35, y=200)

        button_records = tk.Button(root, command=display_bmi_graph, text="Records", width=8, height=1, font='arial 10 bold', bg="#1f6e68", fg="white")
        button_records.place(x=400, y=230)
   

        emptylabel = tk.Label(root, fg='purple', font=('Arial', 12))
        emptylabel.place(x=20, y=320)

        # Load and place the help icon
        help_icon = Image.open("oasisinfobyte/helpicon.png")
        self.help_icon = ImageTk.PhotoImage(help_icon)
        label_help = tk.Label(root, image=self.help_icon, bg='WHITE')
        label_help.image = self.help_icon
        label_help.place(x=470, y=10)
        label_help.bind("<Button-1>", self.open_help_window)  # Bind left mouse click event to open_help_window method

        # Set application icon
        image_icon = Image.open("oasisinfobyte/logo_bmi.png")
        image_icon = ImageTk.PhotoImage(image_icon)
        root.iconphoto(False, image_icon)

        # Get GIF frames and play GIF
        self.gif1_frames = self._get_frames('snowfall.gif')
        self._play_gif(self.canvas, self.gif1_frames)
        
    def open_help_window(self, event):
        if hasattr(self, 'help_window') and self.help_window.winfo_exists():
            self.help_window.lift()
        else:
            self.help_window = tk.Toplevel(self.root)
            self.help_window.title("Help")
            self.help_window.geometry("300x200")

            # Load help image
            help_image = Image.open("oasisinfobyte/BMI.png")
            help_image = ImageTk.PhotoImage(help_image)

             # Display help image
            self.help_label = tk.Label(self.help_window, image=help_image)
            self.help_label.image = help_image
            self.help_label.pack()
            self.help_Feedback = tk.Label(self.help_window, text="Send Feedback on <dearstranger3@gmail.com>", font=('Arial', 8), bg="lightblue")
            self.help_Feedback.pack()
        self.help_window.resizable(width=False, height=False)

    def _get_frames(self, img):
        with Image.open(img) as gif:
            index = 0
            frames = []
            while True:
                try:
                    gif.seek(index)
                    frame = ImageTk.PhotoImage(gif)
                    frames.append(frame)
                except EOFError:
                    break
                index += 1
        return frames

    def _play_gif(self, label, frames, index=0):
        if index >= len(frames):
            index = 0
        frame = frames[index]
        label.itemconfig(1, image=frame)  # Change itemconfig to update the image on canvas
        self.root.after(100, self._play_gif, label, frames, index + 1)


root = tk.Tk()
root.title('BMI Calculator')
root.geometry('500x600')
root.resizable(width=False, height=False)

my_app_instance = MyApp(root)
root.mainloop()
