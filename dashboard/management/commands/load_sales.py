from django.core.management.base import BaseCommand, CommandError
from dashboard.models import Transaction
import csv


class Command(BaseCommand):
    help = "Import the sales data into the django database"

    def handle(self, *args, **options):
        with open("data/sales.csv", encoding="utf-8") as file:
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

        self.stdout.write(self.style.SUCCESS("Successfully loaded sales data"))
