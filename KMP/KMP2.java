/* version in lecture notes

use mutually recursive calls
*/

import java.io.*;

public class KMP2{

    private int[] Prefix;

    private KMP2(String pattern){
        // Prefix = new int[pattern.length()];
        // for(int i = 0; i < pattern.length(); i++){
        //     Prefix[i] = -1;
        // }
    }

    // Specification: Given Q and 0 <= j < #pattern, return 
    // length of longest Prefix of pattern that is a suffix of 
    // pattern[0..j-1]+c.
    private int extend(String pattern, int j, char c){
        if (pattern.charAt(j) == c)
            return j + 1;
        if (j == 0)
            return 0;
        return extend(pattern, prefix(pattern, j), c);
    }

    // Specification: Given Q and 0 < i < #pattern, return length
    // of longest proper Prefix of pattern[0..i-1] that is a suffix
    // of pattern[0..i-1]. Also, store Prefix, in order to maintain Q
    private int prefix(String pattern, int i){
        if (Prefix[i] == -1)
            if (i == 1)
                Prefix[i] = 0;
            else
                Prefix[i] = extend(pattern, prefix(pattern, i-1), pattern.charAt(i-1));
        return Prefix[i];
    }

    // Specification: compute the Prefix array with the aid of extend and Prefix function
    private void computePrefix(String pattern){
        Prefix = new int[pattern.length()];
        for (int i = 0; i < pattern.length(); i++) {
            Prefix[i] = -1;
        }
        // extend(pattern, prefix(pattern, pattern.length()-1), pattern.charAt(pattern.length()-1));
        prefix(pattern, pattern.length()-1);
    }

    public static void main(String[] args){
        String pattern = "abcabcacab";
        KMP2 kmpobj = new KMP2(pattern);
        kmpobj.computePrefix(pattern);
        for (int val : kmpobj.Prefix){
            System.out.print((val));
        }
    }

}




