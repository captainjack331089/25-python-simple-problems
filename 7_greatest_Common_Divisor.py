"""
We often say that the tech industry isn’t nearly as math-heavy as outsiders tend to think it is. Part of that is because most of the heavy computational lifting is done for you by machines. Still, you DO need to tell machines what to do and how to do before letting them loose. (This sounds like the start of a classic “robots take over the world” film…).Python scripts like this greatest common divisor script are perfect examples of how—once you use Python to give machines a clear set of instructions—they’ll spit out the computational data you’re looking for till the end of time.
"""
# Create a divisor to compute the greatest common divisor between two numbers

def gcd2(a,b):
    a,b = (a,b) if a >= b else (b,a)
    while b:
        a,b = b, a%b
    return a

# Create a divisor to compute the greates common divisor between n numbers

def gcd(s):
    if len(s) == 1:
        return s[0]
    if len(s)  == 2:
        return gcd2(s[0],s[1])
    else:
        cd = []
        for i in range(len(s)-1):
            cd.append(gcd2(s[i],s[i+1]))
        cd = list(set(cd))
        return gcd(cd)




if __name__ == '__main__':
    a = 32
    b = 24
    c = 72
    print('{}和{}的最大公约数为：{}'.format(a,b,gcd2(a,b)))
    s = [a,b,c]
    print('{},{}和{}的最大公约数为：{}'.format(a,b,c,gcd(s)))