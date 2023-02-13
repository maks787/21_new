import random 
print("Tere tulemast mängule 21, kui näitad vähem või rohkem kui 21")
koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4 #список повторяется 4 раза 
random.shuffle(koloda) #перемешивать колоду
arv = 0 #начальное число
while arv!=21: #если число НЕ равно
    while True:
      choice = input("Kas võtad kaardi? jah/ei" ) #выбор
      if choice == "jah":
            number = koloda.pop() #убирает и возравщает последнее значение из списка
            print("Sul on kaardi number %d" %number) #выбирается случайная карта из колоды 
      arv += number #суммирует все значения с начального числа 
      if arv > 21: #если число больше 21 ты проиграл
        print("Vabandust, aga sa kaotasid")
        break 
      elif arv == 21: #если у тебя набралось 21 ты выиграл
        print("palju õnne, tabasite numbrit 21!")
        break #прекращение работы програмы
      else:
        print("Teil on %d punkti." %arv) #% показывает какое число выпало 
        if choice == "ei": #если выбор нет
            print("Teil on %d punkti ja olete mängu lõpetanud." %arv) #конечное число игра окончена
            break
