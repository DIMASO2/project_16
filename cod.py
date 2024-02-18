try:
    a=float(input())
    print(10/a)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("aaaaaa")
else:
    print("хорошо")
finally:
    print("норм")