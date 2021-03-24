def arithmetic_arranger(problems, doCalculation=False):
    '''
    Sample: ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True
    '''

    if not isinstance(problems, list):
        return 'Error: Argument problems should be list.'

    if len(problems) == 0:
        return 'Error: Argument problems shold have at least one question.'

    if len(problems) > 5:
        return 'Error: Too many problems.'

    answers = []

    for problem in problems:
        msg = hasError(problem)
        if (len(msg) > 0):
            return msg
        result = calculateProblem(problem)
        answers.append(result)

    str = renderResults(answers, doCalculation)
    return str


def hasError(problem):
    targets = problem.split()

    if len(targets) != 3:
        return "Error: Invalid question."

    if targets.count('+') == 0 and targets.count('-') == 0:
        return "Error: Operator must be '+' or '-'."

    if len(targets[0]) > 4 or len(targets[2]) > 4:
        return "Error: Numbers cannot be more than four digits."

    try:
        int(targets[0])
    except ValueError:
        return "Error: Numbers must only contain digits."

    try:
        int(targets[2])
    except ValueError:
        return "Error: Numbers must only contain digits."

    return ""

# 実際の計算をして結果を配列にして返します


def calculateProblem(problem):
    targets = problem.split()
    result = eval(problem)

    targets.append(separateLine(targets[0], targets[2]))
    targets.append(result)

    return targets


def separateLine(firstNum, secondNum):
    count = len(firstNum)
    if (len(secondNum) > count):
        count = len(secondNum)

    result = "-" * count + "--"
    return result


def renderResults(results, includeSolved=False):
    firstLine = []
    secondLine = []
    sepalator = []
    resultLine = []

    for result in results:
        baseLength = len(result[0])
        if (len(result[1]) > baseLength):
            baseLength = len(result[1])
        baseLength += 1

        firstLine.append(result[0].rjust(len(result[3])))

        second = result[1] + "" + result[2].rjust(len(result[3]) - 1)
        secondLine.append(second)
        sepalator.append(result[3])

        if (includeSolved):
            resultLine.append(str(result[4]).rjust(len(result[3])))

    resultString = '    '.join(firstLine) + '\n'
    resultString += '    '.join(secondLine) + '\n'
    resultString += '    '.join(sepalator)
    if (includeSolved):
        resultString += '\n' + '    '.join(resultLine)

    return resultString
