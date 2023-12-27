CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE Drugs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE Applications (
    id SERIAL PRIMARY KEY,
    application_number INT NOT NULL,
    date_added DATE NOT NULL,
    drug_id INT,
    customer_data TEXT,
    status VARCHAR(50) NOT NULL,
    -- Add other fields as needed
    FOREIGN KEY (drug_id) REFERENCES Drugs(id)
);
