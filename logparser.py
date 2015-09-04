#Resolucao dev task - Andre J Protti
from sys import argv

#Implementacao de insertion sort para classificar as frequencias
def insertionsort(vetor):
    for i in range(1, len(vetor)):
        j = i
        while j > 0 and vetor[j-1][1] < vetor[j][1]:
            aux = vetor[j][1]
            vetor[j][1] = vetor[j - 1][1]
            vetor[j - 1][1] = aux
            j -= 1
    return vetor

#Utilizacao do sys argv para escolher o log a ser analisado diretamente do prompt de comando
script, fileName = argv

#Inicializacao de variaveis a serem utilizadas na analise do log
tList = [()]
counter = 0
url = ""
code = 0
splitLine = ""
sizeUrl = 0

#Leitura linha a linha do log
with open(fileName) as log:
    for line in log:
        #Corte por espacos nas linhas e identificao de tamanho das listas resultantes
        splitLine = line.split()
        lenSplitLine = len(splitLine)
        
        sizeUrl = len(splitLine[2])
        sizeCode = len(splitLine[lenSplitLine-1])
        
        #Corte do url e do codigo de status
        url = splitLine[2][12:sizeUrl-1]
        #int() converte em int e garante que sao numeros que o corte da string esta retornando
        code = int(splitLine[lenSplitLine-1][sizeCode-4:sizeCode-1])
        
        tupleUrlCode = url, code
        
        if counter == 0:
            tList[0] = tupleUrlCode
        else:
            tList.append(tupleUrlCode)
            
        counter += 1
       
#Criacao das listas com os valores unicos de websites e codigos de status       
codeList = []
urlList = []        
               
for i in tList:
    if i[1] not in codeList:
        codeList.append(i[1])
    if i[0] not in urlList:
        urlList.append(i[0])

#Criacao de listas com as frequencias de cada valor unico de url/codigo de status        
codeFreq = [0] * len(codeList)
urlFreq = [0] * len(urlList)

for i in tList:
    for j in range(len(urlList)):
        if i[0] == urlList[j]:
            urlFreq[j] += 1
    for j in range(len(codeList)):
        if i[1] == codeList[j]:
            codeFreq[j] += 1
        
#Criacao de matrizes prontas para print com os resultados        
printUrl = [[0 for x in range(2)] for x in range(len(urlList))]
printCode = [[0 for x in range(2)] for x in range(len(codeList))]
        
for i in range(len(urlList)):
    printUrl[i][0] = urlList[i]
    printUrl[i][1] = urlFreq[i]
        
for i in range(len(codeList)):
    printCode[i][0] = codeList[i]
    printCode[i][1] = codeFreq[i]    
              
#Ordenacao insertionsort das frequencias              
printUrl = insertionsort(printUrl)
printCode = insertionsort(printCode)

#Exibicao dos resultados
print "\nFrequencia URLS:\n"
for i in printUrl:
    print "Freq: " + str(i[1]) + " URL: " + str(i[0])
    
print "\nFrequencia Status codes:\n"    
for i in printCode:
    print "Freq: " + str(i[1]) + " Status code: " + str(i[0])   
        
log.close()