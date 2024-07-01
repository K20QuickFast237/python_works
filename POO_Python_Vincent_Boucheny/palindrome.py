# class to test if word is a palindrome

class Palindrome:
    def __init__(self, word):
        """
            Initializes a new instance of the class.
            
            Parameters:
                word (str): The word to be assigned to the `mot` variable.
        """
        self.mot = word

    def __del__(self):
        """
            Destructor method for the class.

            This method is automatically called when the object is about to be destroyed.
            It prints the uppercase version of the variable 'mot' to the console.

            Parameters:
            None

            Returns:
            None
        """
        print(self.mot.upper())

    def test(self):
        """
            This function is used to test if the instance variable mot is a palindrome.

            Parameters:
                self (object): The instance of the class.
            
            Returns:
                The result of the palindrome test for the instance variable mot.
        """
        return Palindrome.estpalindrome(self.mot)
        
    def estpalindrome(word):
        """
            Check if a word is a palindrome.

            Args:
                word (str): The word to check.

            Returns:
                bool: True if the word is a palindrome, False otherwise.
        """
        return word == word[::-1]



if __name__ == "__main__":
    # print(Palindrome.estpalindrome("radar"))
    # print(Palindrome.estpalindrome("sonar"))
    # print(Palindrome.estpalindrome("Engage le jeu que je le gagne"))
    # print(Palindrome.estpalindrome("engagelejeuquejelegagne"))
    # print(Palindrome.estpalindrome("!@#$% %$#@!"))
    # print(Palindrome.estpalindrome("L O L"))

    p = Palindrome("radar")
    print(p.test())
    p = Palindrome("sonar")
    print(p.test())