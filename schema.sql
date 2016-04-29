DROP TABLE IF EXISTS sale_ski_pack;
DROP TABLE IF EXISTS sale_lift_card;
DROP TABLE IF EXISTS ski_packs;
DROP TABLE IF EXISTS lift_cards;
DROP TABLE IF EXISTS users;

CREATE TABLE ski_packs (
  title       TEXT PRIMARY KEY NOT NULL,
  description TEXT             NOT NULL,
  price_hour  DOUBLE           NOT NULL,
  price_day   DOUBLE           NOT NULL,
  price_week  DOUBLE           NOT NULL
);

CREATE TABLE lift_cards (
  time_period TEXT PRIMARY KEY NOT NULL,
  price_child DOUBLE           NOT NULL,
  price_adult DOUBLE           NOT NULL
);

CREATE TABLE users (
  email         TEXT PRIMARY KEY,
  phone         TEXT    NOT NULL,
  password_hash TEXT    NOT NULL,
  joined        DATE    NOT NULL,
  privilege     INTEGER NOT NULL -- 0:user 1:rabatt-mann 2:admin 3:superadmin
);

CREATE TABLE sale_ski_pack (
  date        DATE    NOT NULL,
  ski_pack_title INTEGER NOT NULL,
  user_email  TEXT    NOT NULL,
  FOREIGN KEY (ski_pack_title) REFERENCES ski_packs (title),
  FOREIGN KEY (user_email) REFERENCES users (email),
  PRIMARY KEY (ski_pack_title, user_email)
);

CREATE TABLE sale_lift_card (
  date         DATE    NOT NULL,
  lift_card_time_period INTEGER NOT NULL,
  user_email   TEXT    NOT NULL,
  FOREIGN KEY (lift_card_time_period) REFERENCES lift_cards (time_period),
  FOREIGN KEY (user_email) REFERENCES users (email),
  PRIMARY KEY (lift_card_time_period, user_email)
);