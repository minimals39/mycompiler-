extern printf
extern fflush
global main
section .data
x   dq     9
y   dq     6
sum  dq     15
a dd "%d ", 13
section .text
main:
mov rcx, a
mov rdx, [y]
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
