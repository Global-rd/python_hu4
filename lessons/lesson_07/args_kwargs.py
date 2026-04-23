#*args

def calculate_total_price(*items):

    print(type(items))
    print(items)
    total = 0

    for _, price, quantity in items:
        total += price * quantity
    
    return total

total = calculate_total_price(
    ("Alma", 300, 2),
    ("Körte", 500, 3),
    ("Barack", 100, 4),
)

print(total)

#**KWARGS 

def describe_person(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}: {v}")

describe_person(name="Steve", height=189, country="Hungary", job="programmer")


#combining positial, default, args, kwargs
def introduce_person(name, age, *hobbies, country="Hungary", **additional_info):
    print(f"Name: {name}" )
    print(f"Age: {age}" )
    print(f"Country: {country}" )

    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"----{hobby}")

    if additional_info:
        print("Additional information")
        for k,v in additional_info.items():
            print(f"----- {k} --- {v}")


introduce_person("John",
                 15,
                 "hiking",
                 "cycling",
                 "reading",
                 country="Switzerland",
                 occupation="programmer",
                 is_active=True
                 )
