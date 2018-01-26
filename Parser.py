import re
from pyparsing import Optional, Word, Literal, Forward, alphas, nums, Group, ZeroOrMore, oneOf, delimitedList, cStyleComment, restOfLine
import pprint
 
lines = []
vardec = dict()
error = 0
varmap = dict()
bnf = None

def syntaxCheck(fname):
  global vardec
  global lines
  global error
  with open(fname) as f:
    lines = [line.rstrip('\n') for line in f]
  if(lines[0]!="begin:"):
    print("Error: Program must begin with begin: statement.")
    error = error+1
  elif(lines[len(lines)-1]!="end:"):
    print("Error: Program must end with end: statement.")
    error = error+1
  else:
    for i in range(1, len(lines)-1):
      l = lines[i]
      #print(l)
      if(len(l)>0):
        if(not l.endswith(';')):
          print("Error in line "+str(i)+": Each statement must end with a semicolon.")
          error = error+1
          return []
        else:
          if(not l.startswith("int ")):
            try:
              var = l[:l.index("=")].rstrip()
              if(not var in vardec.keys()):
                #for k in vardec.keys():
                 # print(k, vardec[k])
                print("Error in line "+str(i)+": Variable not declared.")
                error = error+1
                return []
            except ValueError:
              print("Error in line "+str(i)+": Variable without assignment or declaration.")
              error = error+1
              return []
          else:
            try:
              vname = (l[4:l.index("=")]).rstrip()
            except ValueError:
              vname = l[4:len(l)-1]
            vardec[vname] = "int"
  if(error == 0):
    print("Program is correct")
    return lines

def parse_command(cmd, lno):
  global bnf
  return bnf.parseString(cmd)

def get_value(s, lno):
  global varmap
  value = None
  try:
    value = int(s)
  except ValueError:
    pass
  if value is None:
    try:
      value = varmap[s]
    except KeyError:
      print("Error in line ",lno, ": unknown variable: ", s)
      return None
  return value

def calculate(parts, lno):
  global varmap
  op1 = parts[1]
  op2 = parts[3]
  operator = parts[2]
  op1 = get_value(op1)
  op2 = get_value(op2)
  
  if op1 is None or op2 is None:
    print("Error in line ", lno, ": Unable to evaluate.")
    return
  funcs = {
  '+': lambda a, b: a + b,
  '-': lambda a, b: a - b,
  '*': lambda a, b: a * b,
  '/': lambda a, b: a / b,
  }
  
  varmap[parts[0]] = funcs[operator](op1, op2)
  
def assign(parts, lno):
  global varmap
  value = get_value(parts[1])
  if value is None:
    print("Error in line ", lno, ": Unable to evaluate.")
    return
  varmap[parts[0]] = value

def execute_command(cmd, lno):
  try:
    parts = parse_command(cmd)
  except ParseException:
    print("Error in line ", lno, ".")
    return
  
  if len(parts) == 2:
    assign(parts)
  else:
    calculate(parts)

def BNF():
  global bnf
  if bnf is None:
    ident = Word( alphas+"_", alphas+nums+"_$" )
    integer = Word( nums )
    equal = Literal("=")
    semi = Literal(";").suppress()
    typeName = ident
    varName = ident  
    typeSpec = "int"
    varnamespec = varName
    operand = varName | integer
    operator = oneOf("+ - * /")
    expression = Group(operand + ZeroOrMore(operator + operand) + semi)
    memberDecl = Group( ( typeSpec | typeName ) + Group( delimitedList( varnamespec ) )  + Optional(expression) + semi )
    stmt = memberDecl | Group(varnamespec + equal + expression)
    bnf = stmt
  return bnf

def main():
  global bnf
  BNF()
  lines = []
  fulltext = ""
  err = 0
  fname = input("Enter the filename: ")
  lines = syntaxCheck(fname)
  if len(lines)>0:
    for i in range(1, len(lines)-1):
      l = lines;
      parts = bnf.parseString(l)
      if "=" in parts:
        execute_command(l, i)

if __name__ == '__main__':
  main()
