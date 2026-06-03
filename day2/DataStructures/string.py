s = "Hello everyone. How are you doing"
print(s)
s = s.upper()
print(s)
s = s.lower()
print(s)
st = "   abcdefghojkl   "
print(st)
st = st.strip()
print(st)

# keyword searching
string = "i am feeling very lazy today"
lazy_word = [st.replace("lazy","bored") for st in string.split(' ')]
print(lazy_word)