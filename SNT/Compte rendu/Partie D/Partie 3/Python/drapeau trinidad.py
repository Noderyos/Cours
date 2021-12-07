def main():
    red = '255 0 0 '
    white = '255 255 255 '
    black = '0 0 0 '
    left = 0
    right = 59
    print('P3')
    print('89 60')
    print(255)
    for i in range(60):

        print (left*red + 5*white + 20*black + 5*white + right*red)
        left += 1
        right -= 1






if __name__ == '__main__':
    main()