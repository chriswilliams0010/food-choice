use foodChoice;
create table vegetarian(
	id int not null auto_increment primary key,
    dish_name varchar (100),
    website varchar (2083)
);
create table chicken(
	id int not null auto_increment primary key,
    dish_name varchar (100),
    website varchar (2083)
);
create table pork(
	id int not null auto_increment primary key,
    dish_name varchar (100),
    website varchar (2083)
);
create table beef(
	id int not null auto_increment primary key,
    dish_name varchar (100),
    website varchar (2083)
);
create table fish(
	id int not null auto_increment primary key,
    dish_name varchar (100),
    website varchar (2083)
);