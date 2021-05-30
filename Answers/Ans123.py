#answer2
b = {"1":"ravi","2":"ravi","3":"shyam","4":"pnkj","5":"shyam","6":"pnkj",
"7":"shyam","8":"ravi","9":"pnkj","10":"ravi"}
new = {}
for item in b.values():
	if item in new:
		new[item] += 1
	else:
		new[item] = 1
print(new)

#####output
"""
{'ravi': 4, 'shyam': 3, 'pnkj': 3}
"""


#answer1
l1 = 4,5,6,7,4,6,2
print(list(l1))  #output is [4, 5, 6, 7, 4, 6, 2]
def list_sum(list1):
    total_sum = 0
    for i in range(0,len(list1)):
        total_sum = total_sum + list1[i]
    return total_sum
print("Total sum of list is",list_sum(l1))  # output is Total sum of list is 34


#answer3
def maxconseqtive(list, n):
    count = 0 
    result = 0 
  
    for i in range(0, n):
        if (list[i] == 0):
            count = 0
        else:
            count+= 1 
            result = max(result, count) 
    return result 

l3= [0,0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1]
b = len(l3)
print(maxconseqtive(l3,b))
        
    