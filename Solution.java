/*Complete the method/function so that it converts
 *  dash/underscore delimited words into camel casing. 
 * The first word within the output should be capitalized
 *  only if the original word was capitalized.

Examples
toCamelCase("the-stealth-warrior"); 
// returns "theStealthWarrior"

toCamelCase("The_Stealth_Warrior");
 // returns "TheStealthWarrior"
 * 
 * 
 * 
 */

import java.lang.StringBuilder;
class Solution{

  static String toCamelCase(String s){
	String dash = "-";
	String[] tokens = s.split(dash); 
	String answer ="";
	
	for(int i = 0; i < tokens.length; i++ ) { 
		for (int j = 0; j < tokens[i].length(); j++) { 
			char c = tokens[i].charAt(j);
			char first = tokens[i].charAt(0);
			if (Character.isUpperCase(first)) { 
				answer = answer + tokens[i];
			} 
			
			else { 
			
			answer = answer + tokens[i];
			}
			
			
					 
		
	}
		 
		 
		 
		 
		 
	 }
    return "";
  }
}