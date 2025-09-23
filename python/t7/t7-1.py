failed_logins = 2

if failed_logins == 0:
    print("No failed logins")
elif failed_logins < 5:
    print("Warning: some failed login")
else: 
    print("Account locked")