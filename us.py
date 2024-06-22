import os

file_path = 'usernames.txt'
usernames_count = []

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        usernames = file.read().splitlines()
    
    print(f'Nomes de utilizadores filtrados:')
    
    for user in usernames:
        found = False
        for i, (u, count) in enumerate(usernames_count):
            if u == user:
                usernames_count[i][1] += 1
                found = True
                break
        if not found:
            usernames_count.append([user, 1])
        
    for user, count in usernames_count:
        if count > 3:
            print(f'{user} - {count}')
