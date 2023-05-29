def count_vowels(string: str) -> int:
    vowels = "aeiouAEIOU"  # Lista de vogais
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count
   
