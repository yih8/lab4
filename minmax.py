from numbers import Integral


def minmax(data):

    n=len(data)
    

    maximum = data[0]
    minimum = data[0]
    for i in range (0,n):
        if maximum <= data[i]:
            maximum = data[i] 
            i+=1
        else:
            i+=1
    for i in range (0,n):
        if maximum >= data[i] :
            minimum = data[i] 
            i+=1
        else:
            i+=1
    return ("max=",maximum,"; min=",minimum)  

x = str(input("the input data is \n"))
print(minmax(x))


