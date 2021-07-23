import sys, json
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

n = []
def main():
    lines = read_in()
    n = ["Holiday package", "Vacation"]
    for i in n:
        print(i,end=',');

if __name__ == '__main__':
    main()
