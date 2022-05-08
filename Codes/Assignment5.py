# CBSE Probability Grade 12
# Example 11

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
An unbiased die is thrown twice. Let the event A be odd number on the first throw and B the event
 odd number on the second throw. Check the independence of the events A and B.
"""


def main():
    S = 36  # Number of elements in S
    A = 18  # Number of elements in A
    B = 18  # Number of elements in B
    A_B = 9 # Number of elements common in A and B 

    if( Prob_AB(S,A_B) == Prob_A(S,A)*Prob_B(S,B) ):
       print("Independent events")
    else:
       print("Dependent events")
         
def Prob_A(s,a) -> float:
        """ Returns the probability that event A occurs """
        return a/s

def Prob_B(s,b) -> float:
        """ Returns the probability that event B occurs """
        return b/s

def Prob_AB(s,a_b) -> float:
        """ Returns the probability that event A and B occurs """
        return a_b/s

if __name__ == '__main__':
       main()