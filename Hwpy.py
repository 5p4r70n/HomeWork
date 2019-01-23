def grdcal(x):
    if x>=90:
        return("A")
    elif x>=80 and x<90:
        return("B")
    elif x>=70 and x<80:
        return("c")
    elif x>=60 and x<70:
        return("d")
    elif x>=50 and x<60:
        return("e")
    else : 
      return ("Failed")
#sa=[0,0,0,0,0,0]
#sb=[0,0,0,0,0,0]
z1=0
for i in range(5):
    z=int(input("What is yoursubjet mark"))
    z1=z1+z
x=z1/5
grade = grdcal(x)
print("your grade is",grade)