def reverseVowels(s):
    left, right = 0, len(s)-1
    vowels = set('aeiouAEIOU')
    s = list(s)
    while left < right < len(s):
        while s[left] not in vowels and left < right:
            left += 1
        while s[right] not in vowels and left < right:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

str = "Aa"
print reverseVowels(str)
