status = False
try:
    from snap import Version, TInt
    version = Version
    i = TInt(5)
    if i == 5:
        status = True
except:
    pass

if status:
    print ("SUCCESS, your version of Snap.py is %s" % (version))
else:
    print ("*** ERROR, no working Snap.py was found on your computer")