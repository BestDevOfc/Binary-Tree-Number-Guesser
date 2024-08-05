import math


def legacy_binary_tree( target, list ):
    '''
    
    This binary tree is not good for Pico for 2 reasons:
    1) Have to store list -> takes up a lot of memory
    2) Modifies the actual original list
    
    '''
    my_list = list
    print(f"[ Target Number to Guess: {target} ]")
    while True:
        # gets the middle of the lenght value, but for the index we need to subtract by one (indexes start at 0)
        middle_index = math.floor( len(my_list) / 2 )-1

        # if middle_index with only on element = -1 and we do -1 -1 = -2, so we did not find the number even with only one element left
        if middle_index < -1:
            print(f"[ The number does not exist in this list ! ]")
            break

        
        ''' Could not get PWNTOOLS to compile on a M-Chip MAC >:( '''
        
        middle_number = my_list[middle_index]
        print(f"[ Try this number ]: {middle_number}")
        print("1) Too large")
        print("2) Too small")
        option = int(input("[+] ").strip().rstrip())
        

        if option == 1:
            my_list = my_list[ 0:middle_index ]
            print(f"[ Too Large, new list: {my_list} ]")
            continue
        if option == 2:
            # we're going one over bcs the middle is too small, so we'll skip and cut that half off
            my_list = my_list[ middle_index+1: ]
            print(f"[ Too Small, new list: {my_list} ]")
            continue

def legacy_main():
    my_list = range(0, 1_000)
    target = 100000
    legacy_binary_tree( target, my_list )


if __name__ == "__main__":
    legacy_main()