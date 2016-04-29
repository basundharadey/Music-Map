from Tkinter import *
import sqlite3

def save():
##Registartion page user new user submit button
  global a,root,store1,store2,var1,var2,var3,var4,var5,var6,var7,var8
  store1=[]
  store2=[]
  store3=[]
  store4=[]
  temp1= a.get()
  temp2= b.get()
  temp3= c.get()
  temp4= d.get()
  temp5= e.get()
  temp6= str(f.get())
  temp7= g.get()
  temp8= h.get()
  temp9= k.get()
  con = sqlite3.connect("test.db")
  cur = con.cursor()
  cur.execute("insert into user_entry values(?,?,?,?,?,?,?,?,?)",(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,))
  con.commit()

  
  root1=Tk()
  root1['bg']='yellow' 
  root1.title(" Song Recomendations ")

  Label(root1,text="Welcome"+' '+' '+ temp7,bg='yellow',fg='red').grid(column=3,row=1)

##Age Recomendation
  var0 = int(temp3)
  var1 = 17
  var2 = 21
  var3 = 28
  var4 = 34
  var5 = 40
  var6 = 50
  var7 = 65
  var8 = 100
  
  Label(root1,text="Age Preference",bg='yellow',fg='blue',bd=5).grid(column=3,row=2)
  
  if var0 <= var2 and var0 >= var1 :
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (17,21):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            

      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1
          
  elif var0 <= var3 and var0 >= var2 :
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (21,28):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            

      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1

  elif var0 <= var4 and var0 >= var3 :
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (28,34):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            

      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1

  elif var0 <= var5 and var0 >= var4 :
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (34,40):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            

      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1

  elif var0 <= var6 and var0 >= var5 :
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (40,50):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            

      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1

  elif var0 <= var7 and var0 >= var6 :
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (50,65):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            

      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1

  elif var0 >= var7 and var0 <= var8:
      
      row=cur.execute("select * from user_entry")
      for i in row:
           if i[2] in range (65,100):
              store1.append(i[6])   
                                 
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store1:
              store2.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
            
      r = 3
      for i in store2:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=r)
          r=r+1
  else:
          Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=3)
        
  

##Regional Preference Recomendation
  Label(root1,text="Regional Preference",bg='yellow',fg='blue').grid(column=3,row=5)
  
  asia=['China', 'Japan', 'Korea', 'India', 'Srilanka', 'Pakisthan']
  africa=['Kenia', 'Zimbaboe', 'Nygeria', 'South Africa']
  europe=['Hungary', 'Poland', 'United Kingdom', 'France']
  america=['Brazil', 'United States', 'Canada', 'Haitai']
  osiania=['Austrelia', 'New Zealand']

  if temp4 in asia:
      row=cur.execute("select * from user_entry")
      for i in row:
          if i[3] in asia:
              store3.append(i[6])
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store3:
              store4.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=6)

      x = 6
      for i in store4:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=x)
          x=x+1

  elif temp4 in africa:
      row=cur.execute("select * from user_entry")
      for i in row:
          if i[3] in africa:
              store3.append(i[6])
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store3:
              store4.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=6)

      x = 6
      for i in store4:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=x)
          x=x+1

  elif temp4 in europe:
      row=cur.execute("select * from user_entry")
      for i in row:
          if i[3] in europe:
              store3.append(i[6])
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store3:
              store4.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=6)

      x = 6
      for i in store4:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=x)
          x=x+1

  elif temp4 in america:
      row=cur.execute("select * from user_entry")
      for i in row:
          if i[3] in america:
              store3.append(i[6])
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store3:
              store4.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=6)

      x = 6
      for i in store4:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=x)
          x=x+1

  elif temp4 in osiania:
      row=cur.execute("select * from user_entry")
      for i in row:
          if i[3] in osiania:
              store3.append(i[6])
      row1=cur.execute("select * from user_pref")
      for j in row1:
           if j[0] in store3:
              store4.append(j[1])
           else:
              Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=6)

      x = 6
      for i in store4:
          Label(root1,text="Here your song suggestion : "+ i,bg='yellow').grid(column=3,row=x)
          x=x+1

  else:
           Label(root1,text="Sorry,No suggestions",bg='yellow').grid(column=3,row=6)

     

  root1.mainloop()

                  
def main():
##Registration page new user
    global root,a,b,c,d,e,f,g,h,k
    root= Tk()
    root['bg']='yellow' 
    root.title(" Registration ")
    Label(root,text="User Registration",bg='yellow',fg='red',font=("Helvetica",16)).grid(row=0,column=2)
    Label(root,text="First name :",bg='yellow').grid(row=1,column=1)
    a=Entry(root)
    a.grid(row=1,column=2)
    Label(root,text="Last name :",bg='yellow').grid(row=2,column=1)
    b=Entry(root)
    b.grid(row=2,column=2)
    Label(root,text="Age :",bg='yellow').grid(row=3,column=1)
    c=Entry(root)
    c.grid(row=3,column=2)
    Label(root,text="Country :",bg='yellow').grid(row=4,column=1)
    d = StringVar(root)
    d.set('--Select Country--')
    choices = ['China', 'Japan', 'Korea', 'India', 'Srilanka', 'Pakisthan', 'Kenia', 'Zimbaboe', 'Nygeria', 'South Africa', 'Hungary', 'Poland', 'United Kingdom', 'France', 'Brazil', 'United States', 'Canada', 'Haitai', 'Austrelia', 'New Zealand']
    option = OptionMenu(root, d, *choices)
    option.grid(row = 4, column =2)
    Label(root,text="Language :",bg='yellow').grid(row=5,column=1)
    e = StringVar(root)
    e.set('--Select Language--')
    choices = ['Bengali', 'English', 'Hindi', 'French', 'Chinese']
    option = OptionMenu(root, e, *choices)
    option.grid(row = 5, column =2)
    Label(root,text="Sex :",bg='yellow').grid(row=6,column=1)
    f = IntVar()
    R1 = Radiobutton(root, text="Male", variable=f, value=1, bg='yellow').grid(row=6,column=2)
    R2 = Radiobutton(root, text="Female", variable=f, value=2, bg='yellow').grid(row=7,column=2)
    Label(root,text="ID :",bg='yellow').grid(row=8,column=1)
    g=Entry(root)
    g.grid(row=8,column=2)
    Label(root,text="Password :",bg='yellow').grid(row=9,column=1)
    h=Entry(root)
    h.grid(row=9,column=2)
    Label(root,text="Confirm Password :",bg='yellow').grid(row=10,column=1)
    k=Entry(root)
    k.grid(row=10,column=2)
    Button(root,text="submit",command=save).grid(row=11,column=2)
    Button(root,text="reset",command=clear).grid(row=11,column=1)
    root.mainloop()
    
def clear():
##Registration page reset button
    global root
    root.destroy()
    main()
    

main()
   

