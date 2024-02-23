from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox
import tempfile
import subprocess
from time import strftime 
import datetime 

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("KC Billing App")
        # To App Icon
        # self.root.iconbitmap("kc-icon.ico")

        #============Variables=================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        j=random.randint(1000,9999)
        self.bill_no.set(j)
        self.c_email=StringVar()
        self.search_Bill=StringVar()
        self.model=StringVar()
        self.date=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.subtotal=IntVar()
        self.total_sales=IntVar()
        self.total=IntVar()  
        self.imei=StringVar()
        self.desc=StringVar()


        #Product Category list
        self.Category=["Select Option","IOS","Android"]
        self.SubCatIOS=["...","Iphones"]
        self.Iphones=["...","Iphone 6(series)","Iphone 7","Iphone 7+","Iphone 8","Iphone 8+","Iphone X","Iphone XR","Iphone Xs","Iphone Xsmax","Iphone 11","Iphone 11 pro","Iphone 11 promax","Iphone 12","Iphone 12 pro","Iphone 12 promax","Iphone 13","Iphone 13 pro","Iphone 13 promax","Iphone 14","Iphone 14 pro","Iphone 14 promax","Iphone 15","Iphone 15 pro","Iphone 15 promax"]
        self.SubCatAndroid=["...","Infinix","Itel","Tecno"]
        self.Infinix=["...","hot30i","hot40i 4/128","hot40i 8/128","hot40i 8/256","smart8 3/64","smart8 4/64","smart8 4/128","hot40 pro","smart7HD","Zero30"]
        self.Itel=["...","A04","A05s","A70","p55","p55t","p40+"]
        self.Tecno=["...","spark10 8/128","spark20 4/128","spark20 8/128","spark20 8/256","spark20 pro","spark20 pro+","pop8 4/64","pop8 4/128","pop8 3/64","pop7","cammon20"]

        
        
        
        #image 1
        img=Image.open("image/kc-icon.jpg")
        img = img.resize((150, 150), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)



        lbl_img=Label(self.root,bg="brown4",image=self.photoimg)
        lbl_img.place(x=50,y=0,width=1250,height=150)


        lbl_title=Label(self.root, text="Khaleedurl Conglomerate",font=("times new roman",35,"bold"),bg="white",fg="brown4")
        lbl_title.place(x=0,y=130,width=1530,height=80)

        def time():
            string=strftime("%H:%M:%S %p/ %d-%m-%y")
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl= Label(lbl_title, font=("times new roman",16,'bold'),background='white',foreground="brown4")
        lbl.place(x=0,y=0,width=220,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=200,width=1530,height=500)

        # Customer label frame
        cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="brown4")
        cust_Frame.place(x=10,y=5,width=550,height=150)

        self.lbl_mob=Label(cust_Frame,text="Mobile No:",font=("times new roman",10,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=45)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)


        self.lblCustName=Label(cust_Frame,text="Customer Name:",bd=4,font=("arial",10,"bold"),bg="white")# Middle Frame
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(cust_Frame,textvariable=self.c_name,font=("arial",12,"bold"),width=40)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblEmail=Label(cust_Frame,text="Email:",bd=4,font=("arial",10,"bold"),bg="white")
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(cust_Frame,textvariable= self.c_email,font=("arial",12,"bold"),width=40)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
   
        self.lblDate=Label(cust_Frame,text="Date:",bd=4,font=("arial",10,"bold"),bg="white")
        self.lblDate.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        self.txtDate=ttk.Entry(cust_Frame,textvariable= self.date,font=("arial",12,"bold"),width=40)
        self.txtDate.grid(row=3,column=1,sticky=W,padx=5,pady=2)


        # Products label frame
        prod_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="brown4")
        prod_Frame.place(x=10,y=170,width=550,height=230)
        
        #Category
        self.lblCategory=Label(prod_Frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white")
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.Combo_Category=ttk.Combobox(prod_Frame,value=self.Category,font=("times new roman",10,"bold"),state="readonly",width=24)
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #subcategory
        self.lblSubCategory=Label(prod_Frame,text="Subcategory",font=("times new roman",12,"bold"),bg="white")
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.Combo_SubCategory=ttk.Combobox(prod_Frame,value=[""],font=("times new roman",10,"bold"),state="readonly",width=24)
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Model Name
        self.lblmodel=Label(prod_Frame,text="Model",font=("times new roman",12,"bold"),bg="white")
        self.lblmodel.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.Combomodel=ttk.Combobox(prod_Frame,textvariable=self.model,font=("times new roman",10,"bold"),state="readonly",width=24)
        self.Combomodel.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Price
        self.lblPrice=Label(prod_Frame,text="Price",font=("times new roman",10,"bold"),bg="white")
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.txtPrice=ttk.Entry(prod_Frame,textvariable=self.prices,font=("times new roman",10,"bold"),width=15)
        self.txtPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

         #Quantity
        self.lblQty=Label(prod_Frame,text="Qty",font=("times new roman",10,"bold"),bg="white")
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.txtQty=ttk.Entry(prod_Frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=15)
        self.txtQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        self.lblImei=Label(prod_Frame,text="IMEI",font=("times new roman",12,"bold"),bg="white")
        self.lblImei.grid(row=4,column=0,sticky=W,padx=5,pady=9)
        self.txtImei=ttk.Entry(prod_Frame,textvariable=self.imei,font=("times new roman",10,"bold"),width=35)
        self.txtImei.grid(row=4,column=1,sticky=W,padx=5,pady=9)

        self.lbldesc=Label(prod_Frame,text="Description",font=("times new roman",12,"bold"),bg="white")
        self.lbldesc.grid(row=5,column=0,sticky=W,padx=5,pady=9)
        self.txtdesc=ttk.Entry(prod_Frame,textvariable=self.desc,font=("times new roman",10,"bold"),width=35)
        self.txtdesc.grid(row=5,column=1,sticky=W,padx=5,pady=9)




       
        #Middle Buttons
        self.BtnAddToCart=Button(Main_Frame,command=self.AddItems,height=1,width=9,cursor="hand2",text="Add To Cart",font=("arial",15,"bold"),bg="brown4",fg="black",bd=2)
        self.BtnAddToCart.place(x=600,y=20)

        self.BtnGenerateBill=Button(Main_Frame,command=self.gen_bill,height=1,width=9,cursor="hand2",text="Gen. Bill",font=("arial",15,"bold"),bg="brown4",fg="black",bd=2)
        self.BtnGenerateBill.place(x=600,y=90)

        self.BtnSaveBill=Button(Main_Frame,command=self.save_bill ,height=1,width=9,cursor="hand2",text="Save Bill",font=("arial",15,"bold"),bg="brown4",fg="black",bd=2)
        self.BtnSaveBill.place(x=600,y=160)

        self.BtnPrint=Button(Main_Frame,command=self.iprint,height=1,width=9,cursor="hand2",text="Print",font=("arial",15,"bold"),bg="brown4",fg="black",bd=2)
        self.BtnPrint.place(x=600,y=230)

        self.BtnClear=Button(Main_Frame,command=self.clear_bill,height=1,width=9,cursor="hand2",text="Clear",font=("arial",15,"bold"),bg="brown4",fg="black",bd=2)
        self.BtnClear.place(x=600,y=300)

        self.BtnExit=Button(Main_Frame,command=self.root.destroy,height=1,width=9,cursor="hand2",text="Exit",font=("arial",15,"bold"),bg="brown4",fg="black",bd=2)
        self.BtnExit.place(x=600,y=360)


        # Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=800,y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",16,"bold"),fg="black",bg="brown4")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.entrySearch=ttk.Entry(Search_Frame,textvariable=self.search_Bill,font=("times new roman",13,"bold"),width=24)
        self.entrySearch.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,width=12,cursor="hand2",text="Search",bd=2,font=("arial",10,"bold"),bg="brown4",fg="black")
        self.BtnSearch.grid(row=0,column=2,padx=50)
        
        #Right Frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="brown4")
        RightLabelFrame.place(x=755,y=50,width=600,height=360)

        scroll_y=Scrollbar(RightLabelFrame,orient="vertical")
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold")) 
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)  

        # Bill Counter label frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="brown4")
        Bottom_Frame.place(x=0,y=410,width=1520,height=90) 

        self.lblsubtotal=Label(Bottom_Frame,text="Total",font=("times new roman",12,"bold"),bg="white")
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entrysubtotal=ttk.Entry(Bottom_Frame,textvariable=self.subtotal,font=("times new roman",13,"bold"),width=40)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=10,pady=20)


        self.lblcredit=Label(Bottom_Frame,text="Made by bug_Slash",font=("times new roman",12,"bold"),bg="white",fg="brown4")
        self.lblcredit.place(x=1210,y=30)

       

     
        self.welcome()
        self.l=[]

     #================Function Declaration===============
    def welcome(self):
        self.textarea.delete(1.1,END)
        self.textarea.insert(END,"\t\t Welcome To Khaleedurl Conglomerate\n \t\t\t\tMakarfi Plaza")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,"\n================================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice\n")
    
    

    def AddItems(self):
        self.j=self.prices.get()
        self.b=self.qty.get()*self.j
        
        self.l.append(self.b)
        if self.subtotal.get()=="":
            messagebox.showerror("error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.model.get()}\t\t\t{self.qty.get()}\t\t{self.b}")
            self.subtotal.set(str('%.2f'%(sum(self.l))))
 
    def gen_bill(self):
        if self.model.get()=="":
            messagebox.showerror("error","Please Add To Cart ")
        else:

            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,f"\n Descr:\t\t{self.desc.get()}")
            self.textarea.insert(END,f"\n IMEI:\t\t{self.imei.get()}")
            self.textarea.insert(END,"\n=================================================================")
            self.textarea.insert(END,f"\n Total Amount:\t\tN:{self.subtotal.get()}")
            self.textarea.insert(END,"\nSignature___________\t\t\t\tCust.Signature__________\n")
            self.textarea.insert(END,f"\n Date:{self.date.get()}")
            
            

    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved", f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def clear_bill(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set("")
        j=random.randint(1000,9999)
        self.bill_no.set(str(j))
        self.c_email.set("")
        self.search_Bill.set("")
        self.model.set("")
        self.date.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.subtotal.set(0)
        self.total.set("")
        self.l=[]
        self.welcome()
        self.imei.set("")
        self.desc.set("")



    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_Bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error", "Invalid Bill No.")


    
    def Categories(self,event=""):
        if self.Combo_Category.get()=="IOS":
            self.Combo_SubCategory.config(value=self.SubCatIOS)
            self.Combo_SubCategory.current(0)
        if self.Combo_Category.get()=="Android":
            self.Combo_SubCategory.config(value=self.SubCatAndroid)
            self.Combo_SubCategory.current(0)


    def Product_add(self,event=""):
         if self.Combo_SubCategory.get()=="Iphones":
            self.Combomodel.config(value=self.Iphones)
            self.Combomodel.current(0)
         if self.Combo_SubCategory.get()=="Infinix":
            self.Combomodel.config(value=self.Infinix)
            self.Combomodel.current(0)
         if self.Combo_SubCategory.get()=="Itel":
            self.Combomodel.config(value=self.Itel)
            self.Combomodel.current(0)
         if self.Combo_SubCategory.get()=="Tecno":
            self.Combomodel.config(value=self.Tecno)
            self.Combomodel.current(0)



if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()