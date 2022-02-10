def find_needle(haystack):
    array=[haystack]
    x=-1
    i=''
    for i in array:
        for j in i:
            x+=1
            if j=='needle':
                return('found the needle at position '+str(x))
