user_input = input()
sedadar = ['a', 'e', 'i', 'o', 'u']
iteration_no = 1
for i in user_input:
  if i in sedadar:
    iteration_no *= 2
print(iteration_no)