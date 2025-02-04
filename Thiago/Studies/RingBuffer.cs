namespace Studies
{
    public class RingBuffer<T>
    {
        private T[] Buffer;
        private int Length;
        private int Size;
        private int IndexHead;
        private int IndexTail;
        private bool IsFull => Length == Size;
        public bool IsEmpty => Length == 0;

        public RingBuffer(int size)
        {
            Size = size;
            Length = 0;
            IndexHead = 0;
            IndexTail = 0;
            Buffer = new T[size];
        }

        public RingBuffer<T> Enqueue(T value)
        {
            if (IsFull)
                IncreaseBuffer();

            Buffer[IndexHead] = value;
            IndexHead = (IndexHead + 1) % Size;
            Length++;

            return this;
        }

        private void IncreaseBuffer()
        {
            var newSize = Size * 2;
            var newBuffer = new T[newSize];
            var index = 0;

            while(!IsEmpty)
            {
                newBuffer[index] = Dequeue();
                index++;
            }

            Size = newSize;
            Buffer = newBuffer;
            IndexHead = index;
            IndexTail = 0;
            Length = index;
        }

        public T Dequeue()
        {
            if (IsEmpty)
                throw new System.Exception();

            var value = Buffer[IndexTail];
            IndexTail = (IndexTail + 1) % Size;
            Length--;
            return value;
        }
    }
}