class Animals:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feed(self, corm):
    self.weight += corm
    return self.weight
  
  def feed_sum(self, count):
    return count



class Eggs(Animals):
  def do_some(self):
    return "мы собрали с неё яйца"


class Goose(Eggs):
  animal_type = "Гусь"
  def say(self):
    voice = "га-га"
    return voice


class Milk(Animals):
  def do_some(self):
    return "мы подоили её"


class Cow(Milk):
  animal_type = "Корова"
  def say(self):
    voice = "Мууу"
    return  voice 


class Cutting(Animals):
  def do_some(self):
    return "мы её стригли"

class Sheep(Cutting):
  animal_type = "Овца"
  def say(self):
    voice = "Беее"
    return voice


class Roster(Eggs):
  animal_type = "Курица"
  def say(self):
    voice = "ko-ko"
    return voice


class Goat(Cutting):
  animal_type = "Коза"
  def say(self):
    voice = "me-me"
    return voice


class Duck(Eggs):
  animal_type = "Утка"
  def say(self):
    voice = "кря-кря"
    return voice



animals_list = [
Goose("Серый", 5),
Goose("Белый", 3),
Cow("Манька", 375),
Sheep("Барашек", 50),
Sheep("Кудрявый", 40),
Roster("KOKO", 7),
Roster("Кукареку", 8),
Goat("Рога", 15),
Goat("Копыта", 14),
Duck("Кряква", 10)
]

sum_weight = 0
max_ = 0

for result in animals_list:
  print(result.name, "-это", result.animal_type, "говорящая", result.say(), "и", result.do_some(), "она весит:", result.weight, "кг.", "мы её накормили на:", result.feed_sum(2), "кг", "вес после кормление:", result.feed(2), "кг", "\n")
  sum_weight += result.weight
  
  if result.weight > max_:
    max_ = result.weight
      


print("максимальный вес у животного по имени", result.name, "и оно весит", max_, "кг")
print("вес всех животных состовляет:", sum_weight, "кг")