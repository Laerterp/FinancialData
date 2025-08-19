-- Deleta a view caso já exista
DROP VIEW IF EXISTS vw_financial;

-- Cria a view com os nomes corretos das colunas
CREATE VIEW vw_financial AS
SELECT 
    f.TransactionID,
    f.CustomerID,
    f.Date,
    f.TransactionType,
    f.Amount,
    f.Discount,
    f.Tax,
    f.ShippingCost,
    f.Total,
    f.PaymentMethod,
    f.Status,
    f.Region,
    f.SourceDate,
    d.Age,
    d.Email
FROM fato_financial_data f
LEFT JOIN dim_customer_data d
    ON f.CustomerID = d.CustomerID
WHERE f.PaymentMethod IN ('Pix', 'Debit Card');
