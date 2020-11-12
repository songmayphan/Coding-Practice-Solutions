/*Write a function that takes in a string of one or more words, and returns the same string, 
 * but with all five or more letter words reversed
 * Strings passed in will consist of only letters and spaces. 
 * Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
 * 
 * 
 * December 30th 2018, from 8:54pm to 9:49pm 
 */
public class SpinWords {

  public String spinWords(String sentence) {
    //TODO: Code stuff here
	  String [] data = sentence.split(" "); 
		 String reverse = "";
		 String answer = "";

		 	
		 	for ( int i = 0 ; i < data.length; i++) {
		 		if (data[i].length() >= 5) {
		 			for ( int j = data[i].length() - 1; j >=0; j--) {
		 				reverse = reverse + data[i].charAt(j); 
		 			}
		 			answer = answer + reverse + " ";
               reverse = "";
		 			continue;
		 		}
            
		 		else {
               
		 			answer = answer + data[i] + " ";
               
		 		}
		 		
		 	}
         answer = answer.trim(); //remove white spaces in the beginning and end
		 	return answer;
	  }
  
}
