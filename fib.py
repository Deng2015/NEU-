def fibs(num):
    result = [0,1]
    for i in range (num-2):
        result.append(result[-2] + result[-1])
    return result
number = input("please input one number: ")
number = int(number)
print(fibs(number))
