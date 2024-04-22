# Else finally with try except : Python tutorial 208



while True:
    try:

        age=int(input('enter your age:'))
        # print(f"user input = {age}")
        # break
    except ValueError:
        print(' please type integer')
    except:
        print('unexpected error... ')
        #else block runs when theres no any exception
    else:
        print(f'user inut = {age}')
        break

    #finally blocks run no matter exception occur or not
    finally:
        print('Final blocks running')






