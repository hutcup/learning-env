user_input = input()
user_input_list = user_input.split(" ")
Zir_alephba = []
list1 = []
answer = ''
list_answers = []
for i in range(int(user_input_list[0])):
    list1.append(input())
    
for i in user_input_list[1]:
    if not i in Zir_alephba:
        Zir_alephba.append(i)
        
for i in list1:
    for j in i:
        if not j in Zir_alephba:
            answer = "No"
            break
        else:
            answer = "Yes"
    list_answers.append(answer)
for i in list_answers:
    print(i)