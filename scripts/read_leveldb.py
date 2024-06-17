import sys
import plyvel
import configparser

def get_value(db, key):
    """
    Retrieves the value for a specified key from the LevelDB database.
    """
    try:
        value = db.get(key.encode('utf-8'))
        if value:
            print(f'Value for key "{key}": {value.decode("utf-8")}')
        else:
            print(f'Key "{key}" not found')
    except KeyError:
        print(f'Key "{key}" not found')

def scan_db(db):
    """
    Iterates over all key-value pairs in the LevelDB database and prints them.
    """
    try:
        for key, value in db:
            print(f'Key: {key.decode("utf-8")}, Value: {value.decode("utf-8")}')
    except Exception as e:
        print("Error scanning database", e)

def main():
    """
    Main function to handle command-line arguments and interact with the LevelDB database.
    """
    # Default to None to check if they're set later
    db_path = None
    command = None
    key = None

    # Read configuration file
    config = configparser.ConfigParser()
    config.read('scripts/config.ini')

    if 'LevelDB' in config and 'db_path' in config['LevelDB']:
        db_path = config['LevelDB']['db_path']

    # Override db_path if provided via command-line arguments
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command == "get" and len(sys.argv) == 4:
            db_path = sys.argv[2]
            key = sys.argv[3]
        elif command == "get" and len(sys.argv) == 3:
            key = sys.argv[2]
        elif command == "scan" and len(sys.argv) == 3:
            db_path = sys.argv[2]
        elif command == "scan" and len(sys.argv) == 2:
            pass
        else:
            print("Usage: python3 scripts/read_leveldb.py <command> [db_path] [key]")
            print("Commands:")
            print("  get <key>         - Get the value for the specified key")
            print("  get <db_path> <key> - Get the value for the specified key with a specified db_path")
            print("  scan [db_path]    - Scan and print all key-value pairs with an optional specified db_path")
            sys.exit(1)

    if db_path is None:
        print("Database path must be specified either in config.ini or as a command-line argument.")
        sys.exit(1)

    try:
        db = plyvel.DB(db_path, create_if_missing=False)
    except Exception as e:
        print(f"Error opening LevelDB at {db_path}: {e}")
        sys.exit(1)

    if command == "get":
        if key is None:
            print("Usage: python3 scripts/read_leveldb.py get [db_path] <key>")
            sys.exit(1)
        get_value(db, key)
    elif command == "scan":
        scan_db(db)
    else:
        print("Unknown command:", command)
        sys.exit(1)

    db.close()

if __name__ == "__main__":
    main()
