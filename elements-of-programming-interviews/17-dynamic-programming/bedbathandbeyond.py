# page 310

def get_decomposition(word, word_list):
    return decomposition(word, set(word_list), {})

def decomposition(word, word_set, cache):
    if word == '':
        return []
    if word in cache:
        return cache[word]
    for i in xrange(1, len(word)):
        chunk = word[:i]
        if chunk in word_set:
            d = decomposition(word[i:], word_set, cache)
            if d:
                result = [chunk] + d
                cache[word] = result
                return result
    if word in word_set:
        return [word]
    return []

word_list = ['bed', 'bath', 'hand', 'and', 'beyond', 'bat']
word_list2 = ['bed', 'bath', 'and', 'beyond']
word_list3 = ['be', 'dbath', 'and', 'bey']
word = 'bedbathandbeyond'
print get_decomposition(word, word_list)
print get_decomposition(word, word_list2)
print get_decomposition(word, word_list3)
