import sys, os

# preprocessing!
tc = os.path.join(os.getcwd(), 'tc')
if not os.path.exists(tc):
    os.mkdir(tc)

def createFolders():
    num = input('Enter num or names: ')
    if num.isdigit():
        for i in range(int(num)):
            os.mkdir(os.path.join(tc, chr(i + ord('a'))))
    elif num:
        for name in num.split():
            os.mkdir(os.path.join(tc, name))
    else:
        sys.exit("folder names can't empty!")

def testCounter(problemFolder):
    result = 1
    while os.path.exists(os.path.join(problemFolder, str(result) + '.in')) and os.path.exists(os.path.join(problemFolder, str(result) + '.ans')):
        result += 1
    return result - 1

def textInput():
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return '\n'.join(lines)

def addTestcase(folder, num):
    print('Enter input:')
    in_f = textInput()
    print('Enter output:')
    out_f = textInput()
    with open(os.path.join(folder, num + '.in'), 'w') as ifile, open(os.path.join(folder, num + '.ans'), 'w') as ofile:
        ifile.write(in_f)
        ofile.write(out_f)

def createTest(problem):
    problemFolder = os.path.join(os.getcwd(), 'tc', problem)
    if not os.path.exists(problemFolder):
        sys.exit(f'problem {problem} not found!')
    testNum = testCounter(problemFolder)
    num = input(f'Availabe test(s): {testNum}, how many to add? ')
    num = int(num) if num.isdigit() else 0
    for i in range(num):
        print(f'Test case number {i + 1 + testNum}...')
        addTestcase(problemFolder, str(i + 1 + testNum))

def totalAdding():
    entries = os.listdir(tc)
    folders = [entry for entry in entries if os.path.isdir(os.path.join(tc, entry))]
    folders.sort()
    for problem in folders:
        print(f'Problem {problem}...')
        createTest(problem)

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 tca.py <command>")

    command = sys.argv[1]

    if command == "+":
        createFolders()
    elif command == ".":
        totalAdding()
    else:
        createTest(command)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(f'Error in runtime: {e}')