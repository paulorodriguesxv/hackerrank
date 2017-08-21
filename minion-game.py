def minion_game(string):
    # your code goes here

    mystring = list(string)
    mystring_size = len(mystring)
    vowels = ('A', 'E', 'I', 'O', 'U')

    points = {}
    count = 5
 
    while count <= mystring_size -1: 
        for i in range(mystring_size):
            if i + count > mystring_size: break

            print(mystring[i:i+count])
        count += 1    

minion_game('BANANA')