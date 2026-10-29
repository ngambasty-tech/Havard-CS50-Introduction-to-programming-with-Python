import sys

#print(sys.argv[0]) #name of the file is stored at position [0]


# try:
#     print(sys.argv[1])
# except IndexError:
#     print("No argument provided. Please provide a name as an argument.")

'''
if len(sys.argv) < 2:
    # print("argument not provided")
    sys.exit("argument not provided")

elif len(sys.argv) > 2:
    # print("too many arguments provided")
    sys.exit("too many arguments provided")

print(sys.argv[1])
'''

#slices

# for arg in sys.argv:
#     print(arg)

# for arg in sys.argv[1:]:
#     print(arg)

for arg in sys.argv[1:3]:
    print(arg)