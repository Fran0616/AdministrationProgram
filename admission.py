#Francisco

#Function below will test to see if applicant meet requirement 
def AcceptOrReject(gpa, testScore):
    #if gpa is less than 3 the applicant test score has to be 80 or higher to get accepted. 
    if gpa < 3.0:
        if testScore > 80:
            return ("You been accepted")
        else:
            return("We appriciate your interest but you did not meet the requirement")
    #if applicant gpa is greater or equal to 3 than the applicant just need a test score of 60 or higher to get accepted
    elif gpa >= 3.0:
        if testScore > 60:
            return ("You been accepted")
        else:
            return("We appriciate your interest but you did not meet the requirement")
            
  
       
#main function for user input and callout the AcceptOrReject function
def main():
    #get user input for grade
    grade = float(input("Enter your GPA: "))
    #get user input for test score
    test = float(input("Enter your test score: "))
    #callout the AcceptOrReject function with the argumet grade and test to compute for the requirement
    print (AcceptOrReject(grade, test))
    
main()
