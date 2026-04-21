CREATE TABLE machine_health_predictions (
    "Air temperature [K]" FLOAT,
    "Process temperature [K]" FLOAT,
    "Rotational speed [rpm]" FLOAT,
    "Torque [Nm]" FLOAT,
    "Tool wear [min]" FLOAT,
    "Temp_Diff" FLOAT,
    "Predicted_Failure" INTEGER,
    "Failure_Probability" FLOAT
);
COPY machine_health_predictions
FROM 'D:\akshat\Downloads\machine_health_predictions.csv' 
DELIMITER ',' 
CSV HEADER;

CREATE TABLE dataco (
    "Type" TEXT,
    "Days for shipping (real)" INTEGER,
    "Days for shipment (scheduled)" INTEGER,
    "Benefit per order" FLOAT,
    "Sales per customer" FLOAT,
    "Delivery Status" TEXT,
    "Late_delivery_risk" INTEGER,
    "Category Id" INTEGER,
    "Category Name" TEXT,
    "Customer City" TEXT,
    "Customer Country" TEXT,
    "Customer Email" TEXT,
    "Customer Fname" TEXT,
    "Customer Id" INTEGER,
    "Customer Lname" TEXT,
    "Customer Password" TEXT,
    "Customer Segment" TEXT,
    "Customer State" TEXT,
    "Customer Street" TEXT,
    "Customer Zipcode" FLOAT,
    "Department Id" INTEGER,
    "Department Name" TEXT,
    "Latitude" FLOAT,
    "Longitude" FLOAT,
    "Market" TEXT,
    "Order City" TEXT,
    "Order Country" TEXT,
    "Order Customer Id" INTEGER,
    "order date (DateOrders)" TEXT,
    "Order Id" INTEGER,
    "Order Item Cardprod Id" INTEGER,
    "Order Item Discount" FLOAT,
    "Order Item Discount Rate" FLOAT,
    "Order Item Id" INTEGER,
    "Order Item Product Price" FLOAT,
    "Order Item Profit Ratio" FLOAT,
    "Order Item Quantity" INTEGER,
    "Sales" FLOAT,
    "Order Item Total" FLOAT,
    "Order Profit Per Order" FLOAT,
    "Order Region" TEXT,
    "Order State" TEXT,
    "Order Status" TEXT,
    "Order Zipcode" FLOAT,
    "Product Card Id" INTEGER,
    "Product Category Id" INTEGER,
    "Product Description" FLOAT,
    "Product Image" TEXT,
    "Product Name" TEXT,
    "Product Price" FLOAT,
    "Product Status" INTEGER,
    "shipping date (DateOrders)" TEXT,
    "Shipping Mode" TEXT
);

copy dataco FROM 'D:\akshat\Downloads\dataco.csv' DELIMITER ',' CSV HEADER ENCODING 'WIN1252';
ALTER TABLE machine_health_predictions ADD COLUMN "Machine_ID" SERIAL;


CREATE VIEW vw_SupplyChain_Risk_Assessment AS
SELECT 
    mp."Machine_ID",
    mp."Predicted_Failure",
    mp."Failure_Probability",
    sco."Order Id",
    sco."Product Name",
    sco."Order Item Total" AS "Revenue_At_Risk",
    sco."Shipping Mode",
    CASE 
        WHEN mp."Predicted_Failure" = 1 THEN (sco."Order Item Total" * 0.15)
        ELSE 0 
    END AS "Estimated_Penalty_Cost"
FROM 
    machine_health_predictions mp
JOIN 
    dataco sco ON MOD(sco."Order Id", 5) = MOD(mp."Machine_ID", 5);



copy (SELECT * FROM vw_SupplyChain_Risk_Assessment) TO 'D:\akshat\Downloads/Final_Dashboard_Data.csv' WITH CSV HEADER;

