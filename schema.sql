drop table if exists cryptocurrencies;
create table cryptocurrencies (
  id integer PRIMARY KEY AUTOINCREMENT,
  name text not null,
  abbreviation text not null
);
INSERT INTO cryptocurrencies (name, abbreviation) VALUES ('Bitcoin', 'XBT');
INSERT INTO cryptocurrencies (name, abbreviation) VALUES ('Ethereum', 'ETH');
INSERT INTO cryptocurrencies (name, abbreviation) VALUES ('Litecoin', 'LTC');

drop table if EXISTS enabled;
CREATE TABLE enabled(
  enabled_id integer PRIMARY KEY AUTOINCREMENT,
  enabled integer not null,
  crypto_id int,
  FOREIGN KEY (crypto_id) REFERENCES cryptocurrencies(id)
);
INSERT INTO enabled (enabled, crypto_id) VALUES (1, 1);
INSERT INTO enabled (enabled, crypto_id) VALUES (1, 2);
INSERT INTO enabled (enabled, crypto_id) VALUES (1, 3);