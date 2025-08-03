import dracma
import database

import json


def save_config(user_name: str, main_currency: str, db_config: dict) -> None:
    config = {
        "user_name": user_name,
        "main_currency": main_currency,
        "db_config": db_config
    }
    with open("config.json", "w") as file:
        json.dump(config, file, ident=4)


def first_initialization() -> None:
    print("Hey, you! You finally awake...")
    
    initialization()
    user_name = input("How do you want to be called?\n>")
    main_currency = input("What's you preferred currency? [ISO]\n>")
    
    # Write to the config file:
    db_config = {
        "host": "localhost",
        "port": 3306,    
        "user": "dracma_user",
        "password": "senha_segura",
        "database": "dracma_db"
    }
    save_config(user_name, main_currency, db_config)

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
            print("Enter transaction details:")

            from datetime import datetime
            date = datetime.strptime(
                input("Date [YYYY-MM-DD HH:MM:SS]: "),
                "%Y-%m-%d %H:%M:%S"
            )

            product = input("Product: ")
            brand = input("Brand: ")
            quantity = float(input("Quantity: "))
            ammount = float(input("Ammount: "))
            UPC = input("UPC/ISBN: ")
            price_local = float(input("Price (local currency): "))
            price_standard = float(input("Price (standard currency): "))
            total_local = float(input("Total (local currency): "))
            total_standard = float(input("Total (standard currency): "))
            unit_price_local = float(input("Unit price (local currency): "))
            unit_price_standard = float(input("Unit price (standard currency): "))
            account = input("Account debited: ")
            location = input("Location of purchase: ")
            country = input("Country: ")
            currency = input("Currency used (ISO): ")

            database.add_transaction(
                date,
                product,
                brand,
                quantity,
                ammount,
                UPC,
                price_local,
                price_standard,
                total_local,
                total_standard,
                unit_price_local,
                unit_price_standard,
                account,
                location,
                country,
                currency
            )

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