from tkinter import *
from tkinter import ttk
import pymysql
class student:
    def __init__(self,root):
        self.root=root
        self.root.Title=('Student database management system')
        self.root.Geometry=('1300x700')

        title=Label(self.root,text='student database management system',bd='10',relief='groove',font=('times new roman',40,'bold'),bg='yellow',fg='red',)
        title.pack(side='top',fill='x')
#variables
        self.name_var=StringVar()
        self.roll_var=StringVar()
        self.dob_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()





#frame1
        frame_info=Frame(self.root,relief='ridge',bd='50',bg='crimson')
        frame_info.place(x=40,y=80,width=500,height=750)
        m_title=Label(frame_info,text='Manage students',font=('times new roman',20,'bold'))
        m_title.grid(row=1,columnspan=2,pady=20)
        f1_roll=Label(frame_info,text='Roll no.',bd=5,fg='white',bg='crimson',font=('times new roman',15,'bold'))
        f1_roll.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        f1_roll_text=Entry(frame_info,font=('times new roman',15,'bold'),bd=5,relief='groove')
        f1_roll_text.grid(row=2,column=1,padx=15,pady=15,sticky='w')

        f1_name = Label(frame_info, text='NAME', bd=5, fg='white', bg='crimson',
                        font=('times new roman', 15, 'bold'))
        f1_name.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        f1_name_text = Entry(frame_info,textvariable=self.name_var, font=('times new roman', 15, 'bold'), bd=5, relief='groove')
        f1_name_text.grid(row=3, column=1, padx=15, pady=15, sticky='w')

        f1_email = Label(frame_info, text='EMAIL', bd=5, fg='white', bg='crimson',
                         font=('times new roman', 15, 'bold'))
        f1_email.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        f1_email_text = Entry(frame_info, textvariable=self.email_var,font=('times new roman', 15, 'bold'), bd=5, relief='groove')
        f1_email_text.grid(row=4, column=1, padx=15, pady=15, sticky='w')

        f1_gender = Label(frame_info, text='GENDER', bd=5, fg='white', bg='crimson',
                         font=('times new roman', 15, 'bold'))
        f1_gender.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        f1_gender_text = Entry(frame_info,textvariable=self.gender_var, font=('times new roman', 15, 'bold'), bd=5, relief='groove')
        f1_gender_text.grid(row=5, column=1, padx=15, pady=15, sticky='w')
        gender_combo=ttk.Combobox(frame_info,textvariable=self.gender_var,font=('times new roman', 15, 'bold'))
        gender_combo['value']=('male','female')
        gender_combo.grid(row=5,column=1,padx=20,pady=10)

        f1_dob = Label(frame_info, text='DOB', bd=5, fg='white', bg='crimson',
                         font=('times new roman', 15, 'bold'))
        f1_dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        f1_dob_text = Entry(frame_info, textvariable=self.dob_var,font=('times new roman', 15, 'bold'), bd=5, relief='groove')
        f1_dob_text.grid(row=6, column=1, padx=15, pady=15, sticky='w')

        f1_contact = Label(frame_info, text='CONTACT', bd=5, fg='white', bg='crimson',
                         font=('times new roman', 15, 'bold'))
        f1_contact.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        f1_contact_text = Entry(frame_info, textvariable=self.contact_var,font=('times new roman', 15, 'bold'), bd=5, relief='groove')
        f1_contact_text.grid(row=7, column=1, padx=15, pady=15, sticky='w')

        f1_address = Label(frame_info, text='ADDRESS', bd=5, fg='white', bg='crimson',
                           font=('times new roman', 15, 'bold'))
        f1_address.grid(row=8, column=0, pady=10, padx=20, sticky='w')
        self.address_text = Text(frame_info, font=('times new roman', 10, 'bold'), bd=5, relief='groove',width=25,height=4)
        self.address_text.grid(row=8, column=1, padx=10, pady=10, sticky='w')

#button
        btn_frame=Frame(frame_info, relief='ridge', bd=4, bg='crimson')
        btn_frame.place(x=10,y=560,width=400)
        add_btn=Button(btn_frame,command=self.add_stdn,text='add',width=10).grid(row=0,column=0,padx=10,pady=10)
        del_btn = Button(btn_frame, text='delete', width=10).grid(row=0, column=1, padx=10, pady=10)
        upt_btn = Button(btn_frame, text='update', width=10).grid(row=0, column=2, padx=10, pady=10)
        cl_btn = Button(btn_frame, text='clear', width=10).grid(row=0, column=3, padx=10, pady=10)
#2ndframe
        frame_info2 = Frame(self.root, relief='ridge', bd='50', bg='crimson')
        frame_info2.place(x=600, y=100, width=950, height=670, )
        m_title1 = Label(frame_info2, text='SEARCH BY',font=('times new roman', 20, 'bold'))
        m_title1.grid(row=0, columnspan=4, pady=20)

        text_combo = ttk.Combobox(frame_info2, font=('times new roman', 15, 'bold'),state='readonly')
        text_combo['value'] = ('name', 'roll','contact')
        text_combo.grid(row=1, column=0, padx=20, pady=10)
        f1_text = Entry(frame_info2, font=('times new roman', 15, 'bold'), bd=5, relief='groove')
        f1_text.grid(row=1, column=1, padx=15, pady=15, sticky='w')
        search_btn = Button(frame_info2, text='search', width=10).grid(row=1, column=2, padx=10, pady=10)
        showall_btn = Button(frame_info2, text='showall', width=10).grid(row=1, column=3, padx=10, pady=10)

#table view
        table_info = Frame(frame_info2, relief='ridge', bd='50', bg='white')
        table_info.place(x=35, y=135, width=800 ,height=420, )
        x_scroll=Scrollbar(table_info,orient='horizontal')
        y_scroll = Scrollbar(table_info, orient='vertical')

        st=ttk.Treeview(table_info,columns=('NAME','ROLL NO','DOB','GENDER','ADDRESS','EMAIL','CONTACT'),xscrollcommand=x_scroll.set,
                        yscrollcommand=y_scroll.set)
        x_scroll.pack(side='bottom',fill='x')
        y_scroll.pack(side='right', fill='y')
        x_scroll.config(command=st.xview)
        y_scroll.config(command=st.yview)
        st.heading('NAME',text='name')
        st.heading('ROLL NO', text='roll no')
        st.heading('DOB', text='dob')
        st.heading('GENDER', text='GENDER')
        st.heading('ADDRESS', text='address')
        st.heading('EMAIL', text='email')
        st.heading('CONTACT', text='contact')
        st['show']='headings'
        st.column('NAME',width=50)
        st.column('ROLL NO', width=100)
        st.column('GENDER', width=100)
        st.column('DOB', width=100)
        st.column('ADDRESS', width=150)
        st.column('EMAIL', width=100)
        st.column('CONTACT', width=100)


        st.pack(fill='both',expand=1)


    def add_stdn(self):
        conn=pymysql.connect(host='localhost',user='root',password='',database='3306')
        cur=conn.cursor()
        cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)', self.name_var.get(),
        self.roll_var.get(),
        self.dob_var.get(),
        self.gender_var.get(),
        self.address_text.get('1.0',END),
        self.email_var.get(),
        self.contact_var.get())

        conn.commit()
        conn.close()





#button



root=Tk()
ob=student(root)
root.mainloop()