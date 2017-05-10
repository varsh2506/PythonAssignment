'''This code displays the histogram for a given data set according the user's choice of class size.
First, the hist_data list is updated with each of its elements being a list of elements in a particular class interval.
The histogram is then displayed using the hist_data list.'''

data = [3, 4, 3, 4, 5, 6, 2, 1, 5, 4, 6, 7, 8, 9, 10, 1, 20, 6, 8, 9]
hist_data = [] #Stores the values in each range as a list of lists
bin_size = int(raw_input("Enter width of each interval: "))
l = min(data)
u = bin_size+l-1
ct = 0 
data.sort()

il = [] #Inner list which contains the values in a specific range
while ct<len(data):   
    if data[ct]>=l and data[ct]<=u:
        il.append(data[ct])
        ct+=1
    else:
        l=u+1
        u=l+bin_size-1
        hist_data.append(il)
        il = []
    if ct==len(data):
        hist_data.append(il)

l = min(data)
u = bin_size+l-1

#Printing the histogram using the hist_data list
for j in hist_data:
    print str(l)+'-'+str(u),
    print '-'*len(j)
    l=u+1
    u=bin_size+l-1

    
        
    
    
