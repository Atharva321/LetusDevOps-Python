def split_and_join(line):
    # write your code here
    return ("-".join(line.split(" ")))
#Always remeber to use the joining char before the join function 
# and pass the string to join function 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)