conyruns = [0]*100000

def brown(i):



def conyrun(n):

    if n == 1:
        conyruns[n] = 1
        return 1
    else:
        conyruns[n] = conyrun(n-1) + 1
        return conyruns[n]

i = 1
while True:
    conyruns = [0]*i
    conyrun(i)
    cony_distance = sum(conyrun)
    brown(i)



conyrun(10)
print(conyruns)
print(sum(conyruns))

#
# while True:
#     conyrun(1) = 1
#     conyrun(n) = conyrun(n-1) + 1