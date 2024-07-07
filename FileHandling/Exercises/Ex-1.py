#   1)Write a Python program to read the content from a text file "poem.txt" line by line and display the same on screen.
poem = open("poem.txt",'r')
print(poem.read())
poem.close()

#   2)Write a function in python to count the number of lines from a text file "story.txt".
def count_lines(file_name,mode):
    count = 0
    with open(file_name,mode) as fp:
        for lines in fp:
            print(lines)
            count += 1
    print(f'The no.of lines present in the given file are {count}')
count_lines('story.txt','r')

#   3)Write a function in Python to count and display the total number of words in a text file.
def count_words (file_name,mode):
    word_count = 0
    with open(file_name,mode) as fp:
        for lines in fp:
            words = lines.split()
            word_count += len(words)
    print(f'The no.of words in the given file are {word_count}')
count_words('story.txt','r')

#   4)Write a function in Python to read lines from a text file "story.txt", and display those words, which are less than 4 characters
def display_words(file_name,mode):
    words_count = 0
    with open(file_name,mode) as fp:
        for lines in fp:
            words = lines.split()
            for word in words:
                if len(word) < 4:
                    words_count += 1
                    print(word)
    print(f'The no.of words which are present in the story.txt with less the 4 characters are {words_count}')
display_words('story.txt','r')

#   5)Write a function in Python to count the words "this" and "these" present in a text file "article.txt".
def this_these_count(file_name,mode):
    this_these = 0
    with open(file_name,mode) as fp:
        for lines in fp:
            words = lines.split()

            for word in words:
                word = word.lower()
                if word in ['this','these']:
                    this_these  += 1

    print(f'the no.of this and these words presnt in the article.txt are {this_these}')



this_these_count('article.txt','r')



