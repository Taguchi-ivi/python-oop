class EmployeeData:
  def __init__(self, name: str, department: str) -> None:
    self.name = name
    self.department = department


class PayCalculator:
  def __get_regular_hours(self):
    print("給与計算専用の労働時間計算ロジック")

  def calculate_pay(self, employee: EmployeeData):
    self.__get_regular_hours()
    print(f"{employee.name}の給与を計算しました")

class HourReporter:
  def __get_regular_hours(self):
    print("労働時間レポート専用の労働時間計算ロジック")

  def report_hours(self, employee: EmployeeData):
    self.__get_regular_hours()
    print(f"{employee.name}の労働時間をレポートしました")

class EmployeeRepository:
  def save(self):
    pass

if __name__ == "__main__":
  emp = EmployeeData("Suzuki", "develop")
  pay_calculator = PayCalculator()
  hour_reporter = HourReporter()

  print("経理部門")
  pay_calculator.calculate_pay(emp)

  print("")
  print("人事部門")
  hour_reporter.report_hours(emp)
