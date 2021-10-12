# 1
def capital_indexes(parameter):
    lista = []
    nova = list(parameter.strip(" "))
    
    for index, height in enumerate(nova):
        if height.isupper() == True:
            lista.append(index)
    return lista
    
capital_indexes("TEsT")

#2
def mid (palavra):
    lista = list(palavra.strip(" "))
    num_itens = len(lista)
    
    if (num_itens%2 != 0):
        indice = ((num_itens - 1)/2) 
        return lista[int(indice)] 
    else:
        return ''
    
mid("abc")

#3
def online_count(parameter):
    count_online = 0
    for i in parameter.values():
        # var = statuses
        if ( i == 'online'):
            count_online +=1
    return count_online
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

#4
import random
def random_number():
    random_num = random.randint(1,100)
    
    return random_num

random_number()

#5
def only_ints(par1, par2):
    if (isinstance(par1, bool) or isinstance(par2, bool)):
        return False
    elif (isinstance(par1, int) and isinstance(par2, int)):
        return True
    else:
        return False

only_ints(1, 2)

#6
def double_letters(parameter):
    lista = list(parameter.strip(" "))
    
    for index, height in enumerate(lista):
        print (lista[index])
        if (lista[index] == lista[index-1]):
            return True
    return False
    
    
    
double_letters('kassadin')

#7
def add_dots(parameter):
    mySeparator = "."
    x = mySeparator.join(parameter)
    return x
    
def remove_dots(parameter):
   return parameter.replace(".", "")
    
remove_dots(add_dots('test'))

#8
def count(parameter):
    var = parameter.count("-")
    return var + 1
    
count("ho-tel")

#9
def is_anagram(param1, param2):
    lista1 = list(param1.strip(" "))
    lista2 = list(param2.strip(" "))
    lista1.sort()
    lista2.sort()
    if (lista1 == lista2):
        return True
    return False

is_anagram("casa","saca")

#10
def flatten(parameter):
    lista = []
    for x, tam in enumerate(parameter):
        for y, tam2 in enumerate(tam):
            lista.append(parameter[x][y])
    
    return lista
    
flatten([[1, 2],[3,4]])

#11
def largest_difference(parameter):
    parameter.sort()

    first = parameter.pop(0)
    last = parameter.pop()
    print(first)
    print(last)
    
    return (last-first)
    
largest_difference([1, 20, 3,4])

#12
def div_3(parameter):
    if (parameter%3 != 0):
        return False
    return True
    
div_3(6)

#13
dic = {'A': 0, 'B': 1, 'C': 2}

def get_row_col(parameter):
    lista = list(parameter.strip(" "))
    column = dic.get(lista[0])
    row = int(lista[1])
    return (row-1,column)

get_row_col("A3")

#14
def palindrome(parameter):
    reverse=''.join(reversed(parameter))
    if (parameter == reverse):
        return True
    return False
        
palindrome("natan")

#15
def up_down(parameter):
    down = int(parameter) - 1
    up = int(parameter) + 1
    return (down, up)
    
up_down(5)

#16
def consecutive_zeros(parameter):
    zerocountermax = 0
    zerocounter = 0
    lista = list(parameter.strip(" "))
    
    for index, height in enumerate(lista):
        if int(lista[index]) == 0:
            zerocounter += 1
            if zerocounter > zerocountermax:
                zerocountermax = zerocounter
        elif int(lista[index]) == 1:
            if zerocounter > zerocountermax:
                zerocountermax = zerocounter    
            zerocounter = 0
    return zerocountermax

#17
def all_equal(parameter):
    for index, height in enumerate(parameter):
        if parameter[index] != parameter[index-1]:
            return False
    return True

all_equal([1,1,1])

#18
def triple_and(p1, p2, p3):
    if p1 == True and p2 == True and p3 == True: 
        return True
    return False
    
triple_and(True, False, True)

#19
def convert(parameter): return list(map(str,parameter))
convert([1, 2, 3])

#20
def zap(a, b):
    lista = []
    
    for index, height in enumerate(a):
        lista.append((a[index],b[index]))
    
    return lista

print(zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
))

#21
paren = "("
tese = ")"

def validate(code):
    if "def" not in code:
        return "missing def"
    elif ":" not in code:
        return "missing :"
    elif "(" not in code:
        return "missing paren"
    elif ")" not in code:
        return "missing paren"
    elif (paren + tese) in code:
        return "missing param"
    elif "    " not in code:
        return "missing indent"
    elif "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"
    return True

#22
def list_xor(n, list1, list2):
    if n in list1 and n not in list2:
        return True
    elif n in list2 and n not in list1:
        return True
    elif n in list1 and n in list2:
        return False
    return False
    
list_xor(1, [1, 2, 3], [4, 5, 6])

#23
def param_count(*arg):
    cont_var = 0
    for i in arg:
        cont_var +=1
    return cont_var
    
param_count()

#24
def format_number(number):
    string = str(number)
    tamanho_string = len(string)
    lista = list(string.strip(" "))
    var=3
    i=0
    
    while var < tamanho_string:
        lista.insert(-(var+i), ",")
        var +=3
        i+=1
        
    print((''.join(map(str, lista))))
    return (''.join(map(str, lista)))