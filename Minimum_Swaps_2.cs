using System;

class Solution {

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int _switch = 0;
        foreach (int ii in arr)
        {
            int ii_index = Array.IndexOf(arr, ii) + 1;
            if (ii != ii_index)
            {
                int memo = arr[ii - 1];
                arr[ii - 1] = ii;
                arr[ii_index - 1] = memo;
                _switch++;
            }
        }

        return _switch;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
        ;
        int res = minimumSwaps(arr);

        textWriter.WriteLine(res);

        textWriter.Flush();
        textWriter.Close();
    }
}
