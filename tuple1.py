alfab = "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
n = int
numbers = {}
for i in range(int(input())):
    i = str(input())
    n = alfab.index(i[0])
    numbers[n] = i
for i in range(len(numbers)):
    print(numbers.pop(min(numbers.keys())))