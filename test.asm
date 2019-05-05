DEFAULT REL
extern printf
extern fflush
global main
section .data
i dq  "%d ", 4
j dq  "%d ", 2
count dq  "%d ", 0
section .text
main:
mov rbx, [i+8]
mov rax, [j+8]
imul rbx,rax
push rbx
xor rax,rax
pop rbx
mov [count+8],rbx
xor rbx,rbx
mov rcx, count
mov rdx, [count +8]
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
