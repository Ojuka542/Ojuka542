# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Example usage:
user_sentence = input("Enter a sentence: ")
result = count_vowels(user_sentence)

print(f"The number of vowels in the sentence is: {result}")



