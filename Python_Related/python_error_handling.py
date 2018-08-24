#! /usr/local/bin/python3

ROOSTER = {
    "Adam": 90,
    "Bing": 91,
    "Charles": 83,
    "Danny": 78,
    "Elaine": 98,
    "Fannie": 70,
    "Gram": 89,
    "Haley": 73,
    "Issy": 87
}

def logError(msg):
    errmsg = "error logged: %s" %msg
    print(errmsg)
    raise Exception(errmsg)

def db_accessor(name):
    try:
        score = ROOSTER[name]
        print("got score: %s" %score)
        if score < 80:
            logError("too low")
        if score >= 90:
            logError("too high")
        if score > 80:
            raise ValueError("value error")
    except ValueError as e:
        print("got value error: %s" %repr(e))
        raise
    except Exception as e:
        print("what's error: %s" %repr(e))


def bus_logic(name):
    try:
        first = name[0]
        rest = name[1:]
        newName = first + rest.lower()
        return db_accessor(newName)
    except:
        raise Exception("Wrong name in bus_logic: %s" %name)


if __name__ == "__main__":
    try:
        # get Adam's score
        name0 = "ADAM"
        s0 = bus_logic(name0)
        # get Omar's score
        # name1 = "OMAR"
        # s1 = bus_logic(name1)
        # # get 3Q's score
        name2 = "Charles"
        s3 = bus_logic(name2)
    except Exception as e:
        print("in main: %s" %repr(e))
