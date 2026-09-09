from CSTR import cstr

text1 = "this is a test1 for color"
text2 = cstr("^r^this ^g^is a test2 ^b^for^y^ color")

print(text1)
print(text2)
with open('test.txt','w+') as f:
    f.write(text2)
