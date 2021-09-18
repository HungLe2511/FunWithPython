import abc

#dictionary
my_dict = {"ID" : "123", "NAME" : "HungLe"}

#for key, value in my_dict.items():
#    print(f"{key} : {value}")

def sum( *args, **kwargs ):
    tong = 0
    for i in args:
        tong += i
    return tong

print(sum( 1, 2, 3, 454))

a = (123, "hungle")
print(type(a))