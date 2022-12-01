import psycopg2 as pg

def connection ():
    return pg.connect(
            database='web_arenas',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5433'
        )

def model_users():
    return """CREATE TABLE IF NOT EXISTS tb_users
    (
        id              serial,
        name            varchar(50),
        phone           varchar(16),
        email           varchar(50),
        document        varchar(11),
        password        varchar(20),
        city            varchar(4),
        superuser       bool,

        constraint pk_tb_users_id primary key(id),
        constraint fk_tb_users_city foreign key(city) references tb_city(id)
    );"""

def model_arenas():
    return """CREATE TABLE IF NOT EXISTS tb_arenas
    (
        id              serial,
        name            varchar(50),
        price           float8,
        category        varchar(20),
        city            varchar(4),

        constraint pk_tb_arenas_id primary key(id),
        constraint fk_tb_users_city foreign key(city) references tb_city(id)
    );"""

def model_city():
    return """CREATE TABLE IF NOT EXISTS tb_city
    (
        id              varchar(4),
        name            varchar(20),
        state           varchar(20),

        constraint pk_tb_city_id primary key(id)
    );"""

def model_arenas_ribeirao():
    return """CREATE TABLE IF NOT EXISTS tb_arenas_ribeirao
    (
        id              serial,
        name            varchar(50),

        constraint pk_tb_arenas_ribeirao_id primary key(id)
    );"""