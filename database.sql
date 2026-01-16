-- Simple Loyalty Assessment - Table 1 Data
-- This table was created by the candidate as the original table link was not accessible

CREATE TABLE IF NOT EXISTS table_1 (
    cell_name VARCHAR(10) PRIMARY KEY,
    value INTEGER NOT NULL
);

-- Insert sample data for cells A1 through A20
INSERT INTO table_1 (cell_name, value) VALUES
('A1', 150),
('A2', 230),
('A3', 89),
('A4', 420),
('A5', 175),
('A6', 310),
('A7', 45),
('A8', 267),
('A9', 188),
('A10', 95),
('A11', 342),
('A12', 56),
('A13', 198),
('A14', 401),
('A15', 540),
('A16', 77),
('A17', 289),
('A18', 125),
('A19', 463),
('A20', 214);

-- Create Table 2 structure for calculated results
CREATE TABLE IF NOT EXISTS table_2 (
    category VARCHAR(50) PRIMARY KEY,
    formula VARCHAR(100) NOT NULL,
    value REAL NOT NULL
);
