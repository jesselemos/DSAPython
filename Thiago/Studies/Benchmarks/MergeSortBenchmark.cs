using BenchmarkDotNet.Attributes;
using System;
using System.Linq;

namespace Studies.Benchmarks
{
    [MemoryDiagnoser(true)]
    public class MergeSortBenchmark
    {
        private static MergeSort _mergeSort = new MergeSort();
        private static int _count = 100_000;

        public static int[] GetReversedArray()
        {
            var array = new int[_count];
            for (var index = _count; index > 0; index--)
                array[index - 1] = index;

            return array;
        }

        private static int[] GetRandomArray()
        {
            var random = new Random();
            var array = new int[_count];
            for (var index = _count; index > 0; index--)
                array[index - 1] = random.Next(0, _count);

            return array;
        }

        [Benchmark]
        public void MergeSortWithNewArraysReversedArray()
        {
            var array = GetReversedArray();
            _mergeSort.MergeSortWithNewArrays(array);
        }

        [Benchmark]
        public void MergeSortWithNewArraysRandomCaseScenario()
        {
            var array = GetRandomArray();
            _mergeSort.MergeSortWithNewArrays(array);
        }

        [Benchmark]
        public void MergeSortWith_No_NewArraysReversedArray()
        {
            var array = GetReversedArray();
            _mergeSort.MergeSortWithNoNewArrays(array, 0, array.Length);
        }

        [Benchmark]
        public void MergeSortWith_No_NewArraysRandomCaseScenario()
        {
            var array = GetRandomArray();
            _mergeSort.MergeSortWithNoNewArrays(array, 0, array.Length);
        }
    }
}
