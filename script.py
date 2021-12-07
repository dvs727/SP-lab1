

NAME = 'Дубоносов Вячеслав'
PROGRAM = __file__
DESCR = 'Задание 7'
PASSWD_FILE_ABS_PATH = '/etc/passwd'
GROUP_FILE_ABS_PATH = '/etc/group'


def run_end():
    while True:
        answer = input('Продолжим? [д/н] :')
        if answer == 'н':
            return False
        elif answer == 'д':
            return True
        else:
            print('Неизвестная команда')
            continue


def _input_name():
    INCORRECT_LITERAL = [' ', '']
    while True:
        name = input('Введите имя пользователя: ')
        if not all(char in INCORRECT_LITERAL for char in name):
            print('CORRECT NAME: {}'.format(name))
            return name
        else:
            print('WARNING: name is contain incorrect literals. Input again')
            continue


def _read_file_in_list(file):
    with open(file) as passwd:
        data = passwd.read().split('\n')
        return data


def _get_data_from_line_passwd(line):
    username, password, uid, gid, descr, path, start = line.split(':')
    return username, password, uid, gid, descr, path, start


def _get_data_from_line_group(line):
    group_name, password, gid, all_users = line.split(':')
    return group_name, password, gid, all_users
    pass


def _is_line_group_by_username(name, line):
    data = line.split(':')
    users = data[3].split(',')
    if name in users:
        return True
    else:
        return False


def _is_line_username(name, line):
    if name == line.split(":")[0]:
        return True
    else:
        return False
    pass


def _get_user_data_by_username(name):
    list_data = _read_file_in_list(PASSWD_FILE_ABS_PATH)
    for line in list_data:
        if _is_line_username(name, line):
            _, _, uid, gid, _, _, _ = _get_data_from_line_passwd(line)
            return uid, gid
        else:
            continue
    return None, None


def _get_groups_by_username(gid, username):
    list_data = _read_file_in_list(GROUP_FILE_ABS_PATH)
    list_data.remove('')
    groups = []
    basic_group_name = ''
    for line in list_data[:-1]:
        group_name, _, gid_line, _ = _get_data_from_line_group(line)
        if gid_line == gid:
            basic_group_name = group_name
        if _is_line_group_by_username(username, line):
            groups.append(group_name)
    return groups, basic_group_name


def main():
    while True:
        username = _input_name()
        uid, gid = _get_user_data_by_username(username)
        if uid == None and gid == None:
            print('USER NOT EXIST')
        else:
            groups, basic_group_name = _get_groups_by_username(gid, username)
            print('username:{};UID:{}; groups:{} \nbasic group:{}'.format(
                username,
                uid,
                ' '.join(groups),
                basic_group_name,
            ))
            # тут вывод по заданию
        if not run_end():
            return True
        else:
            continue


if __name__ == "__main__":
    print(
        '{name} {program}; \n описание: {descr}'.format(
            name=NAME,
            program=PROGRAM,
            descr=DESCR,
        )
    )

    main()
