from random import choice
n=8
# Initialize all spin up case
spins=[[1 for i in range(n)] for j in range(n)]
#calculate the system energy
energy=0
for i in range (n):
    for j in range(n):
        energy-=(spins[i][j]*(spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                            spins[(i+1)%n][j]+spins[(i+n-1)%n][j]))
print("<E>=%4.2f"%(float(energy)/(n*n)))
spins=[[choice((-1,1)) for x in range(n)] for y in range(n)]
#calculate the system energy
energy=0
for i in range(n):
    for j in range(n):
        energy-=(spins[i][j]*(spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                            spins[(i+1)%n][j]+spins[(i+n-1)%n][j]))
print("<E>=%4.2f"%(float(energy)/(n*n)))
sym=["d","u"]
for i in range(n):
    for j in range(n):
        print("%s"%(sym[(spins[i][j]+1)//2]),end=" ")
    print(" ")