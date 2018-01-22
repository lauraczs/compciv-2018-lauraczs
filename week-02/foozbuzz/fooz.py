def fob(count):
    i = 1
    while i < (count+1):
        if i%3 ==0 and i%5 == 0:
            print (i, 'FoozBuzz')
        elif i%3 == 0:
            print (i , 'Fooz')
        elif i%5 == 0:
            print (i , 'Buzz')
        else:
            print (i)
        i = i + 1
