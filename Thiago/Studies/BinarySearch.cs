namespace Studies
{
    public class BinarySearch
    {
        public int Search(int[] orderedArray, int value, int start, int end)
        {
            while(start < end)
            {
                var middle = start + (end - start) / 2;

                if (orderedArray[middle] == value)
                    return middle;

                if (orderedArray[middle] > value)
                    end = middle;
                else
                    start = middle + 1;
            }

            return -1;
        }

        public int SearchRec(int[] orderedArray, int value, int start, int end)
        {
            if (start >= end)
                return -1;

            var middle = start + (end - start) / 2;
            if (orderedArray[middle] == value)
                return middle;

            if (orderedArray[middle] > value)
                end = middle;
            else
                start = middle + 1;

            return SearchRec(orderedArray, value, start, end);
        }
    }
}
