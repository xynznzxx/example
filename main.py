def Check_Number(number):
    country_code = number[0:2]
    if country_code == '+1':
        print(f'{number} | Valid')
        return True
    else:
        print(f'{number} | Invalid')
        return False

def Make_Call(number):
    print(f'Calling {number}...') #<-- This Means Its Been Checked


def SendOut_Information(): # <-- Gather Thread And Message Information
    thread_count = input('How Many Threads : ')
    messages = input('How Many Messages To Send : ')
    message_content = input('Message Content : ')
    return(thread_count,messages,message_content)


phone_number = input('Enter Phone Number : ')
checknumber = Check_Number(phone_number)
if checknumber == True:
    send_info = SendOut_Information()
    print(send_info[0])
    print(send_info[1])
    print(send_info[2])
    Make_Call(phone_number)
elif checknumber == False:
    print('Double Check the Phone Number Entered.. And Try Again')
else:
    print('An Error Has Occured')


