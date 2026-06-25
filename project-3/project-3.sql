Create database db;
use db;
create table orders(
	OrderID varchar(20),
    Date DATE,
    CustomerID varchar(20),
    Product Varchar(20),
    Quantity INT,
    UnitPrice DECIMAL(10.2),
    ShippingAddress varchar(20),
    PaymentMethod varchar(20),
    OrderStatus varchar(20),
    TrackingNumber varchar(20),
    ItemsInCart INT,
    CouponCode varchar(20),
    ReferralSource varchar(20),
    TotalPrice decimal(10.2)
    );
    
    select * from orders;
   select * from orders order by TotalPrice DESC;
   
   
   select count(*) as TotalOrders from orders;
   
   select count(*) as deliveredorders from orders where OrderStatus='Delivered';
   
   select sum(TotalPrice) as Revenue from orders;
   
   select Product, SUM(TotalPrice) as Revenue
   from orders group by Product;
   
   select avg(TotalPrice) as AvgOrderValue from orders;
   
   select Product ,count(*) as orders from orders group by Product;
   
   select PaymentMethod ,count(*) as orders from orders group by PaymentMethod;
   
   select OrderStatus ,count(*) as orders from orders group by OrderStatus;
   
   select Product, sum(TotalPrice) as Revenue From orders group by Product Order by Revenue DESC Limit 5;