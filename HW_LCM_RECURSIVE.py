import time
def lcm_recursive(*args):   
    def lcm(x, y):
        lcm=0
        if x > y:
           higher = x
        else:
           higher = y    
        while True:
            if higher % x == 0 and higher % y == 0:
                lcm = higher
                break
            else:
                higher = higher +1 
        return lcm
    if len(args)==2:
        result =lcm(args[0],args[1])
        return result
    return lcm_recursive(args[0],lcm_recursive(*args[1:]))

print(lcm_recursive(2,5,8,51))

starttime = time.time()
print(starttime)
print(lcm_recursive(2,5,8,51))
stoptime = time.time()
print(stoptime)
print(stoptime-starttime)