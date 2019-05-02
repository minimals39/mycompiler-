import sys

#Global Var

lexer = None

asmheader = ("DEFAULT REL\n" +
             "extern printf\n" +
             "extern fflush\n" +
             "global main\n")
asmdata = 'section .data\n'
asmtext = "section .text\n" + "main:\n"
asmexit = 'xor rax, rax\npop rbp\nret\n'

fflush_label = "fflush"

empty_str = '""'
str_prefix = "_STR"
global_str_counter = 0
global_str = {}
global_var = []
global_if_counter = 0

reg_order = ["rcx", "rdx", "r8", "r9"]

#------------------------------------ Get Set Add Function

def getHeader():
    global asmheader
    return asmheader

def getData():
    global asmdata
    return asmdata

def getText():
    global asmtext
    return asmtext

def getLeave():
    global asmexit
    return asmexit

#------------------------------------ Add Assembly code section
def addData(name, value):
    global asmdata
    asmdata += "%s db %s\n" % (name, value)

def addText(asmcode = ""):
    global asmtext
    asmtext += asmcode + "\n"

def addComment(cmd = ""):
    global asmtext
    asmtext += ";" + cmd +"\n"

#------------------------------------ Choose Function Section

def getFunction(Tuple):
    print("-", Tuple[1]) #test
    if Tuple[0] is not "Start": #Found an error or EoF
        print("EoF")
        return "Exit"
    else:
        TempTuple = Tuple[1]
        return TempTuple[0]

def statement_main(tuple):
    ThisTuple = tuple
    while(True):
        state = getFunction(ThisTuple)
        stateTuple = ThisTuple[1]
        print("",state)
        if state == "Exit":
            addText("")
            addComment("")
            addText(asmexit)
            break
        elif state == "DECLARATION":
            print("")
            declacration_routine(stateTuple)
        elif state == "PRINT":
            print("")
            print_routine(stateTuple)
        elif state == "PRINTLN":
            print("")
            println_routine(stateTuple)
        elif state == "FORLOOP":
            print("")
        elif state == "WHILELOOP":
            print("")

        #Next STM
        currentTuple = currentTuple[2]
        print("-----------------------------")

#------------------------------------ All Function Section
def declare_var(var_name, value, assign=None):
    global global_var
    global asmdata

    if var_name in global_var:
        print("Error!, Duplicate var is declared")
    else:
        global_var.append(var_name)
        if assign is None:
            addData(var_name, value)
        elif assign == "arrayDup":
            asmdata += var_name + " times " + str(value) + " dq 0" + "\n"

def declacration_routine(stm):
    #print("visited declacration_routine")
    print(type(stm[2]))
    if type(stm[2]) is not tuple: #Default
        if stm[1] == "string":
            declare_var(stm[2],"'             $', 0")
        else:
            declare_var(stm[2],"0")
    else:
        temp = stm[2]
        print(temp)
        print(temp[0])
        if temp[0] == "ArrayDeclaration":
            declare_var(temp[1], temp[3], "arrayDup")
        elif temp[0] == "ArrayMultiAssign":
            name = temp[1]
            arrValue = getMultival(temp[5])
            declare_var(name, arrValue)
        elif temp[0] == "AssignConstant":
            if type(temp[3]) == tuple:      #Need operation routine
                operation_routine(temp[3])
            else:
                declare_var(temp[1], temp[3])
        elif temp[0] == "AssignString":
            print("sth")
        else:
            print("I think something went wrong :T")