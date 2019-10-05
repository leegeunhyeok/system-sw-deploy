def bmi(height, weight):
    height = height * 0.01
    bmi = weight / height ** 2
    print('BMI :', round(bmi, 2))

    if bmi < 18.5:
        print('마른 체형')
    elif 18.5 <= bmi < 25.0:
        print('정상')
    elif 25.0 <= bmi < 30.0:
        print('비만')
    else:
        print('고도비만')

height = float(input('키: '))
weight = float(input('몸무게: '))
bmi(height, weight)
