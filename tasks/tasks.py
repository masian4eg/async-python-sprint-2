import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s - %(message)s')

FILE = 'mydocument.txt'
RENAMED_FILE = 'mysuperdocument.txt'
NEW_DIR = 'new_dir'


def task_1():
    logging.info('run task_1')
    with open(FILE, mode='w') as f:
        f.write('This text is written with Python')


def task_2():
    logging.info('run task_2')
    os.rename(FILE, RENAMED_FILE)


def task_3():
    logging.info('run task_3')
    os.mkdir(NEW_DIR)


def task_4():
    logging.info('run task_4')
    os.rmdir(NEW_DIR)


def task_5():
    logging.info('run task_5')
    with open(RENAMED_FILE, mode='a') as f:
        f.write('This text is written with Python. CHAPTER 2!')


def task_6():
    logging.info('run task_6')
    os.remove(RENAMED_FILE)


TASKS = {
    'task_1': task_1,
    'task_2': task_2,
    'task_3': task_3,
    'task_4': task_4,
    'task_5': task_5,
    'task_6': task_6,
}
