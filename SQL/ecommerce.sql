CREATE DATABASE OnlineShopping;

Use OnlineShopping;

CREATE TABLE Customer
(
	CustomerID int IDENTITY(1, 1) PRIMARY KEY,
	FirstName varchar(255) NOT NULL,
	LastName varchar(255) NOT NULL,
	DOB date NOT NULL,
	Email varchar(255) NOT NULL,
	Password varchar(255) NOT NULL,
	Contact varchar(255) NOT NULL
);

CREATE TABLE Country
(
	CountryID int IDENTITY(1, 1) PRIMARY KEY,
	CountryName varchar(255) NOT NULL
);

CREATE TABLE Province
(
	ProvinceID int IDENTITY(1, 1) PRIMARY KEY,
	ProvinceName varchar(255) NOT NULL
);

CREATE TABLE City
(
	CityID int IDENTITY(1, 1) PRIMARY KEY,
	CityName varchar(255) NOT NULL
);

CREATE TABLE ZipCode
(
	ZipCodeID int IDENTITY(1, 1) PRIMARY KEY,
	CityID int FOREIGN KEY REFERENCES City(CityID) NOT NULL,
	ProvinceID int FOREIGN KEY REFERENCES Province(ProvinceID) NOT NULL,
	CountryID int FOREIGN KEY REFERENCES Country(CountryID) NOT NULL
);

CREATE TABLE Address
(
	AddressID int IDENTITY(1, 1) PRIMARY KEY,
	HouseNo varchar(255) NOT NULL,
	Street int NOT NULL,
	CustomerID int FOREIGN KEY REFERENCES Customer(CustomerID) NOT NULL,
	ZipCodeID int FOREIGN KEY REFERENCES ZipCode(ZipCodeID) NOT NULL,
	Area varchar(255) NOT NULL
);
