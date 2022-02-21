import datetime
import os.path


def decor(path):
    def _decor(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            if os.path.isfile(path):
                f = open(path, 'a', encoding="utf-8")
                content = '\n'
                content += f'Дата и время вызова функции {datetime.datetime.now()}\n'
                content += f'Имя функции: {old_function.__name__}\n'
                content += f'Аргументы: {args} {kwargs}\n'
                content += f"Результат: {result}\n"
                f.write(content)
                f.close()
            else:
                f = open(path, 'w', encoding="utf-8")
                content = ''
                content += f'Дата и время вызова функции {datetime.datetime.now()}\n'
                content += f'Имя функции: {old_function.__name__}\n'
                content += f'Аргументы: {args} {kwargs}\n'
                content += f"Результат: {result}\n"
                f.write(content)
                f.close()
            return result

        return new_function

    return _decor



