import random
stringlower = ['q', 'w', 'e', 'r',' t' ,'y' ,'u', 'i', 'o', 'p', 'a', 's' ,'d', 'f',' g', 'h' ,'j',' k' ,'l' ,'z', 'x' ,'c' ,'v' ,'b' ,'n',' m ']
stringuppar = ['Q', 'W' ,'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D' ,'F', 'G' ,'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
specifi =[' !', '@', '#', '$' ,'%' ,'^' ,'&' ,'* ']
number = [' 1' ,'2', '3', '4',' 5', '6' ,'7' ,'8' ,'9' ,'0 ']

lenght = int(input("Enter the lenght of Password"))

combbined_list= stringlower +specifi + number + stringuppar
# random.shuffle(combbined_list)

Password  = []
for i  in range (lenght):
    Password = Password + random.choices(combbined_list)

print(" ".join(Password))    
