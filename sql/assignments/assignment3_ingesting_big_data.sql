CREATE DATABASE eCommerce;

USE eCommerce;

CREATE TABLE EventLogs (
    event_time DATETIME NOT NULL,
    event_type NVARCHAR(50) NOT NULL,
    product_id BIGINT NOT NULL,
    category_id BIGINT NOT NULL,
    category_code NVARCHAR(255), -- Nullable since it may contain NULL values
    brand NVARCHAR(100), -- Nullable since it may contain NULL values
    price DECIMAL(10, 2) NOT NULL,
    user_id BIGINT NOT NULL,
    user_session NVARCHAR(100) NOT NULL
);

-- 7m37s
BULK INSERT EventLogs
FROM '/data/2019-Oct.csv' -- Specify the file path
WITH (
    FIELDTERMINATOR = ',', -- Column delimiter (change if needed)
    ROWTERMINATOR = '\n', -- Row delimiter (use newline)
    FIRSTROW = 2, -- Skip header row if present
    BATCHSIZE = 50000 -- Batch size to manage memory use
);

select count(1) from EventLogs; -- 42 million rows
