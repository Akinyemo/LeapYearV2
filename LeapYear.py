
def calc_Leap(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print('Yes')
                return 'Yes'
            else:
                print('No')
                return 'No'    
        else:    
            print('Yes')
            return 'Yes'
    else:
        print('No')
        return 'No'    