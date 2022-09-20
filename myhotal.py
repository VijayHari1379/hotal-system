from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox 
from playsound import playsound



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hari Park")
        self.root.geometry("1350x750+0+0")
        


        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        v5=StringVar()
        v6=StringVar()
        v7=StringVar()
        v8=StringVar()
        v9=StringVar()
        v10=StringVar()
        v11=StringVar()
        v12=StringVar()
        v13=StringVar()
        v14=StringVar()
        v15=StringVar()
        v16=StringVar()
        v17=StringVar()
        v18=StringVar()
        v19=StringVar()
        v20=StringVar()
        v21=StringVar()
        v22=StringVar()
        v23=StringVar()
        v24=StringVar()
        v25=StringVar()
        v26=StringVar()
        v27=StringVar()
        v28=StringVar()
        v29=StringVar()
        v30=StringVar()
        v31=StringVar()
        v32=StringVar()
        v33=StringVar()
        v34=StringVar()
        v35=StringVar()
        v36=StringVar()
        Total_bill=StringVar()
        
        
            
    #=========================================================Function mdeclaration===================================================================
        def iExit():
            while True:
                if iBill_Order:
                    playsound(r'C:\Users\hari\Downloads\no1.WAV')
                    break
                
            iExit=tkinter.messagebox.askyesno("Hari Park","Confirm If You Want To Exit")
            if iExit >0:
                root.destroy()
                return

        def iBill_Order():
            while True:
                if iBill_Order:
                    playsound(r'C:\Users\hari\Downloads\no2.WAV')
                    break
                

            

            self.txtprescription.insert(END,'Idly:  \t\t\tRs.40'  + "\n")
            self.txtprescription.insert(END,'Dosa \t\t\tRs.45' + "\n")
            self.txtprescription.insert(END,'Vadai: \t\t\tRs.15'  + "\n")
            self.txtprescription.insert(END,'Poori: \t\t\tRs.35'  + "\n")
            self.txtprescription.insert(END,'Mysore Bonda: \t\t\tRs.15'  + "\n")
            self.txtprescription.insert(END,'Upma: \t\t\tRs.45'  + "\n")
            self.txtprescription.insert(END,'Uthappam: \t\t\tRs.50'  + "\n")
            self.txtprescription.insert(END,'Appam: \t\t\tRs.35'  + "\n")
            self.txtprescription.insert(END,'Puttu: \t\t\tRs.60'  + "\n")
            self.txtprescription.insert(END,'Rava_Dosa: \t\t\tRs.45'  + "\n")
            self.txtprescription.insert(END,'Pongal: \t\t\tRs.75'  + "\n")
            self.txtprescription.insert(END,'Chicken Biriyani: \t\t\tRs.265'  + "\n")
            self.txtprescription.insert(END,'Mutton_Biriyani: \t\t\tRs.425'  + "\n")
            self.txtprescription.insert(END,'Meals: \t\t\tRs.240'  + "\n")
            self.txtprescription.insert(END,'Lemon_rice: \t\t\tRs.50'  + "\n")
            self.txtprescription.insert(END,'Tomato_Rice: \t\t\tRs.50'  + "\n")
            self.txtprescription.insert(END,'Grillchicken: \t\t\tRs.480'  + "\n")
            self.txtprescription.insert(END,'Carrot_Rice: \t\t\tRs.50'  + "\n")
            self.txtprescription.insert(END,'Curd_Rice: \t\t\tRs.50'  + "\n")
            self.txtprescription.insert(END,'Coconut_Rice \t\t\tRs.60' + "\n")
            self.txtprescription.insert(END,'Sambar_Rice: \t\t\tRs.55'  + "\n")
            self.txtprescription.insert(END,'Fried_Rice: \t\t\tRs.90' + "\n")
            self.txtprescription.insert(END,'Prawn_Rice: \t\t\tRs.160'  + "\n")
            self.txtprescription.insert(END,'Chicken_rice: \t\t\tRs.250'  + "\n")
            self.txtprescription.insert(END,' Egg_rice: \t\t\tRs.200'  + "\n")
            self.txtprescription.insert(END,'Veg_rice: \t\t\tRs.180'  + "\n")
            self.txtprescription.insert(END,'Dosa: \t\t\tRs.40'  + "\n")
            self.txtprescription.insert(END,'Parota: \t\t\tRs.65'  + "\n")
            self.txtprescription.insert(END,'Grill_chicken: \t\t\tRs.480'  + "\n")
            self.txtprescription.insert(END,'Chapati: \t\t\tRs.40'  + "\n")
            self.txtprescription.insert(END,'Masala_dosa: \t\t\tRs.70' + "\n")
            self.txtprescription.insert(END,'Masaladosa: \t\t\tRs.90'  + "\n")
            self.txtprescription.insert(END,'Ice_cream: \t\t\tRs.115'  + "\n")
            self.txtprescription.insert(END,'Juice: \t\t\tRs.90'  + "\n")
            self.txtprescription.insert(END,'Cakes: \t\t\tRs.45'  + "\n")


            

            


            
        
            
        def iTotal_Amount():
            while True:
                if iBill_Order:
                    playsound(r'C:\Users\hari\Downloads\no3.WAV')
                    break
            
            
            
            try:a1=int(v1.get())
            except: a1=0

            try:a2=int(v2.get())
            except: a2=0

            try:a3=int(v3.get())
            except: a3=0

            try:a4=int(v4.get())
            except: a4=0

            try:a5=int(v5.get())
            except: a5=0

            try:a6=int(v6.get())
            except: a6=0

            try:a7=int(v7.get())
            except: a7=0

            try:a8=int(v8.get())
            except: a8=0

            try:a9=int(v9.get())
            except: a9=0

            try:a10=int(v10.get())
            except: a10=0

            try:a11=int(v11.get())
            except: a11=0

            try:a12=int(v12.get())
            except: a12=0

            try:a13=int(v13.get())
            except: a13=0

            try:a14=int(v14.get())
            except: a14=0

            try:a15=int(v15.get())
            except: a15=0

            try:a16=int(v16.get())
            except: a16=0

            try:a17=int(v17.get())
            except: a17=0

            try:a18=int(v18.get())
            except: a18=0

            try:a19=int(v19.get())
            except: a19=0

            try:a20=int(v20.get())
            except: a20=0

            try:a21=int(v21.get())
            except: a21=0

            try:a22=int(v22.get())
            except: a22=0

            try:a23=int(v23.get())
            except: a23=0

            try:a24=int(v24.get())
            except: a24=0

            try:a25=int(v25.get())
            except: a25=0

            try:a26=int(v26.get())
            except: a26=0

            try:a27=int(v27.get())
            except: a27=0

            try:a28=int(v28.get())
            except: a28=0

            try:a29=int(v29.get())
            except: a29=0

            try:a30=int(v30.get())
            except: a30=0

            try:a31=int(v31.get())
            except: a31=0

            try:a32=int(v32.get())
            except: a32=0

            try:a33=int(v33.get())
            except: a33=0

            try:a34=int(v34.get())
            except: a34=0

            try:a35=int(v35.get())
            except: a35=0

            try:a36=int(v36.get())
            except: a36=0

            


            #Define cost quantity

            c1=60*a1
            c2=30*a2
            c3=10*a3
            c4=30*a4
            c5=60*a5
            c6=25*a6
            c7=40*a7
            c8=30*a8
            c9=40*a9
            c10=30*a10
            c11=60*a11
            c12=30*a12
            c13=10*a13
            c14=30*a14
            c15=60*a15
            c16=25*a16
            c17=40*a17
            c18=30*a18
            c19=40*a19
            c20=30*a20
            c21=60*a21
            c22=30*a22
            c23=10*a23
            c24=30*a24
            c25=60*a25
            c26=25*a26
            c27=40*a27
            c28=30*a28
            c29=40*a29
            c30=30*a30
            c31=60*a31
            c32=30*a32
            c33=10*a33
            c34=30*a34
            c35=60*a35
            c36=60*a36

            lbl_Total=Label(FrameDetail,font=("aria",20,"bold"),text="TOTAL BILL",width=70,fg="black",bg="white")
            lbl_Total.place(x=0,y=50)

            lbl_Total=Label(FrameDetail,font=("aria",20,"bold"),text="THANKS FOR YOU",width=70,fg="red",bg="white")
            lbl_Total.place(x=0,y=150)

            
            

            entry_Total=Entry(FrameDetail,font=("arial",20,"bold"),textvariable=Total_bill,bd=0,width=20,bg="lightgreen")
            entry_Total.place(x=30,y=100)

            

            totalcost=c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36
            string_bill="Rs.",('%.2f' %totalcost)
            Total_bill.set(string_bill)


        

        def iReset():
            while True:
                if iBill_Order:
                    playsound(r'C:\Users\hari\Downloads\no4.WAV')
                    break

            v1.set("")
            v2.set("")
            v3.set("")
            v4.set("")
            v5.set("")
            v6.set("")
            v7.set("")
            v8.set("")
            v9.set("")
            v10.set("")
            v11.set("")
            v12.set("")
            v13.set("")
            v14.set("")
            v15.set("")
            v16.set("")
            v17.set("")
            v18.set("")
            v19.set("")
            v20.set("")
            v21.set("")
            v22.set("")
            v23.set("")
            v24.set("")
            v25.set("")
            v26.set("")
            v27.set("")
            v28.set("")
            v29.set("")
            v30.set("")
            v31.set("")
            v32.set("")
            v33.set("")
            v34.set("")
            v35.set("")
            v36.set("")
            
            
            self.txtprescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return





            
    #=========================================================Frame===================================================================
        MainFrame = Frame(self.root)
        MainFrame.grid()


        TitleFrame = Frame(MainFrame, bd=5,width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,width=39,bg="green",fg="white",font=("arial",39,"bold"),text="HARI HOTEL",padx=0)
        self.lblTitle.grid()
       

        FrameDetail = Frame(MainFrame, bd=5,width=1350,height=210,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=5,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=5,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=5,width=1350,height=300,padx=20,relief=RIDGE
                              ,font=("arial",12,"bold"),fg="red",text="-------------------TIFFIN: -------------------------------------LUNCH----------------------------------------DINNER-------------------------------")
        DataFrameLEFT.pack(side=LEFT)

       

        

        DataFrameRIGHT = LabelFrame(DataFrame, bd=5,width=450,height=300,padx=20,relief=RIDGE
                                    ,font=("arial",12,"bold"),text="-------------------------------------MENU-----------------------------",fg='red')
        DataFrameRIGHT.pack(side=RIGHT)
  #===================================================DataFrameLEFT==================================================
       

        


        self.lbl1=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Idly:",padx=2,pady=2)
        self.lbl1.grid(row=0,column=0,sticky=W)
        self.txt1=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v1,width=10)
        self.txt1.grid(row=0,column=1)

        self.lbl2=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Chicken Biriyani:",padx=2,pady=2)
        self.lbl2.grid(row=0,column=2,sticky=W)
        self.txt2=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v2,width=10)
        self.txt2.grid(row=0,column=3)

        self.lbl3=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Chicken rice:",padx=2,pady=2)
        self.lbl3.grid(row=0,column=4,sticky=W)
        self.txt3=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v3,width=10)
        self.txt3.grid(row=0,column=5)

        self.lbl4=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Dosa:",padx=0,pady=0)
        self.lbl4.grid(row=1,column=0,sticky=W)
        self.txt4=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v4,width=10)
        self.txt4.grid(row=1,column=1)

        self.lbl5=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Mutton Biriyani:",padx=2,pady=2)
        self.lbl5.grid(row=1,column=2,sticky=W)
        self.txt5=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v5,width=10)
        self.txt5.grid(row=1,column=3)

        self.lbl6=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Egg rice:",padx=2,pady=2)
        self.lbl6.grid(row=1,column=4,sticky=W)
        self.txt6=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v6,width=10)
        self.txt6.grid(row=1,column=5)

        self.lbl7=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Vadai:",padx=2,pady=2)
        self.lbl7.grid(row=2,column=0,sticky=W)
        self.txt7=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v7,width=10)
        self.txt7.grid(row=2,column=1)

        self.lbl8=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Meals:",padx=2,pady=2)
        self.lbl8.grid(row=2,column=2,sticky=W)
        self.lbl8=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v8,width=10)
        self.lbl8.grid(row=2,column=3)

        self.lbl9=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Veg rice",padx=2,pady=2)
        self.lbl9.grid(row=2,column=4,sticky=W)
        self.txt9=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v9,width=10)
        self.txt9.grid(row=2,column=5)
        
        self.lbl10=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Poori:",padx=2,pady=2)
        self.lbl10.grid(row=3,column=0,sticky=W)
        self.lbl10=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v10,width=10)
        self.lbl10.grid(row=3,column=1)

        self.lbl11=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Lemon rice:",padx=2,pady=2)
        self.lbl11.grid(row=3,column=2,sticky=W)
        self.txt11=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v11,width=10)
        self.txt11.grid(row=3,column=3)

        self.lbl12=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Dosa:",padx=2,pady=2)
        self.lbl12.grid(row=3,column=4,sticky=W)
        self.txt12=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v12,width=10)
        self.txt12.grid(row=3,column=5)

        self.lbl13=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Masala Dosa:",padx=2,pady=2)
        self.lbl13.grid(row=4,column=0,sticky=W)
        self.txt13=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v13,width=10)
        self.txt13.grid(row=4,column=1)

        self.lbl14=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Mutton chukka:",padx=2,pady=2)
        self.lbl14.grid(row=4,column=2,sticky=W)
        self.txt14=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v14,width=10)
        self.txt14.grid(row=4,column=3)

        self.lbl14=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Parota:",padx=2,pady=2)
        self.lbl14.grid(row=4,column=4,sticky=W)
        self.txt14=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v15,width=10)
        self.txt14.grid(row=4,column=5)

        self.lbl15=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Mysore Bonda:                ",padx=2,pady=2)
        self.lbl15.grid(row=5,column=0,sticky=W)
        self.txt15=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v16,width=10)
        self.txt15.grid(row=5,column=1)

        self.lbl16=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Tomato Rice:                  ",padx=2,pady=2)
        self.lbl16.grid(row=5,column=2,sticky=W)
        self.txt16=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v17,width=10)
        self.txt16.grid(row=5,column=3)

        self.lbl17=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Grill chicken:                 ",padx=2,pady=2)
        self.lbl17.grid(row=5,column=4,sticky=W)
        self.txt17=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v18,width=10)
        self.txt17.grid(row=5,column=5)

        self.lbl18=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Upma:",padx=2,pady=2)
        self.lbl18.grid(row=6,column=0,sticky=W)
        self.txt18=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v19,width=10)
        self.txt18.grid(row=6,column=1)

        self.lbl19=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Grill chicken:",padx=2,pady=2)
        self.lbl19.grid(row=6,column=2,sticky=W)
        self.txt19=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v20,width=10)
        self.txt19.grid(row=6,column=3)

        self.lbl20=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Chapati:",padx=2,pady=2)
        self.lbl20.grid(row=6,column=4,sticky=W)
        self.txt20=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v21,width=10)
        self.txt20.grid(row=6,column=5)

        self.lbl21=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Uthappam",padx=2,pady=2)
        self.lbl21.grid(row=7,column=0,sticky=W)
        self.txt21=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v22,width=10)
        self.txt21.grid(row=7,column=1)

        self.lbl22=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Carrot Rice:",padx=2,pady=2)
        self.lbl22.grid(row=7,column=2,sticky=W)
        self.txt22=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v23,width=10)
        self.txt22.grid(row=7,column=3)

        self.lbl23=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Masala dosa:",padx=2,pady=2)
        self.lbl23.grid(row=7,column=4,sticky=W)
        self.txt23=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v24,width=10)
        self.txt23.grid(row=7,column=5)

        self.lbl24=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Appam:",padx=2,pady=2)
        self.lbl24.grid(row=8,column=0,sticky=W)
        self.txt24=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v25,width=10)
        self.txt24.grid(row=8,column=1)

        self.lbl25=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Curd Rice:",padx=2,pady=2)
        self.lbl25.grid(row=8,column=2,sticky=W)
        self.txt25=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v26,width=10)
        self.txt25.grid(row=8,column=3)

        self.lbl26=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Ice cream:",padx=2,pady=2)
        self.lbl26.grid(row=8,column=4,sticky=W)
        self.txt26=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v27,width=10)
        self.txt26.grid(row=8,column=5)

        self.lbl27=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Puttu:       ",padx=2,pady=2)
        self.lbl27.grid(row=9,column=0,sticky=W)
        self.txt27=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v28,width=10)
        self.txt27.grid(row=9,column=1)

        self.lbl28=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Coconut rice:       ",padx=2,pady=2)
        self.lbl28.grid(row=9,column=2,sticky=W)
        self.txt28=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v29,width=10)
        self.txt28.grid(row=9,column=3)

        self.lbl29=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Prawn rice:        ",padx=2,pady=2)
        self.lbl29.grid(row=9,column=4,sticky=W)
        self.txt29=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v30,width=10)
        self.txt29.grid(row=9,column=5)

        self.lbl30=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Rava Dosa",padx=2,pady=2)
        self.lbl30.grid(row=10,column=0,sticky=W)
        self.txt30=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v31,width=10)
        self.txt30.grid(row=10,column=1)

        self.lbl31=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Sambar rice:",padx=2,pady=2)
        self.lbl31.grid(row=10,column=2,sticky=W)
        self.txt31=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v32,width=10)
        self.txt31.grid(row=10,column=3)

        self.lbl32=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Juice:",padx=2,pady=2)
        self.lbl32.grid(row=10,column=4,sticky=W)
        self.txt32=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v33,width=10)
        self.txt32.grid(row=10,column=5)

        self.lbl33=Label(DataFrameLEFT,font=("arial",11,"bold"),text="Pongal:",padx=2,pady=2)
        self.lbl33.grid(row=11,column=0,sticky=W)
        self.txt33=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v34,width=10)
        self.txt33.grid(row=11,column=1)

        self.lbl34=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Fried rice:",padx=2,pady=2)
        self.lbl34.grid(row=11,column=2,sticky=W)
        self.txt34=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v35,width=10)
        self.txt34.grid(row=11,column=3)

        self.lbl35=Label(DataFrameLEFT,font=("arial",11,"bold"),text="  Cakes:",padx=2,pady=2)
        self.lbl35.grid(row=11,column=4,sticky=W)
        self.txt35=Entry(DataFrameLEFT,font=("arial",11,"bold"),textvariable=v36,width=10)
        self.txt35.grid(row=11,column=5)


       

        

        
        #===================================================DataFrameRIGHT==================================================

        self.txtprescription=Text(DataFrameRIGHT,font=("arial",12,"bold"),width=40,height=16 ,padx=2,pady=8)
        self.txtprescription.grid(row=0,column=0)

        
        #===================================================ButtonFrame==================================================
        self.btnprescription=Button(ButtonFrame,text='MENU',bg="green",fg="white",font=("arial",12,"bold"),width=31,bd=2,
                                    command=iBill_Order)
        self.btnprescription.grid(row=0,column=0)

        self.btnFrameDetail=Button(ButtonFrame,text='Total Amount',bg="green",fg="white",font=("arial",12,"bold"),width=29,bd=2,
                               command=iTotal_Amount)
        self.btnFrameDetail.grid(row=0,column=1)
        

        
        self.btnReset=Button(ButtonFrame,text='Reset',bg="green",fg="white",font=("arial",12,"bold"),width=31,bd=2,
                             command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(ButtonFrame,text='Exit',bg="green",fg="white",font=("arial",12,"bold"),width=31,bd=2,command=iExit)
        self.btnExit.grid(row=0,column=4)
        

        #===================================================FrameDetail==================================================

        self.lblLabel=Label(FrameDetail,font=("arial",10,"bold"),pady=4,
        text="TOTAL AMOUNT IS",)
        self.lblLabel.grid(row=0,column=0)


        self.txtFrameDetail=Text(FrameDetail,font=("arial",12,"bold"),width=140,height=8 ,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

        

       

        

       







if __name__=='__main__':
    root=Tk()
    application = Hospital(root)
    root.mainloop()
