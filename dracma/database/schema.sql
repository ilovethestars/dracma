CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME,
    product VARCHAR(255),
    brand VARCHAR(255),
    quantity FLOAT,
    unit VARCHAR(50),
    isbn VARCHAR(20),
    price_local DECIMAL(20, 8),
    price_standard DECIMAL(20, 8),
    total_local DECIMAL(20, 8),
    total_standard DECIMAL(20, 8),
    unit_price_local DECIMAL(20, 8),
    unit_price_standard DECIMAL(20, 8),
    account VARCHAR(255),
    location VARCHAR(255),
    country VARCHAR(100),
    currency VARCHAR(10)
)