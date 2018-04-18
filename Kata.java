// Find a unique number in given array
 public class Kata {
    public static double findUniq(double arr[]) {
      // do the magic
      double num = arr[0];
      int i;
      double [] uniq = new double [arr.length]; 
      for (i = 0; i < arr.length ; i++)
      {
        if (arr[i] == arr[0])
        {
          continue;
        }
        else if ( arr[i] != arr[0] ) 
        {
          return arr[i];
        }
      }
      return arr[i];
    }
   
}
