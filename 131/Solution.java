
public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> palindrionStr = new ArrayList<List<String>> ();
        recursivepartition(palindrionStr, s, 0, 1, s.length());
	    return palindrionStr;
    }

    private void recursivepartition (List<List<String>> result, String str, int start, int length, int maxlength) {
    	if ((start + length) > str.length()) {
    		return;
    	}
    	if (start == 0) {
	    	for (int i = 1; i <= str.length(); i++) {
    	    	recursivepartition(result, str, 0, i, maxlength);
        	}
        }
    	String tmpstr = str.substring (start, start + length);
    	if (isPalindrome(tmpstr)) {
    		if (str.length() == maxlength) {
    			List<String> tmplist = new ArrayList<String> ();
    			tmplist.add(tmpstr);
    			result.add (0, tmplist);
    		} else {
    			result.get (0).add(tmpstr);
    		}
    		recursivepartition (result, str.substring(start + length), 0, 1, maxlength);
    	} else {
    		recursivepartition (result, str, start, length + 1, maxlength);
    	}

    }

    private boolean isPalindrome (String s) {
    	int i = 0;
    	int j = s.length() - 1;
    	while (i <= j) {
    		if (s.charAt(i++) == s.charAt(j--)) {
    		}
    		else
    			return false;		
    	}
    	return true;

    }
}