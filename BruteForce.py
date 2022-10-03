alf=list(' абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
new_alf = []
new_text  =[]
num_text = []
dlin = len(alf)

# get list text input***

text = input('Введите текст сообщения для перебора: ')
new_text = list(text)
for bokv in text:
    for sym in alf:
        if (bokv == sym):           
            num_text.append(alf.index(sym))


print(new_text)
print(num_text)


# new alfavit generation ***
for i in range(1,34):
    #print('~~~~~~~~~~~~~~',i,'~~~~~~~~~~~~~~')
    for j in range(0,33):
        if(i+j > 33):
              new_alf.append(alf[i+j-33])
             # print(i+j-33,'.-->',alf[i+j-33])
        if (i+j <= 33):
            new_alf.append(alf[i+j])
            # print(i+j,'-->',alf[i+j])
        #print('~~~~~~~~~~~~~~',j,'~~~~~~~~~~~~~~')
    sum=''
    for num in num_text:
        for sym in alf:
            if (sym == new_alf[num]):
                sum += sym
    print('Результат: ',sum)
    new_alf=[]
    #input()