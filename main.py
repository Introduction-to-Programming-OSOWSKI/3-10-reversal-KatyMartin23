def reversal(w):
    word = ""
    for i in range(len(w), 0, -1):
        word = word + w[i-1]
    return word

print(reversal("potato"))