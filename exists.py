def exists(word,word_list):
    for w in word_list:
        if word == w:
            return True
    return False

top = ["cheese", "pepe", "onion"]
result = exists("onion", top)
top.pop()
result = exists("onion", top)
print(result)