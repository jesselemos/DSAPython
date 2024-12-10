using Studies.Benchmarks;
using BenchmarkDotNet.Running;

namespace Studies
{
    class Program
    {
        static void Main(string[] args)
        {
            BenchmarkRunner.Run<MergeSortBenchmark>();
        }

    }
}
