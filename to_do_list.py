def menue2():
    print("""
          ///The operations///
1.Add Task
2.Mark task has done
3.Delete tasks
4.View tasks
5.Exit
""")
def tasks():
    print("""
        ///The tasks///
1.buy Grocerries
2.finish home work
3.call mom
4.go for run
""")
Menue={
    1:"Add Task",
    2:"Mark task has done",
    3:"Delete tasks",
    4:"View tasks",
    5:"Exit"
}
tasks2={
    1:"buy Grocerries",
    2:"finish home work",
    3:"call mom",
    4:"go for run"
    }

marked=[]
added=[]
Deleted=[]

menue2()
tasks()
while True:
    try:
        user=int(input("\nWhat operation you want to do: "))
        
        if user==4:
            print(f"you selected{Menue[4]}")
            for i in tasks2:
                print(f"{i}.{tasks2[i]}".strip())
        
        pass
        if user==1:
            print(f"you selected {Menue[1]}")
            user2=int(input("what task you want to do: "))
            if user2 in Deleted:
                print("its not avilable")
            elif user2 in added:
                print("Already it has been selected")
            else:
                print(f"your task is,{tasks2[user2]}".strip())
                added.append(user2)
            
        pass
        if user==3:
            print(Menue[3])
            user4=int(input("what task you want to delete: "))
            if user4 in marked:
                Deleted.append(user4)
                del(tasks2[user4])
            else:
                print("if you want to delete a task\nmarked the tasks you have done first".strip())
        
        pass
        if user==2:
            print(f"you selected to {Menue[2]}")
            user3=int(input("what task has done by you: "))
            if user3 in added:
                marked.append(user3)
            else:
                print("if you want to mark the task\nadd the task first".strip())
        
        pass
        if user==5:
            y=input("do you want to exit(Y/N): ")
            if y=="Y":
                break
            elif y=="N":
                continue
    except ValueError:
        print("Enter integer values only")
    
       


