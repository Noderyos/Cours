def main():
    red = '255 0 0 '
    white = '255 255 255 '
    black = '0 0 0 '
    print('La longeur doit etre 1.5 fois plus grande que la largeur')
    length = input('Longeur :')
    width = input('Largeur : ')
    
    left = 0
    right = int(width)-1
    print('P3')
    print(str(int(length)-1) + ' ' + width)
    print(255)
    for i in range(int(width)):

        print (left*red + 5*white + 20*black + 5*white + right*red)
        left += 1
        right -= 1






if __name__ == '__main__':
    main()