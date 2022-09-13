CREATE DATABASE reservas;

USE reservas;

CREATE TABLE users
(
    id int(255) AUTO_INCREMENT NOT NULL,
    role varchar(20),
    first_name varchar(255),
    lastname varchar(255),
    email varchar(255),
    password varchar(255),
    PRIMARY KEY(id)
)ENGINE=InnoDB;

CREATE TABLE fields
(
    id int(255) AUTO_INCREMENT NOT NULL,
    name varchar(255),
    capacity int,
    PRIMARY KEY(id)
)ENGINE=InnoDB;

CREATE TABLE reservations
(
    id int(255) AUTO_INCREMENT NOT NULL,
    user_id int(255) NOT NULL,
    field_id int(255) NOT NULL,
    start_at datetime,
    end_at datetime,
    PRIMARY KEY(id),
    CONSTRAINT fk_user_reservations FOREIGN KEY(user_id) REFERENCES users(id),
    CONSTRAINT fk_field_reservations FOREIGN KEY(field_id) REFERENCES fields(id)
)ENGINE=InnoDB;

CREATE TABLE anotations
(
    id int(255) AUTO_INCREMENT NOT NULL,
    reservation_id int(255) NOT NULL,
    team char(1) NOT NULL,
    full_name varchar(255) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_reservation_anotations FOREIGN KEY(reservation_id) REFERENCES reservations(id)
)ENGINE=InnoDB;

INSERT INTO users (role, first_name, lastname, email, password) VALUES ('admin','Admin','Reservas','reservas@admin.com','$2b$12$Dpg5dxjNryyc6MUBRLbHY.AqIY6.SS3yuqezZ8ppb/V1eLiXzSYAG')