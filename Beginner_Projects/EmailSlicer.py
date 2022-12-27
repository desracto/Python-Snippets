def slice_email(email:str):
    split = email.split("@")
    return {"username": split[0],
            "domain": split[1]}

if __name__ == "__main__":
    split_email = slice_email("mohammed@gmail.com")
    print(split_email["username"])
    print(split_email["domain"])