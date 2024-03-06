def letter_boxed(file_path, top, left, right, bottom):

    possible_words = []

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:                        
                if not word_is_valid(word):
                    continue
                possible_words.append(word)

    possible_solutions = []
    for word in possible_words:
        for other_word in possible_words:
            if word == other_word:
                continue

            if word[len(word)-1] != other_word[0]:
                continue

            if not words_got_all_letters(word, other_word):
                continue

            mytuple = (word, other_word)
            possible_solutions.append(mytuple)
        
    return possible_solutions

def word_is_valid(word):
    for i in range(0, len(word)):
        if i == len(word) - 1:
            return True
        
        if word[i] in top and word[i+1] in except_top:
            continue
        elif word[i] in bottom and word[i+1] in except_bottom:
            continue
        elif word[i] in right and word[i+1] in except_right:
            continue
        elif word[i] in left and word[i+1] in except_left:
            continue
        else:
            return False

def words_got_all_letters(word, other_word):
    all_letters = top + left + right + bottom

    first_set = set(all_letters)
    second_set = set()

    for char in word:
        second_set.add(char)

    for char in other_word:
        second_set.add(char)

    return first_set == second_set
        

# Example usage
file_path = 'words.txt'
top = ['e', 'i','f']
left = ['o', 'n','u']
right = ['b', 'a','q']
bottom = ['c', 'l','m']
except_top = left + right + bottom
except_left = top + right + bottom
except_right = top + left + bottom
except_bottom = top + left + right
answers = letter_boxed(file_path, top, left, right, bottom)
print(answers)
