user=None

if user is not None and user.access == "admin":
    print("acces done")

else:
    
    raise AttributeError("crashhhhhh")