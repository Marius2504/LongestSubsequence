def maxim(text):
    return len(text)

# brute method #####################################
def subseq(text1,text2,n,m):
    if m == 0 or n==0:
        return ""
    if text1[n-1] == text2[m-1]:
        return text1[n-1] + subseq(text1,text2,n-1,m-1)
    else:
        return max(subseq(text1,text2,n,m-1),subseq(text1,text2,n-1,m),key=maxim)
#####################################################

def citire(name):
    f=open(name)
    linii = f.readlines()
    v_linii = []
    for linie in linii:
        v_linii.append(linie.rstrip())
    return v_linii

def effseq():
    cuv = []
    for i in range(2,len(matrix[0])):
        matrix[0][i] = v_linii[0][i-2]
    for i in range(2,len(matrix)):
        matrix[i][0] = v_linii[1][i-2]
    for i in range(2,len(matrix)):
        for j in range(2,len(matrix[0])):
            if matrix[i][0] == matrix[0][j]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i][j - 1],matrix[i - 1][j])


    i = len(matrix)-1
    j = len(matrix[0])-1

    while i >=2:
        while j >=2 and i>=2:
            if matrix[i][0] == matrix[0][j]:
                cuv.append(matrix[i][0])
                i = i - 1
                j = j - 1
            else:
                if matrix[i-1][j] > matrix[i][j-1]:
                    i = i -1
                else:
                    j = j -1
        i =i -1
    return "".join(cuv)


v_linii = citire('adn')
n=subseq(v_linii[0],v_linii[1],len(v_linii[0]),len(v_linii[1]))
print(n)

matrix = [[0 for i in range(len(v_linii[0])+2)] for j in range(len(v_linii[1])+2)]
cuv = effseq()
print(cuv)

