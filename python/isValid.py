def main():
    test1 = isValid("{") == True
    test2 = isValid("{df(sdfs[asdf}d]dfdf)sdfsdd}") == False
    print(test1)
    print(test2)

def isValid(s):
    close = []
    for c in s:
        if c == "}" or c == ")" or c == "]":
            if not len(close):
                return False
            elif c == close[-1]:
                close.pop()
                continue
            else:
                return False
        if c == "{":
            close.append("}")
        elif c == "(":
            close.append(")")
        elif c == "[":
            close.append("]")
    if len(close):
        return False
    else:
        return True

if __name__ == "__main__":
    main()