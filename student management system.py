from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        
        #FIRST IMAGE

        img=Image.open(r"C:\Users\mantan kumar\OneDrive\Desktop\face recognition\student.jpeg")
                       




        #2ND IMAGE


        img1=Image.open(r"C:\Users\mantan kumar\OneDrive\Desktop\face recognition\download.jpeg")
        img1=img1.resize((510,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #3RD IMAGE:

        img2=Image.open(r"C:\Users\mantan kumar\OneDrive\Desktop\face recognition\download.jpeg")
        img2=img2.resize((500,130),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

         #BACKGROUND IMAGE

        img3=Image.open(r"C:\Users\mantan kumar\OneDrive\Desktop\face recognition\bg.jpg")
        img3=img3.resize((1530,710),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left lable frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="student details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        
        img_left=Image.open(r"C:\Users\mantan kumar\OneDrive\Desktop\face recognition\student.jpeg")
        img_left=img_left.resize((720,130),Image.ADAPTIVE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course information

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white" ,relief=RIDGE,text="current course information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=7320,height=125)
         
         #departmant

        dep_label=Label(current_course_frame,text="Department",font=("time new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly")
        dep_combo["values"]=("select department","Computer","IT","Civil","mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course 

        Course_label=Label(current_course_frame,text="Course",font=("time new roman",13,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        Course_combo=ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly", width=20)
        Course_combo["values"]=("select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year


        year_label=Label(current_course_frame,text="Course",font=("time new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly", width=20)
        year_combo["values"]=("select year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        


        semester_label=Label(current_course_frame,text="Course",font=("time new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly", width=20)
        semester_combo["values"]=("select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class stusent information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white" ,relief=RIDGE,text="Class Student information",font=("time new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=260,width=720,height=400)

        #student id
        StudentId_label=Label(Class_Student_frame,text="StudentID:",font=("time new roman",13,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)

        StudentID_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #STUDENT name
        StudentName_label=Label(Class_Student_frame,text="Student Name:",font=("time new roman",13,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10, pady=5,sticky=W)

        StudentName_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        
        class_div_label=Label(Class_Student_frame,text="Class Division:",font=("time new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10, pady=5,sticky=W)

        class_div_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no

        roll_no_label=Label(Class_Student_frame,text="Roll no:",font=("time new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10, pady=5,sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        
        gender_label=Label(Class_Student_frame,text="Gender:",font=("time new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10, pady=5,sticky=W)

        gender_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date of birth

        
        dob_label=Label(Class_Student_frame,text="DOB:",font=("time new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10, pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #EMAIL ID

        
        
        email_label=Label(Class_Student_frame,text="Email:",font=("time new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10, pady=5,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no

        
        
        phone_label=Label(Class_Student_frame,text="Phone No:",font=("time new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10, pady=5,sticky=W)

        phone_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address

        
        
        address_label=Label(Class_Student_frame,text="Address:",font=("time new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10, pady=5,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name

        
        
        teacher_label=Label(Class_Student_frame,text="Teacher Name:",font=("time new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10, pady=5,sticky=W)

        teacher_entry=ttk.Entry(Class_Student_frame,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio buttons

        Radiobutton1=ttk.Radiobutton(Class_Student_frame,text="take photo sample",value="yes")
        Radiobutton1.grid(row=6,column=0)

        #radio no:2

        Radiobutton2=ttk.Radiobutton(Class_Student_frame,text="No photo sample",value="yes")
        Radiobutton2.grid(row=6,column=1)

        # buttons frame

        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        #save button

        save_btn=Button(btn_frame,text="save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

       
        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text=" Update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

           
        
          #right lable frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="student details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

       
        img_right=Image.open(r"C:\Users\mantan kumar\OneDrive\Desktop\face recognition\bg1.jpg")
        img_right=img_right.resize((720,130),Image.ADAPTIVE)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        ##=== serach system=========

        search_frame=LabelFrame(Right_frame,bd=2,bg="white" ,relief=RIDGE,text="Search System",font=("time new roman",15,"bold"))
        search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(search_frame,text="Search By:",font=("time new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("time new roman",13,"bold"),state="readonly", width=15)
        search_combo["values"]=("select ","Roll No:","Phone No:")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
                
       
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="ShowAll",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #=============table frame=======

        table_frame=Frame(Right_frame,bd=2,bg="white" ,relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        

        self.student_table.pack(fill=BOTH,expand=1)  

        
                              
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()