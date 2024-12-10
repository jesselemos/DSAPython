using System.Linq;

namespace Studies
{
    public class MergeSort
    {
        public int[] MergeSortWithNewArrays(int[] array)
        {
            if (array.Length <= 1)
                return array;

            var midle = array.Length / 2;
            var left = MergeSortWithNewArrays(array.Take(midle).ToArray());
            var rigth = MergeSortWithNewArrays(array.Skip(midle).ToArray());

            return MergeWithNewArrays(left, rigth);
        }

        private int[] MergeWithNewArrays(int[] left, int[] right)
        {
            var totalElements = left.Length + right.Length;
            var newArray = new int[totalElements];
            var leftIndex = 0;
            var rightIndex = 0;
            var newArrayIndex = 0;

            while (leftIndex < left.Length || rightIndex < right.Length)
            {
                if (rightIndex >= right.Length || (leftIndex < left.Length && left[leftIndex] < right[rightIndex]))
                {
                    newArray[newArrayIndex] = left[leftIndex];
                    leftIndex++;
                }
                else
                {
                    newArray[newArrayIndex] = right[rightIndex];
                    rightIndex++;
                }
                newArrayIndex++;
            }

            return newArray;
        }

        public void MergeSortWithNoNewArrays(int[] array, int start, int end)
        {
            int length = end - start;
            if (length <= 1)
                return;

            int middle = start + (length / 2);
            MergeSortWithNoNewArrays(array, start, middle);
            MergeSortWithNoNewArrays(array, middle, end);

            MergeWithNoNewArrays(array, start, middle, end);
        }

        private void MergeWithNoNewArrays(int[] array, int start, int middle, int end)
        {
            var leftIndex = start;
            int rightIndex = middle;
            while(leftIndex < rightIndex && rightIndex < end)
            {
                if (array[rightIndex] >= array[leftIndex])
                {
                    leftIndex++;
                    continue;
                }

                int temp = array[rightIndex];
                for(int index = rightIndex; index > leftIndex; index--)
                {
                    array[index] = array[index - 1];
                }
                array[leftIndex] = temp;

                leftIndex++;
                rightIndex++;
            }
        }
    }
}
