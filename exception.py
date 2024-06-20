# myname='eMobilis'

# for i in myname:
#     if i=="k":
#         print(i)

jina=['banana','apple','mangoes']

for i in jina:
    print(i,jina[i])

try:
    # code that might raise exception
    result = 1/0
except ZeroDivisionError as e :
    # code to handle exception
    print(f"An error has occurred{e}")
finally:
    # code that runs nomatter what
    print("This will be printed")    