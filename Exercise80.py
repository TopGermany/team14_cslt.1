import random
num_simulations=10
total_flips=0
for _ in range(num_simulations):
    num_flips=0
    current_streak=0
    current_result=''
    while current_streak<3:
        num_flips+=1
        total_flips+=1
        flip_result=random.choice(['H', 'T'])
        if current_result==flip_result:
            current_streak+=1
        else:
            current_result=flip_result
            current_streak=1
        print(flip_result, end=' ')
    print("(" + str(num_flips) + " flips)", end=' ')
    print()
average_flips=total_flips/num_simulations
print("On average, "+str(average_flips)+" flips were needed.")