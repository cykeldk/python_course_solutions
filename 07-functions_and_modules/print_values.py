
def printv(vals, start=0):
    if start >= len(vals):
        return
    print(vals[start])
    printv(vals, start+1)

to_print = ['one', 'two', 'three']
printv(to_print)
