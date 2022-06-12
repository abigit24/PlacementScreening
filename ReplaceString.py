def replaceString():
    with open("example.txt", "r+") as f:
        data = "".join(f.readlines())
        modifiedStr = data.replace("placement", "screening")
        f.seek(0)
        f.truncate()
        f.write(modifiedStr)

replaceString()
