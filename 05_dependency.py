"""Dependency (Uses-a): one class uses another only temporarily, as a method argument."""


class Printer:
    def print_page(self, text: str):
        print(f"Printing: {text}")


class ReportGenerator:
    def __init__(self, content: str):
        self.content = content

    # ReportGenerator depends on a Printer strictly during this call.
    # The Printer reference is never stored.
    def output_report(self, printer_device: Printer):
        printer_device.print_page(self.content)


if __name__ == "__main__":
    # 1. Instantiate the objects independently
    my_printer = Printer()
    quarter_report = ReportGenerator("Q1 Academic Performance: Excellent!")

    # 2. Pass the required device in only for this call
    quarter_report.output_report(my_printer)
