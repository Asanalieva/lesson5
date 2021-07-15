try:
    int(input('INTEGER: '))

except ValueError:
    print('Введите корректный тип данныx')
except:
    print('Error')
finally:
    print('End')