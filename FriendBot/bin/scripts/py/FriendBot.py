from time import sleep
import bot
import tkinter as tk
import caffeine
  
if __name__ == "__main__":

    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 700, height = 430)
    canvas1.pack()
    
    
    L1 = tk.Label(root, text="User Name:")
    L1.pack()
    global E1
    E1 = tk.Entry(root, bd =5)
    E1.pack()
    
    L2 = tk.Label(root, text="Password:")
    L2.pack()
    global E2
    E2 = tk.Entry(root, bd =5,show="*")
    E2.pack()
    
    L3 = tk.Label(root, text="Similar accounts to yours (account1,account2, ... ): ")
    L3.pack()
    global E3
    E3 = tk.Entry(root, bd =5,xscrollcommand=True,width=30)
    E3.pack()

    def botting():  
        while True:
            try:
                print("\n\n")
                print("************** \n\n ^-^ Good Morning! Your Bot here :) lets get to work. \n\n**************  \n\n")
                bot.bot(getCreds())  ####  RUN THE BOT
                print("\n\n")
                print("************** \n\n ^-^ Good Night! Restarting soon. I dont sleep long. \n\n************  \n\n")
                sleep(60 * 2)
            
            except:
                print("\n\n")
                print("************** \n\n >:| Something Broke! Trying again in 2 minutes. \n\n************  \n\n")
            
                sleep(60 * 2)

    def getCreds():
        username = E1.get()
        password = E2.get()
        accounts = E3.get()

        return([username,password,accounts.split(",")])


    button1 = tk.Button(text='Enter Instagram credentials below, then click here to begin.',height=10,width=50,
                        font='helvetica',activebackground='green',relief='ridge',activeforeground='red',
                        bd=30,highlightcolor='red',command=botting, bg='peach puff',fg='dark slate gray')

    
    canvas1.create_window(350, 290, window=button1)
    root.mainloop()


