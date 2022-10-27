import random

qt = int(input('Insira quantos digitos a senha deve ter: '))

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nmbrs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb  = ['!', '?', '@', '#', '$', '%', '&', '*', '-', '+', '=', '(', ')', '[', ']'] 

all = lower + upper + nmbrs + symb
random.shuffle(all)

password = []

for i in range(qt):
    password.append(random.choice(all))
    random.shuffle(password)


print(''.join(password)) 
