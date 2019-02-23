
import sys
from shutil import copyfile

submissionFileName = sys.argv[1]
copyfile(submissionFileName, "student_code.py")

import student_code as sc


def checkGetInputs():
    originalStdOut = sys.stdout
    sys.stdout = open("output.txt", 'w')
    try:
        input1, input2, input3, input4, input5 = sc.getInputs()
    except:
        return "Defined but NOT OK"

    sys.stdout = originalStdOut

    if input1 == "medium-ranked" and input2 == 3.8 and input3 == 103 and input4 == 306 and input5 == 1:
        return "Defined and OK"

    return "Defined but NOT OK"


def checkComputeNormGPA():
    result1 = sc.computeNormGPA("high-ranked", 4.0)
    result2 = sc.computeNormGPA("low-ranked", 3.6)

    if result1 == 1.0 and result2 == 0.81:
        return "Defined and OK"


    return "Defined but NOT OK"


def checkComputeNormTestScore():
    result = sc.computeNormTestScore(95, 323)

    if result == 0.855:
        return "Defined and OK"

    return "Defined but NOT OK"

def checkComputeNormPubScore():
    result1 = sc.computeNormPubScore(3)
    result2 = sc.computeNormPubScore(1)

    if result1 == 1.0 and result2 == 0.5:
        return "Defined and OK"

    return "Defined but NOT OK"

def checkComputeNormTotalScore():
    result = sc.computeNormTotalScore("low-ranked", 4.0, 112, 319, 2)
    result = float("{0:.4f}".format(result))

    if result == 0.9306:
        return "Defined and OK"

    return "Defined but NOT OK"

def checkFindBestCandidate():
    originalStdOut = sys.stdout

    sys.stdout = open("output.txt", 'w')

    try:
        sc.findBestCandidate()
    except:
        return "Defined but NOT OK"

    sys.stdout = originalStdOut


    outputFile = open ('output.txt')

    linesInOutput = [line.rstrip() for line in outputFile]
    linesInOutput = [line for line in linesInOutput if line]

    score1 = -0.1
    score2 = -0.1
    score3 = -0.1
    bestCandidate = ""

    try:
        for token in linesInOutput[-4].split(' '):
            if token.strip().replace('.', '', 1).isdigit():
                score1 = float(token.strip())

        for token in linesInOutput[-3].split(' '):
            if token.strip().replace('.', '', 1).isdigit():
                score2 = float(token.strip())

        for token in linesInOutput[-2].split(' '):
            if token.strip().replace('.', '', 1).isdigit():
                score3 = float(token.strip())


        if "third" in linesInOutput[-1] and "best" in linesInOutput[-1]:
            bestCandidate = "OK"
    except:
        return "Defined but NOT OK"

    if bestCandidate == "OK" and score1 == 0.8375 and score2 == 0.7177 and score3 == 0.9306:
        return "Defined and OK"

    return "Defined but NOT OK"

def checkSubmissionFile(submissionFile):
    try:
        submissionFiletokens = submissionFile.split(".")

        fileExtension = submissionFiletokens[1]
        fileName = submissionFiletokens[0]
        fileNameTokens = fileName.split("_")

        if (len(fileNameTokens) != 4 or fileExtension != "py" or (not fileNameTokens[2].isdigit())):
            print("Incorrect Naming for the file.")
            print("Please change your file name to firstName_lastName_studentId_HW3.py")
            print("OTHERWISE, YOU WILL LOSE POINTS")

    except:
        print("Incorrect Naming for the file.")
        print("Please change your file name to firstName_lastName_studentId_HW2.py")
        print("OTHERWISE, YOU WILL LOSE POINTS")

def checkCode (submissionFileName):

    getInputsOK = "Not Defined"
    computeNormGPAOK = "Not Defined"
    computeNormTestScoreOK = "Not Defined"
    computeNormPubScoreOK = "Not Defined"
    computeNormTotalScoreOK = "Not Defined"
    findBestCandidateOK = "Not Defined"

    submissionFile = open(submissionFileName)
    lines = submissionFile.readlines()

    for line in lines:
        if "getInputs" in line:
            getInputsOK = "Defined but not OK"
        if "computeNormGPA" in line:
            computeNormGPAOK = "Defined but not OK"
        if "computeNormTestScore" in line:
            computeNormTestScoreOK = "Defined but not OK"
        if "computeNormPubScore" in line:
            computeNormPubScoreOK = "Defined but not OK"
        if "computeNormTotalScore" in line:
            computeNormTotalScoreOK = "Defined but not OK"
        if "findBestCandidate" in line:
            findBestCandidateOK = "Defined but not OK"

    if computeNormGPAOK == "Defined but not OK":
        computeNormGPAOK = checkComputeNormGPA()

    if computeNormTestScoreOK == "Defined but not OK":
        computeNormTestScoreOK = checkComputeNormTestScore()

    if computeNormPubScoreOK == "Defined but not OK":
        computeNormPubScoreOK = checkComputeNormPubScore()

    if computeNormTotalScoreOK == "Defined but not OK":
        computeNormTotalScoreOK = checkComputeNormTotalScore()

    if findBestCandidateOK == "Defined but not OK":
        findBestCandidateOK = checkFindBestCandidate()

    if  getInputsOK == "Defined but not OK":
        getInputsOK = checkGetInputs()



    print("%-30s%-30s" % ("Function", "Result"))
    print("%-30s%-30s" % ("getInputs", getInputsOK))
    print("%-30s%-30s" % ("computeNormGPA", computeNormGPAOK))
    print("%-30s%-30s" % ("computeNormTestScore", computeNormTestScoreOK))
    print("%-30s%-30s" % ("computeNormPubScore", computeNormPubScoreOK))
    print("%-30s%-30s" % ("computeNormTotalScore", computeNormTotalScoreOK))
    print("%-30s%-30s" % ("findBestCandidate", findBestCandidateOK))

def checkSubmission():
    checkSubmissionFile(submissionFileName)
    checkCode(submissionFileName)


if __name__ == "__main__":
    checkSubmission()



