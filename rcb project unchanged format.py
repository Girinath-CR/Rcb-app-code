from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
import pygame
import sqlite3
w=Tk()
w.title('RCB')
w.geometry('750x750')
w.minsize(750,750)
w.maxsize(750,750)




def player_data():
    w1 = Tk()
    w1.title('Player Details')
    w1.geometry('1000x500')

    #create a database
    con = sqlite3.connect('ipl.db')
    c = con.cursor()
    #create a table
    c.execute(
        'CREATE TABLE if not exists player_details'
        '(Name text,Age integer,ID integer ,Role text,Style text, Runs integer,Wickets integer,Intl_Team text)')



    con.commit()
    con.close()


    def query_database():
        con = sqlite3.connect('ipl.db')
        c = con.cursor()
        c.execute('SELECT rowid, * FROM player_details')
        records=c.fetchall()
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[1], record[2], record[0], record[4], record[5], record[6], record[7], record[8]),
                            tags=('evenrow',))
            else:
                tree.insert(parent='', index='end', iid=count, text='',
                            values=(
                                record[1], record[2], record[0], record[4], record[5], record[6], record[7], record[8]),
                            tags=('oddrow',))
            count += 1

        con.commit()
        con.close()







    style=ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3",rowheight=25,
                    fieldbackground="#D3D3D3", foreground="black")

    style.map('Treeview', background=[('selected', '#347083')])
    # frame for treeview
    tree_frame = Frame(w1)
    tree_frame.pack(pady=10)
    # scrollbar for treeview
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')

    tree.pack()
    tree_scroll.config(command=tree.yview)
    # define columns
    tree['columns'] = ("column1", "column2", "column3", "column4", "column5", "column6", "column7","column8")
    # format columns
    tree.column('#0', width=0, stretch=NO)

    tree.column('column1', anchor=W, width=140)
    tree.column('column2', anchor=W, width=140)
    tree.column('column3', anchor=CENTER, width=140)
    tree.column('column4', anchor=CENTER, width=140)
    tree.column('column5', anchor=CENTER, width=140)
    tree.column('column6', anchor=CENTER, width=140)
    tree.column('column7', anchor=CENTER, width=140)
    tree.column('column8', anchor=CENTER, width=140)

    # Headings-----------------------------------------
    tree.heading("#0", text="", anchor=W)

    tree.heading("column1", text="Name", anchor=W)
    tree.heading("column2", text="Age", anchor=W)
    tree.heading("column3", text="ID", anchor=CENTER)
    tree.heading("column4", text="Role", anchor=CENTER)
    tree.heading("column5", text="Style", anchor=CENTER)
    tree.heading("column6", text="Runs", anchor=CENTER)
    tree.heading("column7", text="Wickets", anchor=CENTER)
    tree.heading("column8", text="Intl_Team", anchor=CENTER)

    tree.tag_configure('oddrow', background='misty rose')
    tree.tag_configure('evenrow', background='floral white')



    data_frame=LabelFrame(w1,text='record')
    data_frame.pack(fill='x',expand='yes',padx=20)

    name_lbl=Label(data_frame,text='Name',)
    name_lbl.grid(row=0,column=0,padx=10,pady=10)
    name_entry=Entry(data_frame)
    name_entry.grid(row=0,column=1,padx=10,pady=10)

    age_lbl = Label(data_frame, text='Age', )
    age_lbl.grid(row=0, column=2, padx=10, pady=10)
    age_entry = Entry(data_frame)
    age_entry.grid(row=0, column=3, padx=10, pady=10)

    id_lbl = Label(data_frame, text='ID', )
    id_lbl.grid(row=0, column=4, padx=10, pady=10)
    id_entry = Entry(data_frame)
    id_entry.grid(row=0, column=5, padx=10, pady=10)

    role_lbl = Label(data_frame, text='Role', )
    role_lbl.grid(row=0, column=6, padx=10, pady=10)
    role_entry = Entry(data_frame)
    role_entry.grid(row=0, column=7, padx=10, pady=10)


    style_lbl = Label(data_frame, text='Style', )
    style_lbl.grid(row=1, column=0, padx=10, pady=10)
    style_entry = Entry(data_frame)
    style_entry.grid(row=1, column=1, padx=10, pady=10)

    runs_lbl = Label(data_frame, text='Runs', )
    runs_lbl.grid(row=1, column=2, padx=10, pady=10)
    runs_entry = Entry(data_frame)
    runs_entry.grid(row=1, column=3, padx=10, pady=10)

    wickets_lbl = Label(data_frame, text='Wickets', )
    wickets_lbl.grid(row=1, column=4, padx=10, pady=10)
    wickets_entry = Entry(data_frame)
    wickets_entry.grid(row=1, column=5, padx=10, pady=10)

    team_lbl = Label(data_frame, text='Intl_Team', )
    team_lbl.grid(row=1, column=6, padx=10, pady=10)
    team_entry = Entry(data_frame)
    team_entry.grid(row=1, column=7, padx=10, pady=10)

    #functions
    def add_player():
        con = sqlite3.connect('ipl.db')
        c = con.cursor()
        c.execute('INSERT INTO player_details VALUES(:Name,:Age,:ID,:Role,:Style,:Runs,:Wickets,:Intl_Team)',
                  {

                      'Name': name_entry.get(),
                      'Age': age_entry.get(),
                      'ID':id_entry.get(),
                      'Role': role_entry.get(),
                      'Style': style_entry.get(),
                      'Runs': runs_entry.get(),
                      'Wickets': wickets_entry.get(),
                      'Intl_Team': team_entry.get()
                  }

                  )


        con.commit()
        con.close()

        #clear entry boxes
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        age_entry.delete(0, END)
        id_entry.delete(0, END)
        role_entry.delete(0, END)
        style_entry.delete(0, END)
        runs_entry.delete(0, END)
        wickets_entry.delete(0, END)
        team_entry.delete(0, END)

        #clear the treeview table
        tree.delete(*tree.get_children())
        query_database()






    def remove_one():
        x=tree.selection()[0]
        tree.delete(x)

        con = sqlite3.connect('ipl.db')
        c = con.cursor()
        c.execute('DELETE from player_details WHERE  oid='+id_entry.get())

        con.commit()
        con.close()

        clear_entries()



    def remove_many():
        x=tree.selection()
        for record in x:
            tree.delete(record)

    def remove_all():
        for record in tree.get_children():
            tree.delete(record)

    def update_player():
        selected=tree.focus()
        tree.item(selected,text='',values=(name_entry.get(),age_entry.get(),id_entry.get(),role_entry.get(),style_entry.get(),
                                           runs_entry.get(),wickets_entry.get(),team_entry.get(),))

        con = sqlite3.connect('ipl.db')
        c = con.cursor()
        c.execute("""UPDATE player_details SET
        
                        Name=:Name,
                        Age=:age,
                        Role=:Role,
                        Style=:Style,
                        Runs=:Runs,
                        Wickets=:Wickets,
                        Intl_Team=:Intl_Team
                        
                        WHERE oid=:oid""",
                  {
                      'Name': name_entry.get(),
                      'age':age_entry.get(),
                      'Role': role_entry.get(),
                      'Style': style_entry.get(),
                      'Runs': runs_entry.get(),
                      'Wickets': wickets_entry.get(),
                      'Intl_Team': team_entry.get(),
                      'oid':id_entry.get(),

                  } )

        con.commit()
        con.close()


    def clear_entries():
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        id_entry.delete(0, END)
        role_entry.delete(0, END)
        style_entry.delete(0, END)
        runs_entry.delete(0, END)
        wickets_entry.delete(0, END)
        team_entry.delete(0, END)







    def select_player(e):
        name_entry.delete(0,END)
        age_entry.delete(0,END)
        id_entry.delete(0, END)
        role_entry.delete(0, END)
        style_entry.delete(0, END)
        runs_entry.delete(0, END)
        wickets_entry.delete(0, END)
        team_entry.delete(0, END)

        #grab record number
        selected=tree.focus()
        #grab record values
        values=tree.item(selected,'values')
        #output entry boxes
        name_entry.insert(0, values[0])
        age_entry.insert(0, values[1])
        id_entry.insert(0, values[2])
        role_entry.insert(0, values[3])
        style_entry.insert(0, values[4])
        runs_entry.insert(0, values[5])
        wickets_entry.insert(0, values[6])
        team_entry.insert(0, values[7])

    #add button
    btn_frame=LabelFrame(w1,text='Buttons')
    btn_frame.pack(fill='x',expand='yes',padx=20)

    update_btn=Button(btn_frame,text='Update',command=update_player)
    update_btn.grid(row=0,column=0,padx=10,pady=10)

    add_btn = Button(btn_frame, text='Add',command=add_player)
    add_btn.grid(row=0, column=1, padx=10, pady=10)

    removeall_btn = Button(btn_frame, text='Remove_all',command=remove_all)
    removeall_btn.grid(row=0, column=2, padx=10, pady=10)

    removeone_btn = Button(btn_frame, text='Remove_one',command=remove_one)
    removeone_btn.grid(row=0, column=3, padx=10, pady=10)

    removemany_btn = Button(btn_frame, text='Remove_many',command=remove_many)
    removemany_btn.grid(row=0, column=4, padx=10, pady=10)

    select_btn = Button(btn_frame, text='Clear Entries',command=clear_entries)
    select_btn.grid(row=0, column=5, padx=10, pady=10)

    #bind the treeview
    tree.bind('<ButtonRelease-1>',select_player)

    query_database()











