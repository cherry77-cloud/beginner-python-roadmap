id1, num1, val1 = map(float, input().split())
id2, num2, val2 = map(float, input().split())

print("VALOR A PAGAR: R$ %.2f" %(num1 * val1 + num2 * val2))
