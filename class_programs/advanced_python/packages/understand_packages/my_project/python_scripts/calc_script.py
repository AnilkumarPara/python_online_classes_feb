# Absolute path

abs_path = 'D:\\calc\\'
import sys
print(sys.path)
sys.path.append(abs_path)
print(sys.path)
import calculator
print(calculator.add(2,3))
