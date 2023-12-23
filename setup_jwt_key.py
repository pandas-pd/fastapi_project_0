import secrets

def main():

    ui : int        = input("\nkey length (reccomended 64 character): ")

    try:
        ui = int(ui)
    except:
        quit("input must be an integer")



    key = secrets.token_urlsafe(ui)
    key = key[:ui]

    print(f"\ngenerated key:\n{key}")

if __name__ == "__main__":
    main()
