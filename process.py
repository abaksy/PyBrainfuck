import re
def clean(text):
    text = text.replace("\n", '')
    text = text.replace(" ", '')
    pattern = re.compile(r"[^<>[\].,+-]")
    text = pattern.sub("", text)
    return text

def bracket_matching(text):
    bracket_indices = dict()
    stack = []
    flag=1
    for i in range(len(text)):
        if text[i] not in ['[', ']']:
            continue
        if text[i] == '[':
            stack.append((text[i], i))
        if stack == []:
            flag=0
            break
        if text[i] == ']':
            top_element = stack.pop()
            if top_element[0] != '[':
                flag=0
                break
            else:
                bracket_indices[top_element[1]] = i
    if flag==1:
        return bracket_indices
    else:
        return None