def QuickSort(A: list, limInf: int, limSup: int, x: int):
	if limInf < limSup:
		i = Particione(A, limInf, limSup, x)
		QuickSort(A, limInf, i-1, x)
		QuickSort(A, i+1, limSup, x)
	
def Particione(A: list, limInf: int, limSup: int, x: int):
	if x == 0:
		indice_pivo = limInf
	elif x == 1:
		indice_pivo = limSup
	else:
		indice_pivo = (limInf + limSup) / 2
	pivo = A[indice_pivo]
	A[limSup] = pivo
	A[indice_pivo] = pivo
	i = limInf - 1
	
	for j in range(limSup - 1):
		if A[j] <= pivo:
			i += 1
			temp = A[j]
			A[j] = A[i]
			A[i] = temp
	#print(A[i])
	temp = A[i+1]
	A[i+1] = A[limSup]
	A[limSup] = temp
	return i + 1

def main():
	A = [30,20,50,10,70,80,90,100,60,40]
	x = 1
	print(QuickSort(A,0,9,x))
main()
