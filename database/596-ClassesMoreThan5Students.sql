#注意可能有重复记录，还有聚合函数不能在where子句中使用
select class from courses group by class having count(distinct(student)) >= 5