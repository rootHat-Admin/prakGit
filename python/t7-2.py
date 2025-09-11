port = 23

if port == 22:
    print("SSH service detected")
elif port == 80:
    print("HTTP service detected")
elif port == 443:
    print("HTTPS servise detected")
else:
    print("Unknown service")