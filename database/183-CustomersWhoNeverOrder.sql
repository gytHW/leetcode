select Customers.Name as Customers from Customers left join Orders on Customers.Id = Orders.CustomerId
where Customers.Id not in (select CustomerId from Orders group by CustomerId)