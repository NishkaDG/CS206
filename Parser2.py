from pyparsing import *
from string import ascii_lowercase

varmap = dict()

nonzero = ''.join([str(i) for i in range(1, 10)])
integer = Word(nonzero, nums)('number')
intdec = Word('int')('declaration')
varname = Word('[A-Za-z]+')('variable name')
vardec = (intdec + varname)('declared variable')
var = (vardec ^ varname)('variable')
equals = Literal('=').suppress()('equal to')
operator = Word('+-*/', exact=1)('operator')
operand = (integer ^ varname)('operand')
operation = (operand + OneOrMore(operator + operand))('operation')
eol = Word(';', exact=1)('semicolon')
expression = (var + equals + operation)('expression')
stmt = ((vardec + eol) ^ (expression + eol))('statement')
stmt_list = ZeroOrMore(stmt)('statement list')
begin = Word('begin:')('begin')
end = Word('end:')('end')
program = (begin + stmt_list + end)('program')

def parse_command(cmd):
        return expression.parseString(cmd)

def get_value(s):
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
                        print('Unknown variable:',s)
                        return None
        return value

def calculate(parts):
        global varmap
        op1 = parts[1]
        op2 = parts[3]
        operator = parts[2]
        op1 = get_value(op1)
        op2 = get_value(op2)

        if op1 is None or op2 is None:
                print('Unable to execute command')
                return
        funcs = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

        varmap[parts[0]] = funcs[operator](op1, op2)

def assign(parts):
        value = get_value(parts[1])
        if value is None:
                print('Unable to execute command')
                return
        varmap[parts[0]] = value

def execute_command(cmd):
        try:
            parts = parse_command(cmd)
        except ParseException:
            print('Exception while parsing command: ', ParseException)
            return

        if len(parts) == 2:
            assign(parts)
        else:
            calculate(parts)

def dump_state():
        global varmap
        print(varmap)

def main():
        lines = []
        fulltext = ''
        err = 0
        fname = input('Enter the filename: ')
        with open(fname)as f:
                lines = f.readlines()
        for l in lines:
                fulltext = fulltext+l
        lines = [l.strip() for l in lines]
        try:
                parts = program.parseString(fulltext)
                for part in parts:
                        print(part)
        except ParseException:
                print('Error in program. Check the syntax. ', ParseException)
                err = 1
        '''if err==0:
                for i in range(1, len(lines)-1):
                        l = lines;
                        parts = stmt.parseString(l)
                        if not parts[0].getName() == 'declaration':
                                parse_command(l)
'''
if __name__ == '__main__':
    main()
