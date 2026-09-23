#Part G

#WIP

#1
class Report:
    def __init__(self):
        pass

    def get_summary():
        return "<summary wip>"    
        

#2
class SalesReport(Report):
    def __init__(self):
        super().__init__()

    #3
    def get_summary():
        return super().get_summary() + "<more stuff>"

#4
sales_report = SalesReport()