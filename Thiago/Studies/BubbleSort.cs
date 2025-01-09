using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Studies
{
    /*
     BubbleSort (Bolha) its idea is get the biggest array number and bring it to the lastest position of the array
     */
    internal class BubbleSort
    {

        public int[] SortArray(int[] toSort)
        {
            for (int j = 0; j < toSort.Length - 1; j++)
            {
                var swapped = false;
                for (int i = 0; i < toSort.Length - j - 1; i++)
                {
                    if (toSort[i] > toSort[i + 1])
                    {
                        var aux = toSort[i];
                        toSort[i] = toSort[i + 1];
                        toSort[i + 1] = aux;
                        swapped = true;
                    }
                }
                if (!swapped) break;
            }

            return toSort;
        }

        /*1 2 3
          4 3 5

         */
    }
}
