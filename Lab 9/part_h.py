#Part H

#1 and #2
class Exporter:
    def __init__(self):
        pass

    def export(data : str):
        print("[data converted to ???]")

    #5
    def __str__(self):
        return "exporter"

#3
class ConsoleExporter(Exporter):
    def __init__(self):
        super().__init__()

    def export(data : str):
        print(f"[{data} converted for a console]")

    def __str__(self) -> str:
        return "console exporter"

class TextExporter(Exporter):
    def __init__(self):
        super().__init__()

    def export(data : str):
        print(f"[{data} converted to text]")

    def __str__(self) -> str:
        return "text exporter"

class SummaryExporter(Exporter):
    def __init__(self):
        super().__init__()

    def export(data : str):
        print(f"[{data} converted to a summary]")

    def __str__(self) -> str:
        return f"summary exporter"


#6
exporters = [
    Exporter(),
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter()
]

#7
for exporter in exporters:
    exporter.export()

#8
class ThirdPartyService:
    def __init__(self):
        pass    

    def export(data : str):
        print("LMAO you shouldn't have trusted us, good luck.")


#9
generic_console_exporter = ConsoleExporter()

#First, the ones that should be obvious.
print(isinstance(generic_console_exporter, ConsoleExporter))
print(isinstance(generic_console_exporter, ConsoleExporter))
print(isinstance(generic_console_exporter, object))
#With this one right above, there is no point in testing it to a primitive type, because objects are not primitives, but can consist of them.

#Then, testing that a subclass is not equal to another one.
print(isinstance(generic_console_exporter, SummaryExporter))
