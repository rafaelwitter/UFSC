.data
_v: .word 29, 28, 27, 26, 25, 24, 23, 22, 21, -1
_n: .word 10                            # tamanho do arranjo
.text
.globl main

main:
    la   $a0, _v
    lw   $a1, _n
    jal  sort
    li   $v0, 10
    syscall

sort:
    addi $sp, $sp, -12                  # preserva��o de conte�do de
    sw   $ra, 8($sp)                    # registradores na pilha
    sw   $s1, 4($sp)
    sw   $s0, 0($sp)
    move $s0, $zero                     # inicializa��o de `i`

for1tst:                                # in�cio do corpo do la�o externo
    nop                                 # MARCA 1
    slt  $t0, $s0, $a1
    beq  $t0, $zero, exit1
    addi $s1, $s0, -1

for2tst:                                # in�cio do corpo do la�o interno
    slti $t0, $s1, 0
    bne  $t0, $zero, exit2
    sll  $t1, $s1, 2
    add  $t2, $a0, $t1
    lw   $t3, 0($t2)
    lw   $t4, 4($t2)
    slt  $t0, $t4, $t3
    beq  $t0, $zero, exit2
    move $a1, $s1
    jal  swap
    addi $s1, $s1, -1
    j    for2tst                        # fim do corpo do la�o interno

exit2:
    addi $s0, $s0, 1
    j    for1tst                        # fim do corpo do la�o externo

exit1:
    lw   $s0, 0($sp)                    # restaura��o de conte�do de
    lw   $s1, 4($sp)                    # registradores na pilha
    lw   $ra, 8($sp)
    addi $sp, $sp, 12
    jr   $ra

swap:                                   # corpo do procedimento
    sll  $t0, $a1, 2                    # �ndice * 4
    add  $t0, $t0, $a0                  # adicionar ao endere�o do array
    lw   $t1, 0($t0)                    # carregar elemento nesse �ndice
    lw   $t2, 4($t0)                    # carregar elemento posterior
    sw   $t2, 0($t0)                    # trocar posterior com anterior
    sw   $t1, 4($t0)                    # salvar anterior no posterior
    jr   $ra                            # retorno ao programa principal
