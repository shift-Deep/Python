print('aaja 3 kati khele')
list1 = [[], [], []]
list2 = [['X', 'X', 'X'], ['O', 'O', 'O']]
cells = '_________'
cells = cells.replace('_', ' ')
m = 0
for i in range(0, 3):
    for j in range(0, 3):
        if i == 1:

            list1[i].append(cells[j + 3])
        elif i == 2:

            list1[i].append(cells[j + 6])
        else:

            list1[i].append(cells[j])

print('-' * 9)
for i in range(0, 3):
    print('| ' + ' '.join(list1[i]) + ' |')
print('-' * 9)
while 1:
    print('enter the cordinates')
    s = input()
    k = int(s[0]) - 1
    l = int(s[2]) - 1
    if k + 1 >= 4 or l + 1 >= 4:
        print("Coordinates should be from 1 to 3!")
        continue

    elif s.isalpha():
        print("You should enter numbers!")
        continue
    elif list1[k][l] == 'X' or list1[k][l] == 'O':
        print("This cell is occupied! Choose another one!")
        continue

    else:
        if m % 2 == 0:

            list1[k][l] = 'X'
            m += 1
        else:
            list1[k][l] = 'O'
            m += 1
        print('-' * 9)
        for i in range(0, 3):
            print('| ' + ' '.join(list1[i]) + ' |')
        print('-' * 9)

        if list1[0] in list2 or list1[1] in list2 or list1[2] in list2:
            print('X wins')
            break
        elif list1[0] in list2 or list1[1] in list2 or list1[2] in list2:
            print('O wins')
            break
        elif list1[0][0] == 'X' and list1[1][1] == 'X' and list1[2][2] == 'X':
            print('X wins')
            break
        elif list1[0][0] == 'O' and list1[1][1] == 'O' and list1[2][2] == 'O':
            print('O wins')
            break
        elif list1[0][0] == 'X' and list1[1][0] == 'X' and list1[2][0] == 'X':
            print('X wins')
            break
        elif list1[0][0] == 'O' and list1[1][0] == 'O' and list1[2][0] == 'O':
            print('O wins')
            break
        elif list1[0][2] == 'X' and list1[1][2] == 'X' and list1[2][2] == 'X':
            print('X wins')
            break
        elif list1[0][2] == 'O' and list1[1][2] == 'O' and list1[2][2] == 'O':
            print('O wins')
            break
        elif list1[0][2] == 'X' and list1[1][1] == 'X' and list1[2][0] == 'X':
            print('X wins')
            break
        elif list1[0][2] == 'O' and list1[1][1] == 'O' and list1[2][0] == 'O':
            print('O wins')
            break
        elif m >= 9:
            print('Draw')
            break;

        else:
            continue




