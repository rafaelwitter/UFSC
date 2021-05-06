.data						#Segmento de dados de um programa (dados que ficam em memoria). 
_VETOR: .word 0x01,0x02,0x0A,0xBA,0x00		#Vetor de 5 posices com valores descritos em hexadecimal. VETOR[0] = 0x01, VETOR[1] = 0x02...
i: .word 2					#Valor inteiro simples
.text
.globl main
main:
	la $s0, i				#Carrega o endereco do label "i" no registrador $s0.  uma pseudoinstru��o
	la $s1, _VETOR				#Carrega o endereco do label "_VETOR" no registrador $s1. O endereco do label � igual ao primeiro endereco do vetor (VETOR[0])
	
	#Leitura de valores da mem�ria
	lw $t0, 0($s1)				#Carrega em $t0 o valor armazenado na posicao de mem�ria apontada por $s1+0 ($t0 = VETOR[0])
	lw $t1, 4($s1)				#Carrega em $t1 o valor armazenado na posicao de memoria apontada por $s1+4 ($t1 = VETOR[1])
	lw $t2, 8($s1)
	
	#Operacoes aritm�ticas simples e armazenamento em mem�ria
	add $t3, $t0, $t1			#Salva no registrador $t3 o resultado da soma dos valores nos registradores $t0 e $t1 ($t3 = $t0 + $t1).
	addi $t3, $t3, 1			#Realiza uma soma imediata ($t3 = $t3 + 1)
	sw $t3, 16($s1)			#Armazena o valor de $t3 na posicao de memoria apontada por $s1+16 (VETOR[4] = $t3)
	
	#Calculo do endereco de memoria VETOR[i]
	lw $s2, 0($s0)				#Carrega em $s2 o valor armazenado na posicao de memoria apontada por $s0 ($s2 = i)
	sll $t8, $s2, 2				#$t8 recebe o valor de $s2 deslocado dois bits para a esquerda ($t8 = $s2<<2 ou $t8 = 4*$s2) (se i=2, $t8=8)
	add $t8, $t8, $s1			#Soma o deslocamento de i com o endereco do vetor em memoria. Para i=2, o resultado final � o endereco de VETOR[2] que tamb�m � calculado como 8($s1)
	lw $t4, 0($t8)				#Carrega em $t4 o valor armazenado na posicao de memoria apontada por $t8 ($t4 = VETOR[i]
	
	#Calculo do endereco de mem�ria VETOR[2 + VETOR[0]]
	lw $t0, 0($s1)				#Carrega em $t0 o valor armazenado na posicao de memria apontada por $s1+0 ($t0 = VETOR[0])
	sll $t0, $t0, 2				#$t0 = $t0*4
	add $t0, $t0, $s1			#$t0 = $t0 + $s1 (VETOR[VETOR[0]])
	lw $v0, 8($t0)				#$v0 = VETOR[2 + VETOR[0]]
	
	#Zerando registradores para exemplo
	add $t0, $zero, $zero			#$t0 = 0+0
	addi $t1, $zero, 0			#$t1 = 0+0
	move $t2, $t0		                #pseudoinstrucao
