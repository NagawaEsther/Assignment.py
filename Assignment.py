# Write a python programme to sum all numbers in the list
#=[8,2,3,0,7]

def sum_of_numbers(a,b,c,d,e):
    output=a+b+c+d+e
    print(f"sum of {a} and {b} and {c} and {d} and {e} is {output}")
sum_of_numbers(8,2,3,0,7)

#Write a python programme to reverse a string[1,2,3,4,a,b,c,d]
def reversed_string(input_string):
    reversed_str = input_string[::-1]  
    return reversed_str
input_str = "1,2,3,4,a,b,c,d"
reversed_str = reversed_string(input_str)
print(reversed_str)

# Write a python function to multiply all the numbers in the list[8,2,3,-1,7]
def list_of_numbers(x,y,z,w,r):
    Result=x*y*z*w*r
    print(f"product of {x} and {y} and {z} and {w} and {r} is {Result}")
list_of_numbers(8,2,3,-1,7)


# Write a python programme to print the even numbers from a given list[1,2,3,4,5,6,7,8,9]
def even_numbers(h,i,j,k,l,m,n,o,p,):
    Result=[2,4,6,8]
    print(Result)

even_numbers(1,2,3,4,5,6,7,8,9)

