word = input("Input a word:")
word_list = list(word)
print(word_list)

result = []
for _ in range(len(word_list)):
    result.append(word_list.pop())
    # You can get the last value if you extract value by pop()

print(result)
print(word[::-1])
