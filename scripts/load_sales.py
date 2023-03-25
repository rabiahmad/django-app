from dashboard.models import Transaction
import csv

sale_column_mapping = {
    'Row ID': 'row_id',
    'Order ID': 'order_id',
    'Order Date': 'order_date',
    'Ship Date': 'ship_date',
    'Ship Mode': 'ship_mode',
    'Customer ID': 'customer_id',
    'Customer Name': 'customer_name',
    'Segment': 'segment',
    'Country': 'country',
    'City': 'city',
    'State': 'state',
    'Postal Code': 'postal_code',
    'Region': 'region',
    'Product ID': 'product_id',
    'Category': 'category',
    'Sub-Category': 'sub_category',
    'Product Name': 'product_name',
    'Sales': 'sales',
}


def run():
    with open('sales.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Transaction.objects.all().delete()

        for row in reader:
            transaction = Transaction(
                row_id=row[0],
                order_id=row[1],
                order_date=row[2],
                ship_date=row[3],
                ship_mode=row[4],
                customer_id=row[5],
                customer_name=row[6],
                segment=row[7],
                country=row[8],
                city=row[9],
                state=row[10],
                postal_code=row[11],
                region=row[12],
                product_id=row[13],
                category=row[14],
                sub_category=row[15],
                product_name=row[16],
                sales=row[17],
            )

            transaction.save()