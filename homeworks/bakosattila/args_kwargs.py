

# combine
def introduce_person(name, age, *hobbies, country="Hungary", **additional_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")

    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
    if additional_info:
        print("Additional Information:")
        for key, value in additional_info.items():
            print(f"{key}: {value}")

introduce_person("John",
                30,
                "Reading",
                "Traveling",
                "Cooking",
                Country="USA",
                occupation="Engineer",
                marital_status="Single",
                is_active=True
                 )
