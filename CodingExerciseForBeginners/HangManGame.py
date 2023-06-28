#HangManGame 

mistake = [
    '''
    +---+
    |   |
    0   |
        |
        |
        |
  ========
  
''',

    '''
    +---+
    |   |
    0   |
    |   |
        |
        |
  ========
    
''',
    '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
  ========
    
''',
    '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
  ========
    
''',
'''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
  ========
    
''',
'''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
  ========
    
'''
]

print('Let\'s Play HangMan!')
print(f'You have only 6 lives so try to guess the word within 6 attempts! Good luck!!')

name = input('Enter a word : ')
n = len(name)
l = list()
for i in range(n):
    l += '_'
print(l)

win_status = 0
m = 0


while(1):
    