# FIXME: NOT FINISHED
def originalCase(org, new):
    result = ""
    if len(org) != len(new):
        return ("Not the same string")
        brake
    for i in range(len(new)):
        # check if a letter
        # look up which case it is in org
        # change case in new
        if org[i].isalpha():
            if org[i].isupper():
                new[i].upper()
                print(new[i])
        i += 1
    print(new)


originalCase("Hello world!", "hellO World!")
