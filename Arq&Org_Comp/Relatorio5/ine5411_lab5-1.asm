.data
_v: .word 29, 28, 27, 26, 25, 24, 23, 22, 21, -1
_k: .word 2                             # índice da palavra a ser trocada
.text
.globl main

main:                                   # inicialização dos parâmetros
    la   $a0, _v
    lw   $a1, _k
    jal  swap
    li   $v0, 10
    syscall

swap:                                   # corpo do procedimento
    sll  $t0, $a1, 2                    # índice * 4
    add  $t0, $t0, $a0                  # adicionar ao endereço do array
    lw   $t1, 0($t0)                    # carregar elemento nesse índice
    lw   $t2, 4($t0)                    # carregar elemento posterior
    sw   $t2, 0($t0)                    # trocar posterior com anterior
    sw   $t1, 4($t0)                    # salvar anterior no posterior
    jr   $ra                            # retorno ao programa principal
