import math
def circle(rad):
  area= round( math.pi*rad**2,2)
  circumference=round(2*math.pi*rad,2)

  
  return area,circumference



a,c=circle(7)
print("area :",a,"cicumference : ",c)
  




