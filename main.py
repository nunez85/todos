todos = []

def print_todos(list: list[str]):
    if len(list) == 0:
        print('No todos')
        return

    max_len = len(max(list, key=lambda x: len(x)))
    horizontal_dashes = '-' * (max_len + 4)
    print('Todos:')
    print(horizontal_dashes)
    for i, element in enumerate(list, start=1):
        print(f'{i}. {element}')
        if i != len(list):
            print(horizontal_dashes)

    print(horizontal_dashes)


def main():
    while True:
        user_input = input('Type add, show, or exit: ')
        if user_input:
            user_input = user_input.strip()
        else:
            continue

        match user_input:
            case 'add':
                todo = input('Enter todo: ')
                if todo:
                    todo = todo.strip()
                else:
                    continue

                todos.append(todo.capitalize())
            case 'show':
                print_todos(todos)
            case 'exit':
                break
            case _:
                print('Unsupported command')

    print('Exiting todos, goodbye!')



if __name__ == '__main__':
    main()