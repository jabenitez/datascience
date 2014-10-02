create view miniM as
  select docid, term, count from Frequency where docid == "10080_txt_crude" or docid == "17035_txt_earn";

create view miniMT as
  select term as docid, docid as term, count from Frequency where docid == "10080_txt_crude" or docid == "17035_txt_earn";


create view myminimultiply as 
select miniM.docid as term , miniMT.term as  docid , sum (miniM.count * miniMT.count) as count 
from miniM, miniMT where miniM.term == miniMT.docid group by miniM.docid , miniMT.term;

select * from myminimultiply;

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
