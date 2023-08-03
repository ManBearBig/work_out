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
            return 0
        elif pushUpsNow.lower() == 'e':
            raise SystemExit("Exiting the program.")
        else:
            raise ValueError("Type either a number \n type 'c' to continue or 'e' to exit.")

while True:
    functionReturnV = xamp()
    totalPushUpsToday_sum += functionReturnV
    totalPushUpsToday_list.append(functionReturnV)

    continue_or_exit = input("Do you want to add more push-ups? (y/n) \n press ENTER to see sum \n write 'pull' to switch to pull-ups \n write 'sit' to switch to sit-ups ")
    if continue_or_exit.lower() != "y":
        break

# Write the totalPushUpsToday_sum to total_pushups.txt
write_total_pushups_to_file(totalPushUpsToday_sum)

# Write the totalPushUpsToday_list to total_pushups_like.txt
write_total_pushups_like_to_file(totalPushUpsToday_list)

print("You have done push-ups today like:", totalPushUpsToday_list)
print("Total push-ups today:", totalPushUpsToday_sum)
