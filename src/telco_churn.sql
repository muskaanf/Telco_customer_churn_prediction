CREATE DATABASE telco_churn;
USE telco_churn;
CREATE TABLE Processed (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    TotalCharges DECIMAL(10, 2),
    MonthlyCharges DECIMAL(10, 2),
    Tenure INT,
    Contract INT,
    PaymentMethod INT,
    OnlineSecurity INT,
    TechSupport INT,
    Gender INT,
    OnlineBackup INT,
    InternetService INT,    
    PaperlessBilling INT
);
CREATE TABLE Customers (
CustomerID VARCHAR(50) PRIMARY KEY,
    Tenure INT,
    Contract INT,
    Gender INT
);

CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID VARCHAR(50),
    OnlineSecurity INT,
    TechSupport INT,
    OnlineBackup INT,
    InternetService INT,    
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID VARCHAR(50),
    TotalCharges DECIMAL(10, 2),
    MonthlyCharges DECIMAL(10, 2),
    PaymentMethod INT,
    PaperlessBilling INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE ChurnPredictions (
    PredictionID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID VARCHAR(50),
    actual INT,
    Predicted INT,
    prediction_probability DECIMAL(10, 6),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

LOAD DATA LOCAL INFILE 'E:\\Muskaan\\work\\10Pearls\\telcoProject\\processed_data.csv'
INTO TABLE Processed
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(TotalCharges, MonthlyCharges, Tenure, Contract, PaymentMethod, OnlineSecurity, TechSupport, Gender, OnlineBackup, InternetService, PaperlessBilling);

LOAD DATA INFILE 'E:\\Muskaan\\work\\10Pearls\\telcoProject\\processed_data.csv'
INTO TABLE Processed
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'E:/Muskaan/work/10Pearls/telcoProject/prediction_results.csv'
INTO TABLE ChurnPredictions
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(CustomerID, actual, Predicted, prediction_probability);