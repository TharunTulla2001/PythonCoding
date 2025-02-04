def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = ""


    for chars in zip(*strings):
        print(chars)
        if (len(set(chars)))==1:
            prefix+=chars[0]
        else:
            break

    return prefix

words = ["flower", "flow", "flows","flore"]
print("Longest Common Prefix:", longest_common_prefix(words))
