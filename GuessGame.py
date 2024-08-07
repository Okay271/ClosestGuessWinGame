# Update and Sort the second arr2 according to the sortin gof the arr1
def bubble_sort(arr1, arr2):
    length = len(arr1)
    
    for i in range(length):
        is_swapped = False
        for j in range(0, length-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                is_swapped = True
        if not is_swapped:
            break

# Sorts the players list according to the scores that players get and print the players from last to first
def print_winner():
    
    bubble_sort(scores, players)  
    scores.reverse()
    players.reverse()
    for i in range(len(players)-1, -1, -1):
        print(str(i+1) + ". " + players[i] + " ( " + str(scores[i]) + " )")

# Checks whether there are differences with same amount and return the groups of values that have dsame differences. 
# Same differences get same points afterwards.
def how_many_same():
    same_groups = []
    count = 0
    start_value = 0
    entered = False
    for i in range(len(differences)-1):
        if differences[i] == differences[i+1]:
            count += 1
            if not entered:
                start_value = i
                entered = True
        else:
            if entered:
                same_groups.append((count+1, start_value))
                count = 0
                entered = False
    
    if entered:
        same_groups.append((count+1, start_value))

    return same_groups

# Checks whether obtained answers' number is equal to the total number of the players' number
def check_answer_number(answers):
    return len(players) == len(answers)
     
players = input("Enter Players' Names By Seperating ',' :: ").split(",")
scores = []

for i in range(len(players)):
    scores.append(0)
    
is_finished = False
hand = 1

while is_finished == False:
    
    print()
    print("-------SCORE TABLE-------")
    for i in range(len(players)):
        print(players[i] + " --> " + str(scores[i]))
    
    print()
    print("Question " + str(hand)) 
    answer = input("For Guess Question Enter 'g' || For Multiple Choice Questions Enter 'm' || Enter f To Finish The Game :: ")
    
    if answer.lower() == "f": # FINISH
        is_finished = True
        print_winner()
    
    elif answer.lower() == "g":
        
        print("----- WELCOME TO THE GUESSING SECTION -----")
        
        valid_data = False
        
        while not valid_data:
            answer = input("Enter Answers By Seperating ',' and Using Capital Letters :: ").split(",")
            is_valid = check_answer_number(answer)
            
            if is_valid:
                valid_data = True
            else:
                print("Try Again! Your Input Contradicts With Player Number")
            
        hand += 1
        correct_answer = float(input("Enter the Correct Answer:: "))
        differences = []
        players_for_count = players.copy()
            
        for values in answer:
            differences.append(abs(correct_answer - float(values)))
            
        bubble_sort(differences, players_for_count)
            
        print("-----FROM CLOSEST TO FARTHEST-----")
        for i in range(len(players)):
            print(players_for_count[i] + " --> " + str(differences[i]))
            
        print("-----******************-----")
        max_score = len(players)
        m = 0
        same_groups = how_many_same()
            
        while m < len(players):
            
            is_same_group = False
                
            for group in same_groups:
                count, start = group
                if m == start:
                    is_same_group = True
                    for i in range(start, start+count):
                        index = players.index(players_for_count[m])
                        scores[index] += max_score
                        m +=1
                    max_score -= 1
                    break
                
            if not is_same_group:
                index = players.index(players_for_count[m])
                scores[index] += max_score
                max_score -= 1
                m += 1
        
    elif answer.lower() == "m":
        
        print("----- WELCOME TO THE MULTIPLE CHOICE SECTION -----")
        valid_data = False
        
        while not valid_data:
            answer = input("Enter Answers By Seperating ',' and Using Capital Letters :: ").split(",")
            is_valid = check_answer_number(answer)
            
            if is_valid:
                valid_data = True
            else:
                print("Try Again! Your Input Contradicts With Player Number")
                    
        hand += 1
        correct_answer = input("Enter The Correct Choice :: ").upper()
        max_score = len(players)
            
        for i in range(len(players)):
            if(answer[i] == correct_answer):
                scores[i] += max_score
            
    else:
        print("Check Your Input!!!")
       
                