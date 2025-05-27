#Example of procedural programming
def calculate_area(lenght,width):
    return lenght*width

def calcualte_perimeter(length,width):
    return  2*(length+width)

length=5
width=3

area=calculate_area(length,width)
perimetri=calcualte_perimeter(length,width)

print(f"Area {area}")
print(f"perimetri: {perimetri}")