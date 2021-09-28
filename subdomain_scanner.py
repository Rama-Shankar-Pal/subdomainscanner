import subprocess
import sys
import os


def main(file_name):
    
#    domains = False
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            domains = file.readlines()
    else:
        print 'File does not exist!\n'
        sys.exit(0)

    for index, domain in enumerate(domains):
        if domain != '\\n':
            domains[index] = domain.rstrip('\n')
    
    output_file = open('out.txt', 'w')

    for index, domain in enumerate(domains):
        output_file.write("{:#^50}".format(domain))
        print '{} - Digging {}'.format(index, domain)
        try:
            command_out = subprocess.check_output(['dig', domain]).split('\n')
            start_index = 0
            end_index = 0
            for index, data in enumerate(command_out):
                if 'HEADER' in data:
                    start_index = index
                if 'Query time' in data:
                    end_index = index
            command_out = '\n'.join(command_out[start_index:end_index])

            output_file.write(os.linesep + command_out)
            output_file.write('\n\n')
        except Exception as e:
            print 'ERROR  ::  ', e
    
    output_file.close()

    print '***** task finished *****'

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: python {} <file name>'.format(sys.argv[0]) 
        print ''
        sys.exit(0)
    else:
        subprocess.call(['clear'], shell=True)
        main(file_name=sys.argv[1])
