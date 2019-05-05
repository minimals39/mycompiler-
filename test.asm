DEFAULT REL
extern printf
extern fflush
global main
section .data
a dq "%d " ,0,0,0,0,0,0,0,0,0
i dq  "%d ", 1
section .text
main:
mov rax, 10
mov [a + 1 * 8], rax
mov rax,20
mov rbx, [i+8]
mov [a+rbx*8],rax
mov rcx, a
mov rdx, [a +8]
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
