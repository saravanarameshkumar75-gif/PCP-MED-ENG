
def gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print("--- Calculating for 44 and 66 ---")
num1_set1 = 44
num2_set1 = 66
gcd_result_set1 = gcd(num1_set1, num2_set1)
lcm_result_set1 = lcm(num1_set1, num2_set1)
print(f"The GCD of {num1_set1} and {num2_set1} is: {gcd_result_set1}")
print(f"The LCM of {num1_set1} and {num2_set1} is: {lcm_result_set1}")

print("\n--- Calculating for 12 and 18 ---")
num1_set2 = 12
num2_set2 = 18
gcd_result_set2 = gcd(num1_set2, num2_set2)
lcm_result_set2 = lcm(num1_set2, num2_set2)
print(f"The GCD of {num1_set2} and {num2_set2} is: {gcd_result_set2}")
print(f"The LCM of {num1_set2} and {num2_set2} is: {lcm_result_set2}")