#Python List sort() Method

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
#['Volvo', 'Ford', 'BMW']


def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
#['VW', 'BMW', 'Ford', 'Mitsubishi']