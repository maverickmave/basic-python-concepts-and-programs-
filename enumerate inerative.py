student =[("Ali",50),("Sara",40),("Ahmad",60)]
for number , (name, marks) in enumerate (student ,start= 1):
    status = "pass" if marks>=50 else "fail"
    print (number , name , marks, status)