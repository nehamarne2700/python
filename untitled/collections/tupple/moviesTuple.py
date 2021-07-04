HAction=['Inception','Avengers end game','Avengers Infinity war','Black Panther','Star Wars']
HHorror=['The Nun','Phycho','Alien','IT','The Witch']
HComedy=['Once Upon A Time In Hollywood','Pulp fiction','Booksmart']
HFamily=['Toy Story','Inside out','Frozen','Home Alone','Finding Nemo']

BAction=['Baaghi 3','War','Tanaji','Malang','URI','Bang bang']
BHorror=['Raaz','Stree','1920','Alone','Bhoot']
BComedy=['Dhamaal','Housefull','Entertainment','PK','Golmaal','Welcome']
BFamily=['Ham Saath Saath Hain','Ham Apke Hai Kon','Taare Zameen Par','Kuch Kuch hota hai']

TAction=['Business Man','Baahubali','Magdheera','Sarrainadu','Dhruva','Robot','Yevdu']
THorror=['Kanchana','Raj Mahal','Arundhati','Kaashmora','Maya']
TComedy=['Comali','Surya The Racer','Mass','Devi','Super Taxi','Tutak tutak tutiya']
TFamily=['Dayalu','Son Of Satyamurti','A..aa','Business man 2']

MAction=['Mauli','Lai Bhari','Baji','Faster Fene','Farzand','Fakt Ladh Mhana']
MHorror=['Zapatlela','Pachadlela','Lapachhapi','Bhay','chakwa','Rakshas']
MComedy=['De Dhakka','Ye Re Ye Re Paisa','Narbachi Wadi','Gallit Ghondhal Dehlit Muzara']
MFamily=['Natsamrat','Sairat','Bucketlist','Killa','Naal','Muramba','Hirkani']

Hollywood=(HAction,HHorror,HComedy,HFamily)
Bollywood=(BAction,BHorror,BComedy,BFamily)
Tollywood=(TAction,THorror,TComedy,TFamily)
Marathi=(MAction,MHorror,MComedy,MFamily)

Movies=(Hollywood,Bollywood,Tollywood,Marathi)
MovieType=('Action','Horror','Comedy','Family')
Moviecategory=('Hollywood','Bollywood','Tollywood','Marathi')

ch=0

