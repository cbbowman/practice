def romanToInt(s):
    result = 0
    for i in range(len(s)):
        if s[i] == "M":
            if i > 0:
                if s[i-1] == "C":
                    continue
            result += 1000
            continue
        if s[i] == "D":
            if i > 0:
                if s[i-1] == "C":
                    continue
            result += 500
            continue
        if s[i] == "C":
            if i == len(s)-1:
                if i > 0:
                    if s[i-1] == "X":
                        continue
                result += 100
                continue
            if s[i+1] == "D":
                result += 400
                continue
            elif s[i+1] == "M":
                result += 900
                continue
            else:
                if i > 0:
                    if s[i-1] == "X":
                        continue
                result += 100
                continue
        if s[i] == "L":
            if i > 0:
                if s[i-1] == "X":
                    continue
            result += 50
            continue
        if s[i] == "X":
            if i == len(s)-1:
                if i > 0:
                    if s[i-1] == "I":
                        continue
                result += 10
                continue
            if s[i+1] == "L":
                result += 40
                continue
            elif s[i+1] == "C":
                result += 90
                continue
            else:
                if i > 0:
                    if s[i-1] == "I":
                        continue
                result += 10
                continue
        if s[i] == "V":
            if i > 0:
                if s[i-1] == "I":
                    continue
            result += 5
            continue
        if s[i] == "I":
            if i == len(s)-1:
                result += 1
                continue
            if s[i+1] == "V":
                result += 4
                continue
            elif s[i+1] == "X":
                result += 9
                continue
            else:
                result += 1
                continue
    return result

def main():
    test1 = romanToInt("IX") == 9
    test2 = romanToInt("LVIII") == 58
    print(test1)
    print(romanToInt("IX"))
    print(test2)

if __name__ == "__main__":
    main()