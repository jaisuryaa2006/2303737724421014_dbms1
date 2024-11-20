CREATE DATABASE event_db;

USE event_db;

CREATE TABLE eventdetails (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    location VARCHAR(255) NOT NULL
);
INSERT INTO eventdetails (id, name, date, location) 
VALUES 
    ('EVT001', 'Tech Conference 2024', '2024-05-14', 'San Francisco'),
    ('EVT002', 'Music Fest', '2024-06-20', 'New York'),
    ('EVT003', 'Art Exhibition', '2024-07-05', 'Los Angeles'),
    ('EVT004', 'Business Summit', '2024-08-12', 'Chicago');
select * from eventdetails;