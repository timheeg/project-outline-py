import logging


def is_true():
    return True


def is_false():
    return False


def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Hello, world")


if __name__ == '__main__':
    main()
