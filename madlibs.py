noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
place1 = input("Enter a place: ")
adj1 = input("Enter an adjective: ")

def Madlib1():
    print('\n\nOnce upon a time, a small {}\n came along and {}\n my socks. I walked to {}\n and bought a {} pair'.format(noun1, verb1, place1, adj1))

def Madlib2():
    print('\n\nWhile walking home, I ran into {}\n. They {}\n me then continued walking to {}\n. The encounter was {}'.format(noun1, verb1, place1, adj1))

def user_choice():
    answer = int(input('Choose your own adventure. Enter 1 or 2 to choose your story.'))
    return answer

if __name__ == "__main__":
    answer = user_choice()
    if answer == 1:
        Madlib1()
    else:
        Madlib2()
    
        