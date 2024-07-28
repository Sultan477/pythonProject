def max_substring(s):
    if not s:
        return {}

    curr_elem = s[0]
    result = {}
    counter = 0
    for elem in s:
        if elem != curr_elem:
            result[curr_elem] = max(counter, result.get(curr_elem, 0))
            curr_elem = elem
            counter = 1
        else:
            counter += 1


    result[curr_elem] = max(counter, result.get(curr_elem, 0))
    return result

if __name__ == '__main__':

    # string = 'aabbbaaaaccbbccc'
    # string = ''
    string = 'ccbbccc'
    print(max_substring(string))

