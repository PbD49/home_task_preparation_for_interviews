from typing import Dict
from class_stack import Stack


def check_brackets(string: str) -> str:
    stack = Stack()
    brackets: Dict[str, str] = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.is_empty() or stack.pop() != brackets[char]:
                return "Несбалансированно"
        else:
            continue

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


string1 = "(((([{}]))))"
string2 = "[([])((([[[]]])))]{()}"
string3 = "{{[()]}}"
string4 = "}{}"
string5 = "{{[(])]}}"
string6 = "[[{())}]"

print(check_brackets(string1))
print(check_brackets(string2))
print(check_brackets(string3))
print(check_brackets(string4))
print(check_brackets(string5))
print(check_brackets(string6))
