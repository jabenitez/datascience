create view myquery as
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;


create view myqueryT as
select docid as term , term as docid , count from myquery;

create view mymultiply as 
select myquery.docid as term , myqueryT.term as  docid , sum (myquery.count * myqueryT.count) as count 
from myquery, myqueryT where myquery.term == myqueryT.docid group by myquery.docid , myqueryT.term;

select * from myminimultiply where docid == "q";

/*drop view FrequencyT;
create view FrequencyT as
select docid as term , term as docid , count from Frequency;

create view mymultiply as 
select Frequency.docid as term , FrequencyT.term as  docid , sum(Frequency.count * FrequencyT.count) as count 
from Frequency, FrequencyT where Frequency.term == FrequencyT.docid group by Frequency.docid , FrequencyT.term;
*/
--select * from mymultiply;
--select a.row_num, b.col_num, sum(a.value*b.value) from a, b
 -- where a.row_num == 2 and b.col_num == 3 and a.col_num == b.row_num;

-- That's it!  Join columns to rows, group by rows and columns, then filter to get the cell you want.

--select a.value, a.row_num , b.value, b.col_num from a
--where a.col_num == 2 and b.row_num == 3

--select value, col_num from b
--where row_num == 3
