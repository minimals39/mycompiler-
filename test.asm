DEFAULT REL
extern printf
extern fflush
global main
section .data
i dq  "%d ", 1
j dq  "%d ", 1
count dq  "%d ", 0
max dq  "%d ", 0
_INT0 dq "%d ",1
_INT1 dq "%d ",0
section .text
main:
loop0:
mov rax, [i+8]
mov rbx,101
cmp rax,rbx
jge endloop0
mov rax, [_INT0+8]
mov [j+8], rax
mov rax, [_INT1+8]
mov [count+8], rax
mov rbx, [i+8]
mov rax, 1
add rbx,rax
push rbx
xor rax,rax
pop rbx
mov [max+8],rbx
xor rbx,rbx
loop1:
mov rax, [j+8]
mov rbx, [max+8]
cmp rax,rbx
jge endloop1
if0:
mov ax, [i+8]
mov bl, [j+8]
div bl
push ax
xor ah,ah
pop ax
mov cl, ah
movsx rax, cl
mov rbx,0
cmp rax,rbx
jne end0
mov rbx, [count+8]
mov rax, 1
add rbx,rax
push rbx
xor rax,rax
pop rbx
mov [count+8],rbx
xor rbx,rbx
end0:
mov rbx, [j+8]
mov rax, 1
add rbx,rax
push rbx
xor rax,rax
pop rbx
mov [j+8],rbx
xor rbx,rbx
jmp loop1
endloop1:
if1:
mov rax, [count+8]
mov rbx,2
cmp rax,rbx
jne end1
mov rcx, i
mov rdx, [i +8]
call printf
xor rcx, rcx
call fflush

end1:
mov rbx, [i+8]
mov rax, 1
add rbx,rax
push rbx
xor rax,rax
pop rbx
mov [i+8],rbx
xor rbx,rbx
jmp loop0
endloop0:
xor rax, rax
pop rbp
ret
