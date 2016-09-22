def simplifyPath(path):
    path = list(filter(lambda x: x != "." and x != "", path.split("/")))
    res = []
    print(path)
    if not path:
        return "/"
    for i in path:
        print(res)
        if i == "..":
            if not len(res):
                continue
            else:
                res.pop()
        else:
            res.append(i)
    return "/"+"/".join(res)

print(simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))
