from configparser import ConfigParser


def config(filename='sql_app/database.ini', section='postgresql'):
    # create parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found in {filename} file.')
    return db_config


if __name__ == '__main__':
    print(config(filename="database.ini"))
