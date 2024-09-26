import sys

from dotenv import load_dotenv

from databasemaker import DatabaseMaker
from infogenerator import InfoGenerator


def migrate_db(is_test_db: bool):
    db = DatabaseMaker(is_test_db=is_test_db)
    db.drop_tables()
    db.create_tables()


def generate_info(is_test_db: bool, rows: int):
    db = DatabaseMaker(is_test_db=is_test_db)
    db.drop_tables()
    db.create_tables()
    InfoGenerator(rows).generate_info()
    db.copy_tables()


if __name__ == "__main__":
    load_dotenv("/home/sheglar/bmstu/petowo/ppo/internal/.env")
    args = sys.argv

    if len(args) > 4 or len(args) == 1:
        print('Invalid number of parameters (must be > 0, < 4)')
        exit(1)
    if len(args) == 2:
        if args[1] == 'test':
            migrate_db(is_test_db=True)
        elif args[1] == 'main':
            migrate_db(is_test_db=False)
            print("done setting main db")
        else:
            print('Invalid parameter: must be "test" or "main"')
            exit(1)
    elif len(args) == 3:
        if args[1] == 'test':
            if args[2] != 'info':
                print('Invalid 2nd parameter: must be "info"')
                exit(1)
            generate_info(is_test_db=True, rows=1000)
        elif args[1] == 'main':
            if args[2] != 'info':
                print('Invalid 2nd parameter: must be "info"')
                exit(1)
            generate_info(is_test_db=False, rows=1000)
        else:
            print('Invalid 1st parameter: must be "test" or "main"')
            exit(1)

    elif len(args) == 4:
        if args[1] == 'test':
            if args[2] != 'info':
                print('Invalid 2nd parameter: must be "info"')
                exit(1)
            try:
                rows = int(args[3])
            except ValueError:
                print('Invalid 3rd parameter: must be int')
                exit(1)
            generate_info(is_test_db=True, rows=rows)
        elif args[1] == 'main':
            if args[2] != 'info':
                print('Invalid 2nd parameter: must be "info"')
                exit(1)
            try:
                rows = int(args[3])
            except ValueError:
                print('Invalid 3rd parameter: must be int')
                exit(1)
            generate_info(is_test_db=False, rows=rows)
        else:
            print('Invalid 1st parameter: must be "test" or "main"')
            exit(1)
