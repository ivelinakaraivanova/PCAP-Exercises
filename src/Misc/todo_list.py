import uuid


def show_tasks(tasks_file):

    try:
        text = open(tasks_file, 'r')
        tasks_list = text.readlines()
        text.close()
    except Exception as e:
        print(e)
    
    return tasks_list


def print_tasks(tasks_list):
    print('\n[YOUR TASKS]')
    if len(tasks_list) == 0:
        print('Empty list\n')
    for task in tasks_list:
        id, description, deadline = task.split(';')
        print(f'{id} | {description} | {deadline}')


def add_task(tasks_file, description, deadline):
    try:
        text = open(tasks_file, 'a')
        id = str(uuid.uuid4())
        text.write(id + ';' + description + ';' + deadline + '\n')
        text.close()
    except Exception as e:
        print(e)

    return tasks_file


def remove_task(tasks_file, id):
    try:
        text = open(tasks_file, 'r')
        tasks = text.readlines()
        tasks_ids = [task.split(';')[0] for task in tasks]

        if id not in tasks_ids:
            return 0
        
        tasks = [x.split(';') for x in tasks]
        tasks = list(filter(lambda x: x[0] != id, tasks ))
        tasks = [x[0]+';'+x[1]+';'+x[2] for x in tasks]
        text.close()
        text = open(tasks_file, 'w')
        text.writelines(tasks)
        text.close()
    except Exception as e:
        print(e)
    
    return tasks_file


def show_menu():
    while True:
        print('\n== TODO LIST ==')
        print('''[1] Show tasks'\n[2] Add tasks\n[3] Complete tasks\n[4] Exit''')
        choice = input('Your choice: ')

        if choice == '1':
            tasks = show_tasks('file_with_tasks.txt')
            print_tasks(tasks)

        elif choice == '2':
            print('[ADD TASK]')
            description = input('What is the task? ')
            deadline = input('What is the deadline? ')
            add_task('file_with_tasks.txt', description, deadline)

        elif choice == '3':
            print('[COMPLETE TASK]')
            tasks = show_tasks('file_with_tasks.txt')
            print_tasks(tasks)

            if not tasks:
                print('No tasks to complete')
            else:
                id = input('Enter id to complete ')
                remove_task('file_with_tasks.txt', id)
       
        elif choice == '4':
            break

        else:
            print('Please enter a correct value')
        

show_menu()
