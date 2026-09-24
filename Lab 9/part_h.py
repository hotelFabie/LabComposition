#Part H

#1 and #2
class Exporter:
    def __init__(self):
        pass

    #4
    def export(self, data : str):
        print(f"[{data} converted to ???]")

    #5
    def __str__(self):
        return "exporter"

#3
class ConsoleExporter(Exporter):
    def __init__(self):
        super().__init__()

    #4
    def export(self, data : str):
        print(f"{data} can now be dealt with through the console.")

    #5
    def __str__(self) -> str:
        return "console exporter"

class TextExporter(Exporter):
    def __init__(self):
        super().__init__()

    #4
    def export(self, data : str):
        print(f"{data}")

    #5
    def __str__(self) -> str:
        return "text exporter"

class SummaryExporter(Exporter):
    def __init__(self):
        super().__init__()

    #4
    def export(self, data : str):
        print(f"SUMMARY\nthis is a {data}.")

    #5
    def __str__(self) -> str:
        return f"summary exporter"

#6
exporters = [
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter()
]

#7
for exporter in exporters:
    exporter.export("thing")

#8
class ThirdPartyService:
    def __init__(self):
        pass    

    def export(self, data : str):
        print("LMAO you shouldn't have trusted us, good luck.")

#Demonstrating that it can be used by inserting it into the list/collection made above, and then be iterated through (again).
exporters.append(ThirdPartyService())

for exporter in exporters:
    exporter.export("modern thing")

#9
generic_console_exporter = ConsoleExporter()

#First, the ones that should be obvious.
print(isinstance(generic_console_exporter, ConsoleExporter))
print(isinstance(generic_console_exporter, ConsoleExporter))
print(isinstance(generic_console_exporter, object))
#With this one right above, there is no point in testing it to a primitive type, because objects are not primitives, but can consist of them.

#Then, testing that a subclass is not equal to another one.
print(isinstance(generic_console_exporter, SummaryExporter))

#10 - Did not want to mess up an earlier instance of a console exporter, so I made one here again.
class ConsoleExporter(Exporter):
    def __init__(self, console_option):
        super().__init__()

        #10 - The console exporter HAS AN option for which console it should adjust the export to.
        self.console_option = console_option

    #4
    def export(self, data : str):
        print(f"{data} can now be dealt with through the console.")

    #5
    def __str__(self) -> str:
        return "console exporter"