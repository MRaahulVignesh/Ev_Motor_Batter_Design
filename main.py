import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import motor_calculation
import battery_calculation

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
            cal = motor_calculation.Calculation(v_weight, v_area, slip, Cd, Crr, wheel_radius, gear_ratio, v_speed, grade_percent)

            torque = int(cal.motor(v_wind))
            power = int(cal.power(v_wind))

            message = "Motor Torque = " + str(torque) + " N/m" + "\n" + "\n" + "Power Rating = " + str(power) + " Watts"

        except Exception as e:
            message = "Error: Check the values"
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


        frame_temp = tk.Frame(pop_up, bg="white", width=400, height=200)
        frame_temp.pack()

        m = tk.Label(pop_up, text=message, font="Times 12", bg="white")
        m.place(x=100, y= 50)

        b = tk.Button(pop_up, text="Okay", font = "Times 12 bold", bg="white", fg="#95b889", bd = "0", highlightthickness=4, 
        highlightcolor="#000000", highlightbackground="#000000", width=10, command=pop_up.destroy)
        b.place(x=130, y= 100)
        tk.mainloop()


    def battery_design(self):

        self.bat_cal = battery_calculation.Battery()
        bty_window = tk.Toplevel(self.master)
        bty_window.title("Battery Design Tool") 
        bty_window.geometry("650x550+300+250") 

        frame_1 = tk.Frame(bty_window, width=650, height=550, bg="white")
        frame_1.pack(fill=tk.BOTH)

        title_label = tk.Label(frame_1, text="Electrical Vehicle Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        title_label.place(x=200, y=50)

        logo_img_1 = tk.PhotoImage(file="images/logo.png")
        logo_label = tk.Label(frame_1, image = logo_img_1, bg="#f8f8f8", fg="#f8f8f8" )
        logo_label.image = logo_img_1
        logo_label.place(x=60, y=20) 

        label_1 = tk.Label(frame_1, text="Initial Velocity :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_1.place(x=70, y=170)
        self.entry_11 = tk.Entry(frame_1, font="Times 15 bold", width=10, state = tk.DISABLED)
        self.entry_11.place(x=220, y=170)

        label_2 = tk.Label(frame_1, text="Final Velocity :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_2.place(x=70, y=220)
        self.entry_12 = tk.Entry(frame_1, font="Times 15 bold", width=10, state = tk.DISABLED)
        self.entry_12.place(x=220, y=220)

        label_3 = tk.Label(frame_1, text="Acceleartion :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_3.place(x=370, y=170)
        self.entry_13 = tk.Entry(frame_1, font="Times 15 bold", width=10, state = tk.DISABLED)
        self.entry_13.place(x=500, y=170)

        label_4 = tk.Label(frame_1, text="Time :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_4.place(x=370, y=220)
        self.entry_14 = tk.Entry(frame_1, font="Times 15 bold", width=10, state = tk.DISABLED)
        self.entry_14.place(x=500, y=220)


        frame_2 = tk.LabelFrame(bty_window, text=" Mode Selection ", width=170, height=170, bg="white")
        frame_2.place(x=250, y=270)

        self.var = tk.IntVar()

        R1 = tk.Radiobutton(frame_2, text="Idle      ", variable=self.var, value=1, bg="white",
                  activeforeground="green", borderwidth="0",  command=self.radio_selection)
        R1.pack(pady=(10,0))

        R2 = tk.Radiobutton(frame_2, text="Cruise    ", variable=self.var, value=2, bg="white", 
                  activeforeground = "green", borderwidth="0", command=self.radio_selection)
        R2.pack()

        R3 = tk.Radiobutton(frame_2, text="Accelerate", variable=self.var, value=3, bg="white",
                  activeforeground = "green", borderwidth="0", command=self.radio_selection)
        R3.pack()

        R4 = tk.Radiobutton(frame_2, text="Brake     ", variable=self.var, value=4, bg="white",
                  activeforeground = "green", borderwidth="0", command=self.radio_selection)
        R4.pack(pady=(0,10))

        button_2_img = tk.PhotoImage(file="images/button_2.png")
        button_add = tk.Button(frame_1, image=button_2_img, bg="white", bd = "0", command=self.generate_add)
        button_add.image = button_2_img
        button_add.place(x=100, y=450)

        button_1_img = tk.PhotoImage(file="images/button_1.png")
        button_generate = tk.Button(frame_1, image=button_1_img, bg="white", bd = "0", command=self.generate_battery)
        button_generate.image = button_1_img
        button_generate.place(x=400, y=450)


    def generate_add(self):

        id = self.var.get()

        
        try:
            if id == 1:
                time = float(self.entry_14.get())
                self.bat_cal.idle(time)
                print(self.bat_cal.energy_required(1500))
            elif id == 2:
                vel = float(self.entry_11.get())
                time = float(self.entry_14.get())
                self.bat_cal.cruise(vel, time)
                print(self.bat_cal.energy_required(1500))
            elif id == 3:
                ini_vel = float(self.entry_11.get())
                fin_vel = float(self.entry_12.get())
                acc = float(self.entry_13.get())
                self.bat_cal.accelerate(ini_vel,fin_vel,acc)
                print(self.bat_cal.energy_required(1500))
            elif id == 4:
                ini_vel = float(self.entry_11.get())
                fin_vel = float(self.entry_12.get())
                acc = float(self.entry_13.get())
                self.bat_cal.decelerate(ini_vel,fin_vel,acc)
                print(self.bat_cal.energy_required(1500))

        except Exception as e:
            message = "Error: Check the values"
            print(e)
 

    def radio_selection(self):

        id = self.var.get()

        if id == 1:
            self.entry_11.config(state = tk.DISABLED)
            self.entry_12.config(state = tk.DISABLED)
            self.entry_13.config(state = tk.DISABLED)
            self.entry_14.config(state = tk.NORMAL)
            print("1")
        
        elif id == 2:

            self.entry_11.config(state = tk.NORMAL)
            self.entry_12.config(state = tk.DISABLED)
            self.entry_13.config(state = tk.DISABLED)
            self.entry_14.config(state = tk.NORMAL)
            print("2")
        
        elif id == 3:

            self.entry_11.config(state = tk.NORMAL)
            self.entry_12.config(state = tk.NORMAL)
            self.entry_13.config(state = tk.NORMAL)
            self.entry_14.config(state = tk.DISABLED)
            print("3")
        
        elif id ==4:
            self.entry_11.config(state = tk.NORMAL)
            self.entry_12.config(state = tk.NORMAL)
            self.entry_13.config(state = tk.NORMAL)
            self.entry_14.config(state = tk.DISABLED)
            print("4")
        
        else:
            print("Invalid")
    
    def generate_battery(self):

        def inner_func():
            ran = float(self.e.get())
            pop_up.destroy()
            sub_pop_up = tk.Tk()
            sub_pop_up.title("Battery Specification")
            w = 400     
            h = 200     
            sw = sub_pop_up.winfo_screenwidth()
            sh = sub_pop_up.winfo_screenheight()
            x = (sw - w)/2
            y = (sh - h)/2
            sub_pop_up.geometry('%dx%d+%d+%d' % (w, h, x, y))

            try:
                cap = int(self.bat_cal.energy_required(ran))
                message = "Battery Capacity = " + str(cap) + " std. units"
            except Exception as e:
                message = "Error: Check your values"

            frame_temp = tk.Frame(sub_pop_up, bg="white", width=400, height=200)
            frame_temp.pack()

            m = tk.Label(sub_pop_up, text=message, font="Times 12", bg="white")
            m.place(x=100, y= 50)
            b = tk.Button(sub_pop_up, text="Okay", font = "Times 12 bold", bg="white", fg="#95b889", bd = "0", highlightthickness=4, 
            highlightcolor="#000000", highlightbackground="#000000", width=10, command=sub_pop_up.destroy)
            b.place(x=130, y= 100)
            tk.mainloop()

        pop_up = tk.Tk()
        pop_up.title("Battery Specification")
        w = 400     
        h = 200     
        sw = pop_up.winfo_screenwidth()
        sh = pop_up.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        pop_up.geometry('%dx%d+%d+%d' % (w, h, x, y))
        frame_temp = tk.Frame(pop_up, bg="white", width=400, height=200)
        frame_temp.pack()
        m = tk.Label(frame_temp, text="Enter Range:", font="Times 12", bg="white")
        m.place(x=120, y= 50)
        self.e = tk.Entry(frame_temp, font="Times 12", width = 5, bg="white")
        self.e.place(x=220, y= 50)
        button_3 = tk.Button(frame_temp, text="Generate", font = "Times 12 bold", bg="white", fg="#95b889", bd = "0", highlightthickness=4, 
        highlightcolor="#000000", highlightbackground="#000000", command = inner_func,width=10)
        button_3.place(x=150, y=100)
        tk.mainloop()


        
def main():
  
    root = tk.Tk()
    root.geometry("650x550+300+250")
    root.resizable(False, False)
    root.title("EV Design Tool")
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()
