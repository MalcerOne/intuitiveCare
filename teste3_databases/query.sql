CREATE TABLE mytable (
    column1 VARCHAR(255),
    column2 INT,
    column3 DOUBLE
);

-- Load the data from the CSV file into the table
LOAD DATA INFILE './files/relatorio_teste3.csv'
INTO TABLE mytable
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;