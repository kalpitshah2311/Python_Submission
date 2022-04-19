class Rectangle:
    x_corner = 0
    y_corner = 0
    def show(self):
        print(" X : "+str(self.x_corner))
        print(" y : " + str(self.y_corner))

def mov_rectangle(r,x,y):
    r.x_corner += x
    r.y_corner += y

re = Rectangle()
re.show()
mov_rectangle(re,100,20)
print("after moving")

re.show()
