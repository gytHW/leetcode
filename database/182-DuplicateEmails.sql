#需注意的就是where中不能使用聚合函数
select Email from Person group by Email having count(Email) >= 2;