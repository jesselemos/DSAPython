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
            var math = "{((2+1)*[2+1])}";
            var stack = new Stack<char>();
            var possibilities = new Dictionary<char, char>();
            var isValid = true;

            possibilities.Add('{', '}');
            possibilities.Add('(', ')');
            possibilities.Add('[', ']');

            foreach (var m in math)
            {
                if (possibilities.ContainsKey(m))
                {
                    stack.Add(m);
                    continue;
                }

                if (possibilities.Values.Contains(m))
                {
                    if (stack.IsEmpty)
                    {
                        isValid = false;
                        break;
                    }

                    var value = stack.Pop();
                    if(possibilities[value] != m)
                    {
                        isValid = false;
                        break;
                    }
                }
            }

            Console.WriteLine($"is {(isValid ? "Valid": "Invalid")}");


            //var stack = new Stack<int>()
            //    .Add(5)
            //    .Add(4)
            //    .Add(3)
            //    .Add(2)
            //    .Add(1);

            //while (!stack.IsEmpty)
            //{
            //    Console.WriteLine(stack.Pop());
            //}



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
