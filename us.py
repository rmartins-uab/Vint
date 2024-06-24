import os

file_path = 'usernames_and_urls.txt'
output_path = 'output.txt'
usernames_count = []

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        usernames = file.read().splitlines()
    
    for user in usernames:
        found = False
        for i, (u, count) in enumerate(usernames_count):
            if u == user:
                usernames_count[i][1] += 1
                found = True
                break
        if not found:
            usernames_count.append([user, 1])
    
    with open(output_path, 'w', encoding='utf-8') as file:
        for user, count in usernames_count:
            file.write(f'{user} ,{count}\n')

    print(f'Arquivo processado e salvo em {output_path}')
else:
    print(f'O arquivo {file_path} não existe.')
