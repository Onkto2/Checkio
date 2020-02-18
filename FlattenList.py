#def flat_list(array):

output=[]
l = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
def RemoveNesting(l):
        
    for i in l: 
        if type(i) == list: 
            RemoveNesting(i) 
        else: 
            output.append(i)
    
#l=array
RemoveNesting(l)
print("the orignal",output)

array = output

    

    #return array
print("Done")




