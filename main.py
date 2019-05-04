from ply import *
import argparse
import flex
import myparser
import genasm
import subprocess
import platform


system_platform = platform.system()

# parser = argparse.ArgumentParser(description='Bcc compiler')
# parser.add_argument("input", help="Path of file to compile.")
# parser.add_argument("output_asm", help="Output assembly file name.")
# parser.add_argument("output_exec", help="Output executeable file name.")
# args = parser.parse_args()
lines = open("text.bcc", 'r').read()
genasm.lexer = flex.lexer
result = myparser.parse(lines)
var = {}
var['c'] = 'b'
ab = "abcdefg"
abb = "'"+ab+"'"
if 'a' not in var:
     print("yessssssssss")
print(ab[:-3])
print(result)
genasm.statement_main(result)


print("\n----- ASM simple -----")
print(genasm.getHeader())
print(genasm.getData())
print(genasm.getText())



if result:
     file = open("test.asm", 'w')
     file.writelines(genasm.asmheader)
     file.writelines(genasm.asmdata)
     file.writelines(genasm.asmtext)
     file.writelines(genasm.asmexit)
     file.close()

     '''if system_platform not in nasm_args:
         print("Compile to executeable for this platform is not supported yet.")
     else:
         nasm_arg = nasm_args[system_platform]
         p = subprocess.Popen(['nasm', '-f', nasm_arg, args.output_asm, '-o', args.output_asm[:-3] + 'o'])
         p.wait()
         p = subprocess.Popen(
             ['gcc', '-w', '-no-pie', '-m64', '-o', args.output_exec, args.output_asm[:-3] + 'o'])
         p.wait()
         print("Compiled successfully.")'''