create table test (
	id int,
	name varchar(40),
	street varchar(50)
)


select * from test

insert into test (id, name, street) values (2, 'Panna', 'Y street')

update test set name = 'Laci' where id = 1

delete from test where id = 1