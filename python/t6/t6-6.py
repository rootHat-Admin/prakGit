# users database (dict)
users = {
    "admin": {"password": "12345", "role": "superuser"},
    "guest": {"password": "guest", "role": "real-only"}
}

# server configuration (dict)
server_config = {
    "ip": "192.168.0.1",
    "port": 445,
    "ssl_enabled": True
} 

# log entry (dict)
log_entry = {
    "user": "admin",
    "action": "login",
    "time": "12:30",
    "status": "success"
}

print(users)