text=input("enter the string")
def swapcodo(s,n):
    sawpstring=""
    for char in s:
        if char==',':
            sawpstring+='.'

        elif char=='.':
            sawpstring+=','

         else:
            sawpstring+=char

    tstring=""
        for i in range(len(sawpstring)):
                    char=sawpstring[i]
                    if i<n:
                    if 'A'<=char<='Z':
                                
