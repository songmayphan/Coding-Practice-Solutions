public class Positive{

   public static int sum(int[] arr){
      int sum = 0;
      for (int i = 0; i < arr.length; i++) {
         if ( arr[i] < 0 ) {
            continue;
         }
         else { sum += arr[i];
         }
      }
      return sum;
   }
   public static void main (String [] args) {
   
      int [] arr = {1, -1, 4}; 
      int sum = sum(arr);
      System.out.println(sum); 
   }
}
