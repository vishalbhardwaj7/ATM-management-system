import tkinter as tk
import time
from tkinter import font  as tkfont
from tkinter import messagebox
current_balance=10000
pin='1234'
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage,BalancePage,ChangePin,Exit):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('G6')
        self.controller.state('zoomed')
        heading_label=tk.Label(self, text='G6 ATM',font=('italic',45,'bold'),foreground='white',background='#3d3d5c')
        heading_label.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        password_label=tk.Label(self,text='Enter 4 Digit Pin',font=('italic',14),bg='#3d3d5c',fg='white')
        password_label.pack(pady=10)

        my_password=tk.StringVar()
        password_entry=tk.Entry(self,textvariable=my_password, font=('italic',13),width=22)
        password_entry.focus_set()
        password_entry.pack(ipady=7)
        def handle_focus_in(_):
            password_entry.configure(fg='black',show='*')
        password_entry.bind('<FocusIn>',handle_focus_in)



        def check_password():

            if my_password.get()==pin:
               my_password.set('')
               incorrect_password_label['text']=''
               controller.show_frame('MenuPage')
            else:
                incorrect_password_label['text']='Incorrect Pin'
        button=tk.Button(self, text='Submit',command=check_password,relief='raised',borderwidth=1,width=15,height=1)
        button.pack(pady=10)

        incorrect_password_label=tk.Label(self,text='',font=('italic',13),fg='white',bg='#33334d',anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)

        bottom_frame=tk.Frame(self,relief='raised',borderwidth=13)
        bottom_frame.pack(fill='x',side='bottom')
        def toc():
            current_time=time.strftime('%I:%M%p')
            time_label.config(text=current_time)
            time_label.after(200,toc)
        time_label=tk.Label(bottom_frame,font=('italic',10))
        time_label.pack(side='right')    
        toc()

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        heading_label=tk.Label(self, text='G6 ATM',font=('italic',45,'bold'),foreground='white',background='#3d3d5c')
        heading_label.pack(pady=25)
        main_menu_label=tk.Label(self,text='Main Menu',font=('italic',13),fg='white',bg='#3d3d5c')
        main_menu_label.pack()

        selection_label=tk.Label(self,text='Please make a selection',font=('italic',13),fg='white',bg='#3d3d5c',anchor='w')
        selection_label.pack(fill='x')
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label=tk.Label(self,textvariable=controller.shared_data['Balance'],font=('italic',13),fg='white',bg='#3d3d5c',anchor='e')
        balance_label.pack(fill='x')
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
        withdraw_button=tk.Button(button_frame,text='Withdraw',command=withdraw,relief='raised',borderwidth=3,width=50,height=5)
        withdraw_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame('DepositPage')
        deposit_button=tk.Button(button_frame,text='Deposit',command=deposit,relief='raised',borderwidth=3,width=50,height=5)
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame('BalancePage')
        balance_button=tk.Button(button_frame,text='Balance',command=balance,relief='raised',borderwidth=3,width=50,height=5)
        balance_button.grid(row=2,column=0,pady=5)
        
        def changepin():
            controller.show_frame('ChangePin')
        changepin_button=tk.Button(button_frame,text='ChangePin',command=changepin,relief='raised',borderwidth=3,width=50,height=5)
        changepin_button.grid(row=3,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
        exit_button=tk.Button(button_frame,text='Exit',command=exit,relief='raised',borderwidth=3,width=50,height=5)
        exit_button.grid(row=4,column=0,pady=5)


        bottom_frame=tk.Frame(self,relief='raised',borderwidth=13)
        bottom_frame.pack(fill='x',side='bottom')
        def toc():
           current_time=time.strftime('%I:%M%p')
           time_label.config(text=current_time)
           time_label.after(200,toc)
        time_label=tk.Label(bottom_frame,font=('italic',10))
        time_label.pack(side='right')    
        toc()
        
       
        


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        heading_label=tk.Label(self, text='G6 ATM',font=('italic',45,'bold'),foreground='#ffffff',background='#3d3d5c')
        heading_label.pack(pady=25)
        choose_amount_label=tk.Label(self,text='Choose the amount you want to withdraw',font=('italic',13),fg='white',bg='#3d3d5c')
        choose_amount_label.pack()
        
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            if amount<=current_balance:
                tk.Label()
                current_balance-=amount
                controller.shared_data['Balance'].set(current_balance)
                messagebox.showinfo("Successful", "Successful")
                controller.show_frame('MenuPage')
            else:
                messagebox.showerror("Failed", "Insufficient Balance")


        hundred_button=tk.Button(button_frame,text='500',command=lambda:withdraw(500),relief='raised',borderwidth=3,width=50,height=5)
        hundred_button.grid(row=0,column=0,pady=5)

        thousand_button=tk.Button(button_frame,text='1000',command=lambda:withdraw(1000),relief='raised',borderwidth=3,width=50,height=5)
        thousand_button.grid(row=1,column=0,pady=5)

        two_thousand_button=tk.Button(button_frame,text='2000',command=lambda:withdraw(2000),relief='raised',borderwidth=3,width=50,height=5)
        two_thousand_button.grid(row=2,column=0,pady=5)

        five_thousand_button=tk.Button(button_frame,text='5000',command=lambda:withdraw(5000),relief='raised',borderwidth=3,width=50,height=5)
        five_thousand_button.grid(row=3,column=0,pady=5)

        eight_thousand_button=tk.Button(button_frame,text='8000',command=lambda:withdraw(8000),relief='raised',borderwidth=3,width=50,height=5)
        eight_thousand_button.grid(row=0,column=1,pady=5,padx=810)

        ten_thousand_button=tk.Button(button_frame,text='10000',command=lambda:withdraw(10000),relief='raised',borderwidth=3,width=50,height=5)
        ten_thousand_button.grid(row=1,column=1,pady=5,padx=810)

        twelve_thousand_button=tk.Button(button_frame,text='12000',command=lambda:withdraw(12000),relief='raised',borderwidth=3,width=50,height=5)
        twelve_thousand_button.grid(row=2,column=1,pady=5,padx=810)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,textvariable=cash,width=60,justify='right')
        other_amount_entry.grid(row=3, column=1, pady=5,ipady=30)


        def other_amount(_):
            global current_balance
            if int(cash.get())<=current_balance:
                current_balance-=int(cash.get())
                controller.shared_data['Balance'].set(current_balance)
                cash.set('')
                messagebox.showinfo("Successful", "Successful")
                controller.show_frame('MenuPage')
            else:
                messagebox.showerror("Failed", "Insufficient Balance")

        other_amount_entry.bind('<Return>',other_amount)
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label=tk.Label(self,textvariable=controller.shared_data['Balance'],font=('italic',13),fg='white',bg='#3d3d5c',anchor='w')
        balance_label.pack(fill='x')
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=13)
        bottom_frame.pack(fill='x',side='bottom')

        def toc():
            current_time=time.strftime('%I:%M%p')
            time_label.config(text=current_time)
            time_label.after(200,toc)
        time_label=tk.Label(bottom_frame,font=('italic',10))
        time_label.pack(side='right')
        toc()


class DepositPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        heading_label=tk.Label(self, text='G6 ATM',font=('italic',45,'bold'),foreground='white',background='#3d3d5c')
        heading_label.pack(pady=25)
        space_label = tk.Label(self,font=('italic',13),fg='white',bg='#3d3d5c')
        space_label.pack()
        enter_amount_label = tk.Label(self,text='Enter amount',font=('italic',13),fg='white',bg='#3d3d5c')
        enter_amount_label.pack(pady=15)
        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,textvariable=cash,font=('italic',12),width=30)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            messagebox.showinfo("Successful", "Successful")
            controller.show_frame('MenuPage')
            cash.set('')
            
        enter_button = tk.Button(self,text='Enter',command=deposit_cash,relief='raised',borderwidth=3,width=25,height=1)                                  
        enter_button.pack(pady=10)
        two_tone_label = tk.Label(self,bg='#33334d')
        two_tone_label.pack(fill='both',expand=True)
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        def toc():
            current_time=time.strftime('%I:%M%p')
            time_label.config(text=current_time)
            time_label.after(200,toc)
        time_label=tk.Label(bottom_frame,font=('italic',10))
        time_label.pack(side='right')    
        toc()
class BalancePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        heading_label = tk.Label(self,text='G6 ATM',font=('italic',45,'bold'),foreground='#ffffff',background='#3d3d5c')                      
        heading_label.pack(pady=25)
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label=tk.Label(self,textvariable=controller.shared_data['Balance'],font=('italic',13),fg='white',bg='#3d3d5c',anchor='w')
        balance_label.pack(fill='x')
        
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')
        menu_button = tk.Button(button_frame,command=menu,text='Menu',relief='raised',borderwidth=3,width=50,height=5)                   
        menu_button.grid(row=0,column=0,pady=5)
        
        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,text='Exit',command=exit,relief='raised',borderwidth=3,width=50, height=5)            
        exit_button.grid(row=1,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        def toc():
            current_time=time.strftime('%I:%M%p')
            time_label.config(text=current_time)
            time_label.after(200,toc)
        time_label=tk.Label(bottom_frame,font=('italic',10))
        time_label.pack(side='right')    
        toc()

class ChangePin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        heading_label = tk.Label(self,text='G6 ATM',font=('italic',45,'bold'),foreground='#ffffff',background='#3d3d5c')                      
        heading_label.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        password_label=tk.Label(self,text='Enter Old Pin',font=('italic',14),bg='#3d3d5c',fg='white')
        password_label.pack(pady=10)

        old_pin=tk.StringVar()
        password_entry=tk.Entry(self,textvariable=old_pin, font=('italic',13),width=22,show='*')
        password_entry.focus_set()
        password_entry.pack(ipady=7)

        password_label=tk.Label(self,text='Enter New Pin',font=('italic',14),bg='#3d3d5c',fg='white')
        password_label.pack(pady=10) 
        new_pin=tk.StringVar()
        password_entry=tk.Entry(self,textvariable=new_pin, font=('italic',13),width=22, show="*")
        password_entry.focus_set()
        password_entry.pack(ipady=7)
      
        password_label=tk.Label(self,text='Enter Confirm Pin',font=('italic',14),bg='#3d3d5c',fg='white')
        password_label.pack(pady=10)
        conf_pin=tk.StringVar()
        password_entry=tk.Entry(self,textvariable=conf_pin, font=('italic',13),width=22,show='*')
        password_entry.focus_set()
        password_entry.pack(ipady=7)
        
        
        def check_password(): 
            global pin   
            if old_pin.get() == pin and new_pin.get() == conf_pin.get():
                pin=new_pin.get()
                messagebox.showinfo("Successful", "Pin Successfully Changed")
                controller.show_frame('StartPage')
            else:
                messagebox.showerror("Failed", "Pin Mismatch")
                


        button=tk.Button(self, text='Submit',command=check_password,relief='raised',borderwidth=1,width=15,height=1)
        button.pack(pady=10)
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=13)
        bottom_frame.pack(fill='x',side='bottom')
        controller.show_frame('StartPage')
        
        def toc():
            current_time=time.strftime('%I:%M%p')
            time_label.config(text=current_time)
            time_label.after(200,toc)
        time_label=tk.Label(bottom_frame,font=('italic',10))
        time_label.pack(side='right')    
        toc()
class Exit(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()