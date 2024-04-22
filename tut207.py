# Try , Except : exception handling, python tutorial 207
# exception handling
# try except else finally


#exception are the errors that come during the execution time
# the line you think will face error, put it in try block

while True:
    try:

        age=int(input('enter your age:'))
        break
    except ValueError:
        print('you entered something other than number, please try again!')
    except:
        print('unexpected error...')


if age<18:
    print('You can\'t play this game.')

else:
    print('you can play this game.')







