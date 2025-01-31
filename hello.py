def f(x, p, num):
 
    return pow(x, p) - num
 
# calculating the value
# of the differential of the function
def f_prime(x, p):
 
    return p * pow(x, p - 1)
 
# The function that returns
# the root of given number
def root(num, p):
 
    # Defining range
    # on which answer can be found
    left = -num
    right = num
 
    x = 0
    while (True):
 
        # finding mid value
        x = (left + right) / 2.0
        value = f(x, p, num)
        prime = f_prime(x, p)
        if (value * prime <= 0):
            left = x
        else:
            right = x
        if (value < 0.000001 and value >= 0):
            return x
 
# Driver code
if __name__ == "__main__":
 
    P = 1234321
    N = 2
 
    ans = root(P, N)
    print(ans)