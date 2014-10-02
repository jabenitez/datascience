create view mytable as select * from Frequency where term == 'washington' or term == 'taxes' or term == 'treasury';


create view mybusqueda as
SELECT * FROM mytable
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;


create view mybusquedaT as
select docid as term , term as docid , count from mybusqueda;

create view mymultiplica as 
select mybusqueda.docid as term , mybusquedaT.term as  docid , sum (mybusqueda.count * mybusquedaT.count) as count 
from mybusqueda, mybusquedaT where mybusqueda.term == mybusquedaT.docid group by mybusqueda.docid , mybusquedaT.term;

select * from myminimultiplica where docid == "q";
