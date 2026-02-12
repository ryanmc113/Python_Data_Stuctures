from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

# print("Inital stack:")
# print(stack)

# print("Each element popped off the stack")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print("Empty Stack")
# print(stack)

# print("\n")


def ide_systax_check(syn_string):
    string_stack = []
    syntax_push = ["(", "{", "["]
    syntac_pop = [")", "}", "]"]
    syn_match = {"(": ")", "{": "}", "[": "]"}
    for s in syn_string:
        if s in syntax_push:
            string_stack.append(s)
        if s in syntac_pop:
            if len(string_stack) < 1:
                print("False")
                return False
            if s == syn_match.get(string_stack[len(string_stack) - 1]):
                string_stack.pop()
            else:
                print("False")
                return False
    if len(string_stack) == 0:
        print("True")
        return True
    # print(string_stack)


def test():
    test_l = ["("]
    test_match = {"(": ")", "{": "}", "[": "]"}
    if test_l[len(test_l) - 1] == test_match.get(test_l[len(test_l) - 1]):
        print("true")
    print(test_l[len(test_l) - 1])
    print(test_match.get(test_l[len(test_l) - 1]))


ide_systax_check("if (a > b) { print(c); } ")
ide_systax_check("if (a > b} { print(c); } ")
ide_systax_check("if (a > b)} { print(c); } ")
# test()
