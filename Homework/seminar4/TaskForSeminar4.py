# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10 ^ {-1} ≤ d ≤10 ^ {-10}$

def denominator(x): return x*(x+1)*(x+2)


def num_pi(degree):
    d = -degree
    pi1 = 1
    pi2 = 0
    flag = 1
    n = 2
    while (pi1-pi2) >= 10**d:
        if not flag % 2:
            pi2 = pi1 - 4/denominator(n)
        else:
            pi1 = pi2 + 4/denominator(n)
        flag += 1
        n += 2
    return 3+(pi1+pi2)/2


degree = int(input('Enter the required precision: '))

print('pi=', round(num_pi(degree), degree))
