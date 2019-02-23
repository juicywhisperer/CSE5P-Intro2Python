def getInputs():
    ranking = str(input("Enter undergraduate university ranking (low-ranked, medium-ranked, high-ranked): "))
    GPA = float(input("Enter undergraduate GPA (0.0 - 4.0): "))
    TOEFL = int(input("Enter TOEFL score (0-120): "))
    GRE = int(input("Enter GRE score (260-340): "))
    pub = int(input("Enter the number of publications: "))
    return (ranking,GPA,TOEFL,GRE,pub)

def computeNormGPA(ranking,GPA):
    if ranking == 'low-ranked':
        rank_weight = 0.9
    elif ranking == 'medium-ranked':
        rank_weight = 1.0
    elif ranking == 'high-ranked':
        rank_weight = 1.1
    norm_GPA = (rank_weight * GPA) / 4
    if norm_GPA > 1:
        norm_GPA = 1.0
    return norm_GPA

def computeNormTestScore(TOEFL,GRE):
    norm_test_score = ( 0.6 * (TOEFL / 120) + 0.4 * (GRE / 340))
    return norm_test_score

def computeNormPubScore(pub):
    if pub == 0:
        norm_pub_score = 0.0
    elif pub == 1:
        norm_pub_score = 0.5
    else:
        norm_pub_score = 1.0
    return norm_pub_score

def computeNormTotalScore(ranking,GPA,TOEFL,GRE,pub):
    norm_GPA = computeNormGPA(ranking,GPA)
    norm_test_score = computeNormTestScore(TOEFL,GRE)
    norm_pub_score = computeNormPubScore(pub)
    norm_total_score = (0.5 * norm_GPA + 0.3 * norm_test_score + 0.2 * norm_pub_score)
    return norm_total_score

def findBestCandidate():
    while True:
        i = 1
        while i <= 3:
            if i == 1:
                (ranking,GPA,TOEFL,GRE,pub) = getInputs()
                s1 = computeNormTotalScore(ranking,GPA,TOEFL,GRE,pub)
                i += 1
            elif i == 2:
                (ranking,GPA,TOEFL,GRE,pub) = getInputs()
                s2 = computeNormTotalScore(ranking,GPA,TOEFL,GRE,pub)
                i += 1
            elif i == 3:
                (ranking,GPA,TOEFL,GRE,pub) = getInputs()
                s3 = computeNormTotalScore(ranking,GPA,TOEFL,GRE,pub)
                i += 1
        print("Normalized total score of the first applicant is:" , "%.4f" % s1)
        print("Normalized total score of the second applicant is:" , "%.4f" % s2)
        print("Normalized total score of the third applicant is:" , "%.4f" % s3)
        if s1 == max(s1,s2,s3):
            s_best = 'first'
        elif s2 == max(s1,s2,s3):
            s_best = 'second'
        elif s3 == max(s1,s2,s3):
            s_best = 'third'
        print("The",s_best,"applicant is the best candidate.",sep=' ')