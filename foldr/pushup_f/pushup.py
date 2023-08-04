from /pullup_f import pullup

def read_total_pushups_from_file():
    try:
        with open("total_pushups.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist, create it with an initial value of 0
        write_total_pushups_to_file(0)
        return 0
    except ValueError:
        # If the file contains a non-integer value, reset it to 0
        write_total_pushups_to_file(0)
        return 0

def write_total_pushups_to_file(totalPushUpsToday_sum):
    try:
        with open("total_pushups.txt", "w") as file:
            file.write(str(totalPushUpsToday_sum))
    except Exception as e:
        print("Error while writing to the file:", e)

def read_total_pushups_like_from_file():
    try:
        with open("total_pushups_like.txt", "r") as file_like:
            return [int(num) for num in file_like.read().split()]
    except FileNotFoundError:
        # If the file doesn't exist, create it with an empty list
        write_total_pushups_like_to_file([])
        return []
    except ValueError:
        # If the file contains invalid numbers, reset it to an empty list
        write_total_pushups_like_to_file([])
        return []

def write_total_pushups_like_to_file(totalPushUpsToday_list):
    try:
        with open("total_pushups_like.txt", "w") as file_like:
            file_like.write(' '.join(map(str, totalPushUpsToday_list)))
    except Exception as e:
        print("Error while writing to the file:", e)

totalPushUpsToday_sum = read_total_pushups_from_file()
totalPushUpsToday_list = read_total_pushups_like_from_file()

def xamp():
    pushUpsNow = input("how many push-ups did you do rn? (write number) \n type 'c' to continue or 'e' to exit \n")
    try:
        pushUpsNow = int(pushUpsNow)
        print("You did:", pushUpsNow, "pushups, gj!")
        return pushUpsNow
    except ValueError:
        if pushUpsNow.lower() == 'c':
            return None
        elif pushUpsNow.lower() == 'e':
            raise SystemExit("Exiting the program.")
        else:
            raise ValueError("Type either a number \n type 'c' to continue or 'e' to exit.")

functionReturnV = xamp()
if functionReturnV is not None:
    totalPushUpsToday_sum += functionReturnV
    totalPushUpsToday_list.append(functionReturnV)

def true():
    global totalPushUpsToday_sum, totalPushUpsToday_list
    
    while True:
        print("You have done push-ups today like:", totalPushUpsToday_list)
        print("Total push-ups today:", totalPushUpsToday_sum)
        continue_or_exit = input(
        '''
Do you want to add more push-ups? write 'y'  
write 'n' to exit 
write 'reset' to reset the counter for today 
write 'pop' to delete the last insertion 
write 'pull' to switch to pull-ups 
write 'sit' to switch to sit-ups 
type here:
        ''')
        
        if continue_or_exit.lower() == 'n':
            break
        elif continue_or_exit.lower() == 'y':
            functionReturnV = xamp()
            if functionReturnV is not None:
                totalPushUpsToday_sum += functionReturnV
                totalPushUpsToday_list.append(functionReturnV)
        elif continue_or_exit.lower() == 'pull':
            pull_up.pull_up_func()  
        elif continue_or_exit.lower() == 'reset':
            totalPushUpsToday_sum = 0
            totalPushUpsToday_list = []
            write_total_pushups_to_file(totalPushUpsToday_sum)
            write_total_pushups_like_to_file(totalPushUpsToday_list)
            print(totalPushUpsToday_sum)
            print(totalPushUpsToday_list)
        elif continue_or_exit.lower() == 'pop':
            if totalPushUpsToday_list:
                last_pushup_count = totalPushUpsToday_list.pop()
                totalPushUpsToday_sum -= last_pushup_count
                write_total_pushups_to_file(totalPushUpsToday_sum)
                write_total_pushups_like_to_file(totalPushUpsToday_list)
            else:
                print("There are no entries to pop.")
            print(totalPushUpsToday_sum)
            print(totalPushUpsToday_list)
        else:
            pass
    
    # Remove all occurrences of 0 from the list
    totalPushUpsToday_list = [x for x in totalPushUpsToday_list if x != 0]


# Write the totalPushUpsToday_sum to total_pushups.txt
write_total_pushups_to_file(totalPushUpsToday_sum)

# Write the totalPushUpsToday_list to total_pushups_like.txt
write_total_pushups_like_to_file(totalPushUpsToday_list)

true()
