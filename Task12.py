text = input()
if text.count('f') > 1:
    print(text.index('f'), text.rindex('f'))
if text.count('f') == 1:
    print(text.index('f'))
else:
    print()