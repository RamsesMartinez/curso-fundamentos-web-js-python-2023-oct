-- leer información
select trackid, name, albumid, composer from track;
select * from album;  -- id 1 del album?

select trackid, name, albumid  from track
where albumid=150;

-- filtrar datos
select * from track where composer = 'roy z';

-- ordenar
select * from track where composer = 'roy z'
order by name;
select * from track where composer = 'roy z'
order by name asc;
select * from track where composer = 'roy z'
order by name desc;

-- operadores: varias condiciones
select * from track where composer = 'roy z';
select * from track where track.composer = 'chuck berry';

-- or
select * from track 
where composer = 'roy z' or
	composer = 'chuck berry'or
	composer = 'jorge ben'
order by composer, name asc;

-- and 
-- '%'
select * from track 
where name like 'a%' and 
	genreid = 1 and
	milliseconds < 200000
order by composer, name asc;


--- not
select * from album where albumid >= 10 and albumid <= 30;
select * from album where not albumid >= 10;
select * from album where not (albumid >= 10 and albumid <= 30);


-- count
select count(*) from track where genreid = 2;
select * from genre where genreid = 2;

-- insert
select * from track order by trackid desc;
insert into track(trackid, name, albumid, mediatypeid, milliseconds, unitprice)
values (3504, 'mi nueva canción', 241, 1, 250000, 1.49);

-- update
update track
set genreid = 2, composer  = 'ramses' 
where trackid = 3504;

select * from track where trackid = 3504;

