'''import os

if os.path.exists('sketch.txt'):
    date = open('sketch.txt')

    for each_line in date:
        try:
#if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass
    date.close()
else:
    print('The date file is missing!')'''




import sys
import pickle

def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=fh)
            print(each_item,file=fh)


man = []
other = []

try:
    date = open('sketch.txt')

    for each_line in date:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    date.close()
except IOError:
    print('The date file is missing!')

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

try:
    with open('man_data.txt', 'rb') as man_file, open('other_data.txt', 'rb') as other_file:
        new_man = pickle.load(man_file)
        new_other = pickle.load(other_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

print_lol(new_man)
print_lol(new_other)

#try:
#    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
#        print_lol(man, fh=man_file)
#        print_lol(other, fh=other_file)
#except IOError as err:
#    print('File error:' + str(err))



'''try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file = man_file)
    print(other, file = other_file)
#    man_file.close()
#    other_file.close()
except IOError:
    print('File error.')

finally:
    man_file.close()
    other_file.close()'''

#print(man)
#print(other)


