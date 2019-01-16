from string import ascii_lowercase

input_file = open("input.txt", "r").read()

oldline = ""

while oldline != input_file:
    oldline = input_file
    for n in range(1, len(input_file)):
        if input_file[n] == input_file[n-1]:
            pass
        elif input_file[n].lower() == input_file[n-1].lower():
            input_file = input_file[:n] + input_file[n + 1:]
            input_file = input_file[:n - 1] + input_file[n:]
            break
   
print (len(input_file))


original_file = input_file
for i in ascii_lowercase:
    input_file = original_file
    input_file = input_file.replace(i, "")
    input_file = input_file.replace(i.upper(), "")
    
    oldline = ""
    
    while oldline != input_file:
        oldline = input_file
        for n in range(1, len(input_file)):
            if input_file[n] == input_file[n-1]:
                pass
            elif input_file[n].lower() == input_file[n-1].lower():
                input_file = input_file[:n] + input_file[n + 1:]
                input_file = input_file[:n - 1] + input_file[n:]
                break
        
    print (len(input_file))