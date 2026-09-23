#Part G

#1
class Report:
    def __init__(self, title : str):
        self.title = title

    def get_summary(self):
        return f"[{self.title}]"    
        

#2
class SalesReport(Report):
    def __init__(self, title : str, sales_number : int):
        super().__init__(title)

        self.sales_number = sales_number

    #3
    def get_summary(self):
        return super().get_summary() + f" {self.sales_number} units have been sold."

#4
sales_report = SalesReport("FISH EQUIPMENT", 5000)
print(sales_report.get_summary())