from calculator import add, sub, multiply, divide, power, square

# Test cases for calculator functions 

def main():
    # test cases for addition 
    print("\nTest 1: Addition")
    print("Add two integers (135 + 100)")
    nums = add(135,100)
    if nums == 235: 
        print("Answer is 235. Test passed")
    else:
        print(f"Test failed, answer was {nums}")

    print("\nAdd two negative integers (-75 + -18)")
    nums = add(-75,-18)
    if nums == -93: 
        print("Answer is -93. Test passed")
    else:
        print(f"Test failed, answer was {nums}")

    # test cases for subtraction 
    print("\nTest Case 2: Subtraction")
    print("Subtract two integers (135 - 100)")
    nums = sub(135,100)
    if nums == 35: 
        print("Answer is 35. Test passed")
    else:
        print(f"Test failed, answer was {nums}")
    
    print("\nSubtract two negative integers (-75 - (-18))")
    nums = sub(-75,-18)
    if nums == -57: 
        print("Answer is -57. Test passed")
    else:
        print(f"Test failed, answer was {nums}")

    # test cases for multiplication 
    print("\nTest Case 3: Multiplication")
    print("Multiply two integers (100 * 400)")
    nums = multiply(100,400)
    if nums == 40000: 
        print("Answer is 40000. Test passed")
    else:
        print(f"Test failed, answer was {nums}")
    
    print("\nMultiply two negative integers (-75 * -18)")
    nums = multiply(-75,-18)
    if nums == 1350: 
        print("Answer is 1350. Test passed")
    else:
        print(f"Test failed, answer was {nums}")

    # test cases for division 
    print("\nTest Case 3: Division")
    print("Divide two integers (1000 / 25)")
    nums = divide(1000,25)
    if nums == 40: 
        print("Answer is 40. Test passed")
    else:
        print(f"Test failed, answer was {nums}")
    
    print("\nDivision two negative (-80 / -4)")
    nums = divide(-80,-4)
    if nums == 1350: 
        print("Answer is 20. Test passed")
    else:
        print(f"Test failed, answer was {nums}")

    # test cases for powers 
    print("\n Test Case 4: Powers")
    print("Integer to positive power (2 ** 2)")
    nums = power(2,2)
    if nums == 4: 
        print("Answer is 4. Test passed")
    else:
        print(f"Test failed, answer was {nums}")
    
    print("\nNegative integer to positive power (-3 ** 2)")
    nums = power(-3,2)
    if nums == -9:
        print("Answer is -9. Test passed")
    else:
        print(f"Test failed, answer was {nums}")

    # test case for square root 
    print("\n Test Case 5: Square root")
    print("Square root of Integer (16)")
    nums = square(16)
    if nums == 4: 
        print("Answer is 4. Test passed")
    else:
        print(f"Test failed, answer was {nums}")
    

if __name__ == "__main__":
    main()