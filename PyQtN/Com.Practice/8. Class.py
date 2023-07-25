# 1

class Tiguan():
  def walk(self):
    print('성큼 성큼')
  def hello(self):
    print('안녕하세요')

tiguan = Tiguan()
tiguan.walk()

# 2
class Kduck():
  def __init__(self, color):
    self.color = color
  def walk():
    print('뒤뚱 뒤뚱')
  def color(self, color):
    print(color)

myduck = Kduck('white')
print(myduck.color)

# 3
class KyourWindow():
  def getPosition(self):
    return (0, 0)

class KmyWindow(KyourWindow):
  pass

my_window = KmyWindow()
print( my_window.getPosition() )

# 4
class Machine():
  def __init__(self):
    super().__init__()
    self.power()  
  
  def power(self):
    print('Power On')
    
  def run(self):
    print('삐그덕 삐그덕')
  
class NewMachine(Machine):
  def __init__(self):
    super().__init__()
    self.setting()

  def run(self):
    print('위이잉~~')

  def setting(self):
    print('징~ 징~ 사전 설정 중입니다.')
    print('사전 설정 완료되었습니다.')

machine = Machine()
machine.run()

print('-'*32)

new_machine = NewMachine()
new_machine.run()