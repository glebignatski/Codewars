public class CountingDuplicates {
  public static int duplicateCount(String text) {
      char[] ch_array = text.toCharArray();   // "abcd" -> 'a', 'b', 'c', 'd'
      int[] num_chars = new int[text.length()];
      for(int i = 0; i < text.length(); i++){
        //num_chars[i] = 1;             // the char occured at least once at a position in text
        ch_array[i] = text.charAt(i); // load chars of text into ch_array[]      
        if(Character.isUpperCase(ch_array[i])){
          ch_array[i] = Character.toLowerCase(ch_array[i]);
        }
      }
      // abcdffaabdfd -> a = 3, b = 2, d = 3, f = 3, 
      for(int i = 0; i < text.length(); i++){
        char ch = ch_array[i];
        for(int j = 0; j < text.length(); j++){
        if(ch != '\0'){
          if(ch_array[j] == ch_array[i] && i != j){ // blank out the char
            num_chars[i] = 1;
            ch_array[j] = '\0';
          }
          }
        }
      }
      // "aabBcdde"
      // arr[0] = 2
      // "0abBcdde"
      // arr[1] = 
      int mult = 0;
      for(int i = 0; i < num_chars.length; i++){
        if(num_chars[i] == 1 ){
          mult++;
        }
      }
      
      return mult;
    }
}