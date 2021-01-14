# Ex039 - Understanding functions (def)

def add_number(n1, n2):
    ret = n1+n2
    return ret

def add_txt(t1, t2):
    print(t1+t2)

ans = add_number(10, 15)
print(ans)      # 25 is printed out.
text1 = 'Korea~'
text2 = 'Hooray!!'
add_txt(text1, text2)   # 'Korea~Hooray!!' is printed out
