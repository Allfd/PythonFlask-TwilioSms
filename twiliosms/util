
import os
import logging

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('C:/Users/bhardhi/PycharmProjects/EstesTwilioSMS/app/appFiles/app.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Open_File():
    """Open_File Class will open file/close in Directory"""
    def __init__(self, filename, mode):
        self.filenam e= filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

class Create_Dir():

    def __init__(self, directoryName):
        try:
            self.directoryName = directoryName
            cwd = os.getcwd()
            os.mkdir(directoryName)
            # print(os.listdir())
            os.chdir(cwd)
        except Exception as e:
            print("File Path Already Created")
        except IOError as e:
            print(e)
        else:
            print(os.listdir())


class Member:

    num_of_team_members = 0

    def __init__(self ,first ,last ,phone_number, team_name):
        self.first = first
        self.last = last
        self.phone_number = phone_number
        self.team_name = team_name

        Member.num_of_team_members += 1

        f = open("C:/Users/bhardhi/PycharmProjects/EstesTwilioSMS/app/appFiles/teamMembers.txt", "a+")
        f.write('{0}, {1}, {2}, {3}\n'.format(first, last, phone_number ,team_name))
        f.close()
        logger.info('Created Team Member: {} - {} -{}'.format(self.first, self.last, self.phone_number))

    def fullname(self):
        retur n('{} {}'.format(self.first ,self.last))

    def is_valid_num(self):
        if len(self.phone_number) == 10:
            print("Phone Number is valid")
        else: print("Not a valid phone number")

'''class get_phone_number:
    f = open("C:/Users/bhardhi/PycharmProjects/EstesTwilioSMS/app/appFiles/teamMembers.txt", "r")
    lines = f.readlines()
    for line in lines:
        #line = (line.rsplit(',', 3))
        #print(line)
        numbers = (line.split()[2])
        print(numbers.replace(',', ''))'''
