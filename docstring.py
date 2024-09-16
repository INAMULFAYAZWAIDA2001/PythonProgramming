def square(n):
    print(n**2)
    '''Takes in a number n, returns the square of n'''
square(12)

# '''Takes in a number n, returns the 
#square of n''' is a docstring which 
#will not appear in output

def cube(m):
    '''Takes in a number n, returns the cube of n'''
    return m**3
print(cube.__doc__)