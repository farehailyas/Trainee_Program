def safe_cast(value , target_value):
    try:
        if target_value == "int":
            res = int(value)
        elif target_value == "float":
            res = float(value)
        elif target_value == "bool":
            res = bool(value)
        elif target_value == "str":
            res = str(value)
        return res
    except ValueError:
        return None

print(safe_cast("42", "int"))
print(safe_cast("3.14", "float"))
print(safe_cast("hello", "int")) 
print(safe_cast(0, "bool"))