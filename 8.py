class Parent():
          
    def show(self):
        print("Inside Parent1")
          

          
          

class Child(Parent):
          
 
    def show(self):
        print("Inside Child")
     
        

obj = Child()
  
obj.show()
