use foodChoice;
create table vegetarian(
	id int not null auto_increment primary key,
    dish_name varchar (30),
    website varchar (50)
);
create table chicken(
	id int not null auto_increment primary key,
    dish_name varchar (30),
    website varchar (50)
);
create table pork(
	id int not null auto_increment primary key,
    dish_name varchar (30),
    website varchar (50)
);
create table beef(
	id int not null auto_increment primary key,
    dish_name varchar (30),
    website varchar (50)
);
create table fish(
	id int not null auto_increment primary key,
    dish_name varchar (30),
    website varchar (50)
);