def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f"Nothing: {object} {type(object)}")
        elif isinstance(object, float) and str(object) == 'nan':
            print(f"Cheese: {object} {type(object)}")
        elif isinstance(object, str) and not object:
            print(f"Empty: {object} {type(object)}")
        elif isinstance(object, bool) and not object:
            print(f"Fake: {object} {type(object)}")
        elif isinstance(object, int) and not object:
            print(f"Zero: {object} {type(object)}")
        else:
            print("Type not found")
            return 1
        return 0
    except Exception:
        return 1
