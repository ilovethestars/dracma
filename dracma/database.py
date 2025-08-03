import mariadb
import datetime


def load_config() -> dict:
    import json
    with open("config.json", "r") as f:
        return json.load(f)


def connect_db() -> mariadb.connections.Connection:
    config = load_config()["db_config"]
    return mariadb.connect(
        user=config["user"],
        password=config["password"],
        host=config["host"],
        port=config["port"],
        database=config["database"]
    )


def add_transaction(
    date: datetime.datetime,
    product: str,
    brand: str,
    quantity: float,
    ammount: float,
    UPC: str,
    price_local: float,
    price_standard: float,
    total_local: float,
    total_standard: float,
    unit_price_local: float,
    unit_price_standard: float,
    account: str,
    location: str,
    country: str,
    currency: str
) -> None:
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO transactions (
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
            VALUES (
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?
            )
            """,
            (
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
        )
        connection.commit()
        print("Transaction added with success!")

    except mariadb.Error as error:
        print("Maria error... Poor Shadow!")
        print(error)
    
    finally:
        cursor.close()
        connection.close()
