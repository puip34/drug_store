INSERT INTO Users (username, password, email, role) VALUES
('admin', 'adminpass', 'admin@example.com', 'admin'),
('seller1', 'sellerpass1', 'seller1@example.com', 'seller'),
('seller2', 'sellerpass2', 'seller2@example.com', 'seller');

INSERT INTO Drugs (name, description) VALUES
('Drug A', 'Description for Drug A'),
('Drug B', 'Description for Drug B'),
('Drug C', 'Description for Drug C');

INSERT INTO Applications (application_number, date_added, drug_id, customer_data, status) VALUES
(1, '2023-01-01', 1, 'Customer data for Application 1', 'pending'),
(2, '2023-01-02', 2, 'Customer data for Application 2', 'completed'),
(3, '2023-01-03', 3, 'Customer data for Application 3', 'in_progress');
