using Studies.Benchmarks;
using BenchmarkDotNet.Running;
using System;
using static JetBrains.FormatRipper.FileExplorer.FileTypeExplorer;

namespace Studies
{
    class Program
    {
        static void Main(string[] args)
        {
            //BenchmarkRunner.Run<MergeSortBenchmark>();

            int[] arr = new int[] { 1, 2, 3, 4 };

            var bubble = new BubbleSort();
            var ret = bubble.SortArray(arr);
            Console.WriteLine($"{ret}");

            //var search = new BinarySearch();

            //for(var value = 0; value < 7; value++)
            //{
            //    var result = search.SearchRec(arr, value, 0, arr.Length);
            //    Console.WriteLine($"value= {value} index = {result}");
            //}

        }

    }

}
