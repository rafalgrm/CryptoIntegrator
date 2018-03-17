drop table if exists cryptocurrencies;
create table cryptocurrencies (
  id integer PRIMARY KEY AUTOINCREMENT,
  name text not null
);