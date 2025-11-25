role = "guest"

if role == "admin":
    print("Full access granted")
elif role == "editor":
    print("Partial access granted")
elif role == "guest":
    print("Read-only access")
else: 
    print("Access_denied")