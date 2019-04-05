
# List

meineZahlen = list(range(1,6))
nummern = [nummer * 2 for nummer in meineZahlen]
print(nummern)

# Dictionary

meinText = '''
a b dfd fdfsdfs
dfsd
gfgg
'''

meineStat = {zeichen: meinText.count(zeichen) for zeichen in meinText}
print(meineStat)

# Set

otherChars = {char for char in meinText if char not in 'aeiou\n'}
print(otherChars)