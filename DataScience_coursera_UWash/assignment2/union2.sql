select count(*) from Frequency 
  where (docid == "10398_txt_earn" and count == 1) 
  or  (docid == "925_txt_trade" and count == 1);