def music():
    root = Tk()
    root.geometry('200x200')
    root.minsize(200, 200)
    root.maxsize(200, 200)
    # bg_image=ImageTk.PhotoImage(Image.open("H:/python tkinter project/cricket rcb/EQtmN0fUcAAnCyu.png"))
    # label1=Label(master=root,image=bg_image)
    # label1.pack()

    pygame.mixer.init()

    def play_music():
        pygame.mixer.music.load(
            'H:/python tkinter project/cricket rcb/music/Official RCB Anthem for Dream11 IPL 2020.mp3')
        pygame.mixer.music.play()

    def stop_music():
        pygame.mixer.music.stop()
    button1 = Button(root, text='sound on', font=("Franklin Gothic Demi Cond", 14), bg='gray5', fg='pale goldenrod',
                         command=play_music)
    button1.place(x=70, y=70)
    button2 = Button(root, text='sound off', font=("Franklin Gothic Demi Cond", 14), bg='gray5',
                         fg='pale goldenrod', command=stop_music)
    button2.place(x=69, y=125)

bg_image=ImageTk.PhotoImage(Image.open("H:/python tkinter project/cricket rcb/images/EQtmN0fUcAAnCyu.png"))
label1=Label(w,image=bg_image)
label1.place(x=0,y=0,width=750,height=750)
button1=Button(w,text='Player Data',font=("Franklin Gothic Demi Cond", 14),bg='gray5',fg='pale goldenrod',command=player_data)
button1.place(x=325,y=310)
button2=Button(w,text='Theme music',font=("Franklin Gothic Demi Cond", 14),bg='gray5',fg='pale goldenrod',command=music)
button2.place(x=315,y=375)
button3=Button(w,text='Exit',font=("Franklin Gothic Demi Cond", 14),bg='gray5',fg='pale goldenrod',command=w.destroy)
button3.place(x=350,y=430)
frame1=Frame(w)
frame1.place(x=10,y=50,width=133,height=200)
frame2=Frame(w)
frame2.place(x=10,y=400,width=133,height=268)

image1=ImageTk.PhotoImage(Image.open("H:/python tkinter project/cricket rcb/images/5848881.png"))
image2=ImageTk.PhotoImage(Image.open("H:/python tkinter project/cricket rcb/images/virat bg2.png"))

label_abd=Label(frame1,image=image1)
label_abd.pack( )
label_king=Label(frame2,image=image2)
label_king.pack( )




w.mainloop()


