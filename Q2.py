text=input("enter the string")
def count_vowels(text):
    vowels="aeiouAEIOU"
    totalvowels=0
    uniquevowels=set()

    for char in text:
        if char in vowels:
          totalvowels+=1

        uniquevowels.add(char.lower())

        uniquevlist=sorted(uniquevowels)

        print(f"vowels:{totalvowels}")
        print(','.join(uniquevlist))

count_vowels(text)
