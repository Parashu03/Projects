print('VOTING SOFTWARE')
list1=[]
list2=[]
print('SYMBOL 1 for  Party1 ')
print('SYMBOL 2 for Party2 ')
print('NOTE :- PLEASE ENTER ONLY 1 AND 2')
dict={'001':'a','002':'b','003':'c','004':'d','005':'e'}
while True:
    id=input('Enter Your VOTER ID :')
    if id in dict.keys():
        dict.pop(id)
        while True:
            n=input('enter your choice :')
            if n=='1':
                list1.append(n)
                break
            elif n=='2':
                list2.append(n)
                break
            elif n=='exit':
                break
            else:
                print('Try again...')
    elif id=='exit':
        num=len(list1)+len(list2)
        print('total no of votes =',num)
        print('Party1 votes are :- ',len(list1))
        print('Party2  votes are :- ',len(list2))
        if len(list1)>len(list2):
            print('Congratulation\'s Party1 on your successfull WIN in ELECTION ')
        elif len(list1)==len(list2):
            print('The both parties got same votes... ')
        else:
            print('Congratulation\'s Party2 on your successfull WIN in ELECTION ')
        break
    elif id not in dict.keys():
        print('ID not exist ..')
    else:
        print('Invalid ID...')
print('''BE BRIGHT ...
      VOTE FOR WHAT IS RIGHT...!''')