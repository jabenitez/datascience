drop view mymatrix;
create view mymatrix as 
select a.row_num as col , b.col_num as row, sum(a.value*b.value) as myval 
from a, b where a.col_num == b.row_num group by a.row_num , b.col_num;

select myval from mymatrix where col == 2 and row ==3;
--select a.row_num, b.col_num, sum(a.value*b.value) from a, b
 -- where a.row_num == 2 and b.col_num == 3 and a.col_num == b.row_num;

-- That's it!  Join columns to rows, group by rows and columns, then filter to get the cell you want.

--select a.value, a.row_num , b.value, b.col_num from a
--where a.col_num == 2 and b.row_num == 3

--select value, col_num from b
--where row_num == 3
