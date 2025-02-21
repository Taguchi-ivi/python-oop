from abc import ABC, abstractmethod
import datetime
import re

class Context:
  def __init__(self, expression: str, date: datetime.date) -> None:
    self.validate(expression)
    self.expression = expression
    self.date = date

  def validate(self, expression: str) -> None:
    if len(expression) != 10 or not bool(re.match(r"(?.*YYYY)(?.*MM)(?.*DD)", expression)):
      raise ValueError("expressionが不正です")

class AbstractExpression(ABC):
  @abstractmethod
  def interpret(self, context: Context) -> Context:
    pass

class YearExpression(AbstractExpression):
  def __init__(self):
    self.__child = None

  def set_child(self, child: AbstractExpression) -> None:
    self.__child = child

  def interpret(self, context: Context) -> Context:
    expression = context.expression
    year = context.date.year
    context.expression = expression.replace("YYYY", str(year))

    # 再起的に
    if self.__child:
      self.__child.interpret(context)
    return context

class MonthExpression(AbstractExpression):
  def __init__(self):
    self.__child = None

  def set_child(self, child: AbstractExpression) -> None:
    self.__child = child

  def interpret(self, context: Context) -> Context:
    expression = context.expression
    month = context.date.month
    context.expression = expression.replace("MM", str(month).zfill(2))

    # 再起的に
    if self.__child:
      self.__child.interpret(context)
    return context

class DayExpression(AbstractExpression):
  def __init__(self):
    self.__child = None

  def set_child(self, child: AbstractExpression) -> None:
    self.__child = child

  def interpret(self, context: Context) -> Context:
    expression = context.expression
    day = context.date.day
    context.expression = expression.replace("DD", str(day).zfill(2))

    # 再起的に
    if self.__child:
      self.__child.interpret(context)
    return context


if __name__ == "__main__":
  now_date = datetime.datetime.now().date()
  expression = "MM/DD/YYYY"

  context = Context(expression, now_date)

  year_expression = YearExpression()
  month_expression = MonthExpression()
  day_expression = DayExpression()

  month_expression.set_child(day_expression)
  year_expression.set_child(month_expression)

  result = year_expression.interpret(context)

  print(now_date.strftime("%m/%d/%Y"))
  print(result.expression)