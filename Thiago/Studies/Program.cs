using Studies.Benchmarks;
using BenchmarkDotNet.Running;
using System;
using static JetBrains.FormatRipper.FileExplorer.FileTypeExplorer;
using System.Collections.Generic;
using System.Linq;

namespace Studies
{
    class Program
    {
        static void Main(string[] args)
        {

            var stack = new Stack<int>()
                .Add(5)
                .Add(4)
                .Add(3)
                .Add(2)
                .Add(1);

            while (!stack.IsEmpty)
            {
                Console.WriteLine(stack.Pop());
            }

            var queue = new Queue<int>()
                .Enqueue(5)
                .Enqueue(4)
                .Enqueue(3)
                .Enqueue(2)
                .Enqueue(1);

            while (!queue.IsEmpty)
            {
                Console.WriteLine(queue.Dequeue());
            }




            //BenchmarkRunner.Run<MergeSortBenchmark>();

            //int[] arr = new int[] { 1, 2, 3, 4 };

            //var bubble = new BubbleSort();
            //var ret = bubble.SortArray(arr);
            //Console.WriteLine($"{ret}");

            //var search = new BinarySearch();

            //for(var value = 0; value < 7; value++)
            //{
            //    var result = search.SearchRec(arr, value, 0, arr.Length);
            //    Console.WriteLine($"value= {value} index = {result}");
            //}

        }

    }
}
