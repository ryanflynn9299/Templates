-- A SQL script to instantiate/populate DB Tables
DROP TABLE IF EXISTS Example;

CREATE TABLE Example(
    Id int(11) PRIMARY KEY,
    Text varchar(255)
);

INSERT INTO Example(Id, Text)
VALUES (1, 'Hello World!');
