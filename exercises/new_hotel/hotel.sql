
 
 CREATE TABLE Person (
    id int NOT NULL AUTO_INCREMENT,
    last_name varchar(255)  NOT NULL,
    first_name varchar(255)  NOT NULL,
    address varchar(255),
    ssn varchar(255)  NOT NULL,
    driver_license varchar(255),
    PRIMARY KEY (id)
);


 CREATE TABLE Guest (
    id int NOT NULL AUTO_INCREMENT,
    person_id int NOT NULL,
    check_in datetime  NOT NULL,
    check_out datetime,
    room_id int NOT NULL,
    PRIMARY KEY (id)
);

 CREATE TABLE Room (
    id int NOT NULL AUTO_INCREMENT,
    room_type varchar(255)  NOT NULL,
    total int NOT NULL,
    room_price int NOT NULL,
    PRIMARY KEY (id)
);

insert into Room(room_type,total,room_price)
values("single",10, 30),("double",20, 50), ("suite",5, 100)