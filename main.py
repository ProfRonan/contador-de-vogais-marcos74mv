def count_vowels(string: str) -> int:
    vowels = "aeiouAEIOU"  # Lista de vogais
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count
    
print(count_vowels("xyz"))       # Saída: 0
print(count_vowels("aeiou"))     # Saída: 5
print(count_vowels("AbCdeFG"))   # Saída: 3
print(count_vowels("hello123"))  # Saída: 2
print(count_vowels("hello!@#"))  # Saída: 2
