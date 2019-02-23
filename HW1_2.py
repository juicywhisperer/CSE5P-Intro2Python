r = float(input("Enter the radius of a circle (in inches): "))
r_feet = r * 0.0833
pi = 3.1415
print("The diameter of the circle is: ","%.4f" % (r_feet*2),"feet")
print("The perimeter of the circle is: ",round(r_feet*2*pi,4),"feet")
print("The area of the circle is: ",round((pow(r_feet,2))*pi,4),"square feet")