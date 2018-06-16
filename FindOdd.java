public class FindOdd {
	public static int findIt(int[] a) {
    int count = 0;
    int i;
    int j;
    for ( i = 0; i < a.length; i++){ 
      for(  j =0; j< a.length; j++) {
       if (a[i] == a[j]) count++;    
    }
      if (count % 2 != 0) return a[i];
  }
  	return -1;
  }
}