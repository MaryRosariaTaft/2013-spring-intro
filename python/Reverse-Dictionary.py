
def reverseD(dict):
    ans = {}
    for key in dict.keys():
        if dict[key] not in ans.keys():
            ans[dict[key]] = [key]
        else:
            ans[dict[key]].append(key)
    return ans




d = {"cat": 3, "dog":5, "cow":3, "frog": 3, "moose":1, "bird":5}
print "dictionary: " , d
print "reverse dict: ", reverseD(d)
