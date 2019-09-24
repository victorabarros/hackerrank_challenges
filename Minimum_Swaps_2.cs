using System.IO;
using System;

public class Solution {
    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int switchs = 0;
        int iterable = 0;

        while (true)
        {
            int ii = arr[iterable];
            int ii_index = Array.IndexOf(arr, ii) + 1;
            if (ii != ii_index)
            {
                int memo = arr[ii - 1];
                arr[ii - 1] = ii;
                arr[ii_index - 1] = memo;
                switchs++;
            }
            else
            {
                iterable++;
            }
            // System.Console.WriteLine(arr[0].ToString() + arr[1].ToString() + arr[2].ToString() + arr[3].ToString());
            if (iterable == arr.Length)
            {
                break;
            }
        }

    return switchs;
    }

    public static void Main() {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));

        // int[] arr = new int[4] {4, 3, 1, 2};
        int res = minimumSwaps(arr);
        // System.Console.WriteLine(res);

        textWriter.WriteLine(res);

        textWriter.Flush();
        textWriter.Close();
    }
}
