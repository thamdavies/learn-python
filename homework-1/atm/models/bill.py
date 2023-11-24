class Bill:
  def __init__(self, datetime, user, amount):
    self.__datetime = datetime
    self.__user = user
    self.__amount = amount

  def date(self):
    return self.__datetime.strftime("%Y-%m-%d")

  def time(self):
    return self.__datetime.strftime("%H:%M:%S")

  def user(self):
    return self.__user

  def amount(self):
    return '${:,}'.format(self.__amount)

  def account_balance(self):
    return self.__user.fm_account_balance()
  
