''' These commands are used to average a list of five numbers!'''

list1 = []
c = 1
for i in range(5):
    n = float(input('Enter a Number_{}: '.format(c)))
    c+=1
    list1.append(n)
print('your Average: ',sum(list1)/len(list1))
