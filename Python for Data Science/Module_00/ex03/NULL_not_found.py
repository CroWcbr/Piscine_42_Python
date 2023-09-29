def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: " + str(object) + " " + str(type(object)))
    elif isinstance(object, float):
        print("Cheese: " + str(object) + " " + str(type(object)))
    elif isinstance(object, bool):
        print("Fake: " + str(object) + " " + str(type(object)))
    elif isinstance(object, int):
        print("Zero: " + str(object) + " " + str(type(object)))
    elif isinstance(object, str) and len(object) == 0:
        print("Empty: " + str(object) + " " + str(type(object)))
    else:
        print("Type not found")
        return 1
    return 0
