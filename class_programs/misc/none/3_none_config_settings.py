config = {
    "debug_mode": "enabled",
    "max_items": 50,
    "theme": "light"
}

if config["debug_mode"] is None:
    print("Debug mode is not enabled.")
else:
    print("Debug mode is enabled.")

"""
In configuring applications, None can represent the 
absence of a value or feature not being enabled.
"""