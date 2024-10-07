CREATE TABLE dockertest (
    ID SERIAL PRIMARY KEY,
    Email TEXT
);

INSERT INTO dockertest (Email) VALUES ('test@mail.com');
INSERT INTO dockertest (Email) VALUES ('perceval@mail.com');