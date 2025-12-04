import argparse
import sys

def read_file(filename):
    """Reads a file"""
    with open(filename, 'r') as f:
        return f.read()
    
def main():
    parser = argparse.ArgumentParser(
        description="ccut command"
    )

    parser.add_argument('filename', nargs='?', default=None,
                        help="filename to read")
    parser.add_argument('-f', "--fields",type=str,
                        help="Returns only the second field of the line")
    parser.add_argument('-d', "--delimiter", type=str, default='\t',
                        help="Specify a delimeter")
    
    args = parser.parse_args()

    content = ''
    try:
        if args.filename:
            content = read_file(args.filename)
        else:
            content = sys.stdin.buffer.read()
    except FileNotFoundError:
        print(f'file {args.filename} does not exist', file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f'You do not have permission to read this file {args.filename}', file=sys.stderr)
        exit(1)
    except IOError as e:
        print(f'An IO error occured : {e}', file=sys.stderr)
    
    delimiter = args.delimiter
    fields = []
    if args.fields.find(",") != -1:
        fields = args.fields.split(',')
    elif args.fields.find(" ") != -1:
        fields = args.fields.split()
    
    lines = content.rstrip().split('\n')
    if fields:
        output = ""
        for l in lines:
            line_output = ""
            for field in fields:
                line_output += f"{l.split(delimiter)[int(field)]}\t"
            output += f"{line_output}\n"

        print(output, file=sys.stdout)


if __name__ == '__main__':
    main()