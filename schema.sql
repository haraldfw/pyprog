DROP TABLE IF EXISTS ski_packs;
DROP TABLE IF EXISTS users;

CREATE TABLE ski_packs (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  title       TEXT   NOT NULL,
  description TEXT   NOT NULL,
  price_hour  DOUBLE NOT NULL,
  price_day   DOUBLE NOT NULL,
  price_week  DOUBLE NOT NULL
);

CREATE TABLE lift_cards (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  price_child_day    DOUBLE NOT NULL,
  price_child_week   DOUBLE NOT NULL,
  price_child_season DOUBLE NOT NULL,
  price_adult_day    DOUBLE NOT NULL,
  price_adult_week   DOUBLE NOT NULL,
  price_adult_season DOUBLE NOT NULL
);

CREATE TABLE users (
  email         TEXT PRIMARY KEY,
  username      TEXT NOT NULL,
  name_first    TEXT NOT NULL,
  name_sur      TEXT NOT NULL,
  password_hash TEXT NOT NULL
);

CREATE TABLE sale_ski_pack (
  date        DATE    NOT NULL,
  ski_pack_id INTEGER NOT NULL,
  FOREIGN KEY (ski_pack_id) REFERENCES ski_packs (id),
  user_email  TEXT    NOT NULL,
  FOREIGN KEY (user_email) REFERENCES users (email),
  PRIMARY KEY (ski_pack_id, user_email)
);

CREATE TABLE sale_lift_card (
  date         DATE    NOT NULL,
  lift_card_id INTEGER NOT NULL,
  user_email   TEXT    NOT NULL,
  FOREIGN KEY (lift_card_id) REFERENCES lift_cards (id),
  FOREIGN KEY (user_email) REFERENCES users (email),
  PRIMARY KEY (lift_card_id, user_email)
);