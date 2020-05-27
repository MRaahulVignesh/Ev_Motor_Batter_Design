
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import calculation

class Main:
    def __init__(self, master):
       

        self.master = master

        mainframe = tk.Frame(self.master, width=650, height=550, bg="white")
        mainframe.pack(fill=tk.BOTH)

        title = tk.Label(mainframe, text="Electrical Vehicle Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        title.place(x=200, y=50)

        logo_img = tk.PhotoImage(file="images/logo.png")
        logo = tk.Label(mainframe, image = logo_img, bg="#f8f8f8", fg="#f8f8f8" )
        logo.image = logo_img
        logo.place(x=60, y=20)

        motor_img = tk.PhotoImage(file="images/Motor.png")
        battery_img = tk.PhotoImage(file="images/battery.png")
        
        button_motor = tk.Button(mainframe, image=motor_img, bg="white", fg="white", bd="0", command = self.motor_design)
        button_motor.image = motor_img
        button_motor.place(x=20, y=200)
        
        button_battery = tk.Button(mainframe, image=battery_img, bg="white", bd="0", command= self.battery_design)
        button_battery.image = battery_img
        button_battery.place(x=340, y=200)

    def motor_design(self):
        mtr_window = tk.Toplevel(self.master)
        mtr_window.title("Motor Design Tool") 
        mtr_window.resizable("false", "false")
        mtr_window.geometry("650x550+300+250")  

        frame_1 = tk.Frame(mtr_window, width=650, height=550, bg="white")
        frame_1.pack(fill=tk.BOTH)

        title_label = tk.Label(frame_1, text="Electrical Vehicle Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        title_label.place(x=200, y=50)

        logo_img_1 = tk.PhotoImage(file="images/logo.png")
        logo_label = tk.Label(frame_1, image = logo_img_1, bg="#f8f8f8", fg="#f8f8f8" )
        logo_label.image = logo_img_1
        logo_label.place(x=60, y=20)


        label_1 = tk.Label(frame_1, text="Vehicle Weight :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_1.place(x=70, y=170)
        self.entry_1 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_1.place(x=200, y=170)

        label_2 = tk.Label(frame_1, text="Vehicle Area :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_2.place(x=70, y=220)
        self.entry_2 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_2.place(x=200, y=220)

        label_3 = tk.Label(frame_1, text="Slip :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_3.place(x=70, y=270)
        self.entry_3 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_3.place(x=200, y=270)

        label_4 = tk.Label(frame_1, text="Cd :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_4.place(x=70, y=320)
        self.entry_4 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_4.place(x=200, y=320)

        label_5 = tk.Label(frame_1, text="Crr :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_5.place(x=70, y=370)
        self.entry_5 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_5.place(x=200, y=370)

        label_6 = tk.Label(frame_1, text="Grade_percent :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_6.place(x=370, y=170)
        self.entry_6 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_6.place(x=500, y=170)

        label_7 = tk.Label(frame_1, text="Vehicle Speed :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_7.place(x=370, y=220)
        self.entry_7 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_7.place(x=500, y=220)

        label_8 = tk.Label(frame_1, text="Wind Speed :", font="Times 12", bg="#f8f8f8", fg="#101010")
        label_8.place(x=370, y=270)
        self.entry_8 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_8.place(x=500, y=270)

        label_9 = tk.Label(frame_1, text="Wheel Radius :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_9.place(x=370, y=320)
        self.entry_9 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_9.place(x=500, y=320)

        label_10 = tk.Label(frame_1, text="Gear Ratio :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_10.place(x=370, y=370)
        self.entry_10 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_10.place(x=500, y=370)

        button_1_img = tk.PhotoImage(file="images/button_1.png")
        button_cal = tk.Button(frame_1, image=button_1_img, bg="white", bd = "0", command=self.generate_motor)
        button_cal.image = button_1_img
        button_cal.place(x=270, y=450)

    def generate_motor(self):

    

        ## call the function here
        try:
            v_weight = float(self.entry_1.get())
            v_area = float(self.entry_2.get())
            slip = float(self.entry_3.get())
            Cd = float(self.entry_4.get())
            Crr = float(self.entry_5.get())
            grade_percent = float(self.entry_6.get())
            v_speed = float(self.entry_7.get())
            v_wind = float(self.entry_8.get())
            wheel_radius = float(self.entry_9.get())
            gear_ratio = float(self.entry_10.get())
            cal = calculation.Calculation(v_weight, v_area, slip, Cd, Crr, wheel_radius, gear_ratio, v_speed, grade_percent)

            torque = int(cal.motor(v_wind))
            power = int(cal.power(v_wind))

            message = "Motor Torque = " + str(torque) + " N/m" + "\n" + "\n" + "Power Rating = " + str(power) + " Watts"

        except Exception as e:
            message = "Error: Check the variables"
            print(e)

        pop_up = tk.Tk()
        pop_up.title("Motor Specification")
        w = 400     
        h = 200     
        sw = pop_up.winfo_screenwidth()
        sh = pop_up.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        pop_up.geometry('%dx%d+%d+%d' % (w, h, x, y))

        m = tk.Label(pop_up, text=message, font="Times 12", width=120, height=5)
        m.pack()
        b = tk.Button(pop_up, text="OK", command=pop_up.destroy, width=10)
        b.pack()
        tk.mainloop()


    def battery_design(self):
        bty_window = tk.Toplevel(self.master)
        bty_window.title("Battery Design Tool") 
        bty_window.geometry("650x550+300+250")  
        
        frame_1 = tk.Frame(bty_window, width=650, height=550, bg="#f8f8f8")
        frame_1.pack(fill=tk.BOTH)

        title_label = tk.Label(frame_1, text="Electrical Vehicle Battery Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        title_label.place(x=100, y=50)

        
def main():
  
    root = tk.Tk()
    root.geometry("650x550+300+250")
    root.resizable(False, False)
    root.title("EV Design Tool")
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()
