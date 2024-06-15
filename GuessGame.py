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

# Prints the items in a unique way
def print_items(arr):
    for item in arr:
        print(item, end=" ")
    print()
    
# Sorts the players list according to the scores that players get and print the players from last to first
def print_winner():
    
    bubble_sort(scores, players)  
    scores.reverse()
    players.reverse()
    for i in range(len(players)-1, -1, -1):
        print(str(i+1) + ". " + players[i] + " ( " + str(scores[i]) + " )")