q1=""" what is the capital of Andhra Pradesh?
a) Amaravati
b) vizag
c)vijayawada
d) Guntur"""

q2="""What's anushka character role name in Bahubali?
a) Devesana
b) Sivagami
c) Avantika
d) Arundati"""

q3="""who is the national crush?
a) Samantha
b) Tamanah
c) Rashmika
D) Anushka"""

q4="""who is the founder of instagram?
a) Bill gates
b) Ambani
c) Mark Zukerberg
d) Elon musk"""

q5="""who is the prime minister of india?
a) Jagan mohan reddy
b) Narendra modi
c) Draupadi murmu
d) Rishi sunak"""

que={q1:"b",q2:"a",q3:"c",q4:"c",q5:"b"}
name=input("Hi, What is ur name?")
print("Hello",name,"Welcome to the quiz")
score=0
for i in que:
    print()
    print(i)
    s1=input("Do you want to skip this question(yes/no):")
    if s1=="yes":
        continue
    ans=input("Enter the answer:")
    if ans==que[i]:
        print("Wow! u got 1 point")
        score=score+1
        print("ur current score:",score)
    else:
        print("sorry, u lost 1 point")
        score=score-1
        print("ur current score:",score)
    s2=input("Do you want to quit(yes/no)?")
    if s2=="yes":
        break
print("ur total score=",score)
        




 
