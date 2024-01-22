# This regex library used for split the sentence with substitution method to use "-" symbol.
import re

# This function used the sum of series like user input '5' and this evaluate 2+22+222+2222+22222=24690.
def sum_of_series():
    num=int(input("Enter the value :"))
    f=0
    v=2
    f=v
    t=10
    r=[]
    result=0
    for i in range(num-1):
        r.append(v)
        v1=2
        v=f
        f=(v1*t)+v
        r.append(f)
        t*=10
    rl=list(sorted(set(r)))
    for i in rl:
        result+=i
    print(f"Sum of the given series is : {result}")
#series()

# This function used for sum of the iteration value to sum, eg- previous value add to current value.
def sum_of_iteration():
    it=int(input("How many iteration you want to sum :"))
    previous_number=0
    total_sum = 0
    for current_number in range(it+1):
        sum=current_number + previous_number
        print(f"previous number:{previous_number} current number:{current_number}={sum}")
        total_sum+=sum
        previous_number=current_number
    print(f"Totall sum is:{total_sum}")
#sum_of_iteration()

# This function used for remove the empty string and i use here "if" condition.
def remove_empty_string():
    str_list=['car','lorry','','bus','','auto','tracter','']
    original=[i for i in str_list if i!='']
    print(f"Original list :{str_list}")
    print(f"After remove the empty strings :{original}")
#remove_empty_string()

# This function used for split the given sentence , here i was use regular expression (regx) library and in between two word print the hyphen that's it.
def hyphen():
    word=input("Enter the sentence :")
    result=re.sub(r'\s','-',word )
    print(f"After update :{result}")
#hyphen()

# This function used for given sentence in particular word starting the index position of that word and find it index.
def find_position(string_1,string_2):
    last_position=string_1.rfind(string_2)
    return last_position

# This loop use for display the function choice number to end-user.
print()
show=["1 <-----sum_of_series","2 <-----sum_of_iteration","3 <-----find_position","4 <-----hyphen","5 <-----remove_empty_string"]
for s in show:
    print(s)
print()

# This line get input to user the choice number.
numb=input("Enter the choice number :")

# function calling using with if condition
if numb=="1":
    sum_of_series()

elif numb=="2":
    sum_of_iteration()

elif numb=="3":
    string_1=input("Enter your sentence:")
    string_2=input("which word to find that position in sentence :")    
    result=find_position(string_1,string_2)
    print(f"The last position of {string_2} in {string_1} :{result}")
    
elif numb=="4":
    hyphen()

elif numb=="5":
    remove_empty_string()

else:
    print(f"Kindly please enter valid choice number")
    
    

    
    
    
    

    

    
    
    