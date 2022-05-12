import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    number = np.random.randint(1, 101)
    left =1
    right = 100
    count = 0
   
    while True:
        predict_number = (left+right)//2 # предполагаемое число
        count += 1
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number>predict_number:
            left = predict_number+1
        else:
            right = predict_number+1
        if count >7:
            if predict_number +1 == number:
                break
            if predict_number -1 == number:
                break
    return(count)

print(f'Количество попыток: {random_predict()}')
