import dracma
import database


def first_initialization() -> None:
    print("Hey, you! You finally awake...")
    
    initialization()
    print(
        "This is the first initialization of Dracma.\n"
        "Let's start with a few questions...\n"    
    )
    print("How do you want to be called?")
    user_name = input()

    print(
        "Cool name! Now the boring questions..."
        "What do you want to be your preferred currency? (use ISO format)"
    )
    main_currency = input()
    print("Is that even valuable? Cool, I guess...")

    # Write to the config file:
    ...

    return


def quote_of_the_day() -> None:
    print("\"This will be a feature someday...\"")
    print("---Josué Brito")
    # TODO create a quote of the day feature


def initialization() -> None:
    print("Dracma personal finance (CLI version 0.0.0)")
    print("Last updated: 2025-07-31\n")
    quote_of_the_day()
    print("\n")
    print("Tip: you can exit at any time by typing 'exit'.\n")

    return


def menu() -> None:
    print("Choose an option:")
    print(
        "1. Add to the database.\n"
        "2. View database.\n"
        "\n"
    )
    
    match input("Option: ").strip().lower():
        case "1":
            database.add_to_db()
        
        case "2":
            print("With the FUR?!")
        
        case "exit":
            dracma.terminate()

        case _:
            print("Bruh???")

    return


def start_application() -> None:
    initialization()
    menu()
    # TODO add mini-review of prefered investments
    
    return