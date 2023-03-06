def solution(babbling):
    answer = []
    count = 0
    for n in babbling:
        n = n.replace('aya' , '*')
        n = n.replace('ye', '*')
        n = n.replace('woo' , '*')
        n = n.replace('ma', '*')
        answer.append(str(set(n)))
        
    for a in answer:
        if "{'*'}"== a:
            count += 1
        else:
            continue
    return count