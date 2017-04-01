def func(a,b):
    print(a/b)
#this will give you a Zero division Error, excpetion occurs so print not called actually
#func(20,0)

print("Hello")

#Exception Handling
try:
    func(20,3)
    func(20,0)
except Exception:
    print("this is Division by Zero")
finally:
    print("This will definitely be printed always")