while(1):
    print('****************************************************************')
    print('\n                          MOVIES WORLD                         ')
    print('\n1:Movies Menu\n2:Add Movie\n3:Search Movie\n4:Exit')
    ch1=int(input('Enter Your choice : '))

    if(ch1==1):
        while(1):
            print('****************************************************************')
            print('\n           WELCOME TO MOVIES MENU              ')
            print('\n1:Hollywood Movies\n2:Bollywood Movies\n3:Tollywood Movies\n4:Marathi Movies\n5:Exit')
            ch=int(input('Enter your choice : '))

            if(ch==1):
                print('\n--------------------- HOLLYWOOD MOVIES -----------------')
                for i in range(len(MovieType)):
                    print('\n'+str(i+1)+' ] '+MovieType[i]+' -> ')
                    for j in range(len(Hollywood[i])):
                        print('\t'+str(j+1)+' : '+Hollywood[i][j])
                    print('\n-------------------------------------------------------\n')

            elif(ch==2):
                print('\n--------------------- BOLLYWOOD MOVIES -----------------')
                for i in range(len(MovieType)):
                    print('\n'+str(i+1)+' ] '+MovieType[i]+' -> ')
                    for j in range(len(Bollywood[i])):
                        print('\t'+str(j+1)+' : '+Bollywood[i][j])
                    print('\n-------------------------------------------------------\n')

            elif(ch==3):
                print('\n--------------------- TOLLYWOOD MOVIES -----------------')
                for i in range(len(MovieType)):
                    print('\n'+str(i+1)+' ] '+MovieType[i]+' -> ')
                    for j in range(len(Tollywood[i])):
                        print('\t'+str(j+1)+' : '+Tollywood[i][j])
                    print('\n-------------------------------------------------------\n')

            elif(ch==4):
                print('\n--------------------- MARATHI MOVIES -----------------')
                for i in range(len(MovieType)):
                    print('\n'+str(i+1)+' ] '+MovieType[i]+' -> ')
                    for j in range(len(Marathi[i])):
                        print('\t'+str(j+1)+' : '+Marathi[i][j])
                    print('\n-------------------------------------------------------\n')

            elif(ch==5):
                print('\nThank You For Visiting Us ....\n')
                break

            else:
                print('Invalid Choice....')

            con=int(input('\nDo you want to continue Movies Menu......Press 1 '))
            if(con!=1):
                break

    elif(ch1==2):
        while (1):
            print('****************************************************************')
            print('\n           WELCOME TO ADD MOVIES MENU              ')
            print('\n1:Hollywood Movies\n2:Bollywood Movies\n3:Tollywood Movies\n4:Marathi Movies\n5:Exit')
            ch = int(input('Enter category of movie to add : '))
            print('\n1:Action\n2:Horror\n3:Comedy\n4:Family')
            tp=int (input('Enter Type of movie to add'))
            if tp>len(MovieType):
                print('Invalid Type...')
                break

            if (ch == 1):
                print('\n--------------------- HOLLYWOOD MOVIES -----------------')
                print('\nType :\t'+MovieType[tp-1])
                name=str.lower(input('Enter Movie Name : '))
                if name not in (n.lower() for n in Hollywood[tp-1]):
                    Hollywood[tp-1].append(name)
                    print('Movie listed successfully...')
                    print(Hollywood[tp-1])
                else:
                    print('Movie is already listed...')
                print('\n-------------------------------------------------------\n')

            elif (ch == 2):
                print('\n--------------------- BOLLYWOOD MOVIES -----------------')
                print('\nType :\t' + MovieType[tp - 1])
                name = str.lower(input('Enter Movie Name : '))
                if name not in (n.lower() for n in Bollywood[tp - 1]):
                    Bollywood[tp - 1].append(name)
                    print('Movie listed successfully...')
                    print(Bollywood[tp - 1])
                else:
                    print('Movie is already listed...')
                print('\n-------------------------------------------------------\n')

            elif (ch == 3):
                print('\n--------------------- TOLLYWOOD MOVIES -----------------')
                print('\nType :\t' + MovieType[tp - 1])
                name = str.lower(input('Enter Movie Name : '))
                if name not in (n.lower() for n in Tollywood[tp - 1]):
                    Tollywood[tp - 1].append(name)
                    print('Movie listed successfully...')
                    print(Tollywood[tp - 1])
                else:
                    print('Movie is already listed...')
                print('\n-------------------------------------------------------\n')

            elif (ch == 4):
                print('\n--------------------- MARATHI MOVIES -----------------')
                print('\nType :\t' + MovieType[tp - 1])
                name = str.lower(input('Enter Movie Name : '))
                if name not in (n.lower() for n in Marathi[tp - 1]):
                    Marathi[tp - 1].append(name)
                    print('Movie listed successfully...')
                    print(Marathi[tp - 1])
                else:
                    print('Movie is already listed...')
                print('\n-------------------------------------------------------\n')

            elif (ch == 5):
                print('\nThank You For Visiting Us ....\n')
                break

            else:
                print('Invalid Choice....')

            con = int(input('\nDo you want to continue with Add Movie Menu......Press 1 '))
            if (con != 1):
                break

    elif(ch1==3):
        print('****************************************************************')
        print('\n           WELCOME TO SEARCH MOVIES MENU              ')
        flag=0
        name=str.lower(input('Enter Movie Name You Want To Search : '))
        for i in range(len(Movies)):
            for j in range(len(Movies[i])):
                if name in (n.lower() for n in Movies[i][j]):
                    print('\nMovie Found In ->'+Moviecategory[i]+' -> '+MovieType[j])
                    flag=1
                    break
        if(flag==0):
            print('Movie Not Found...')

    elif(ch1==4):
        print('\nThank You...')
        break

    else:
        print("Invalid Choice....")