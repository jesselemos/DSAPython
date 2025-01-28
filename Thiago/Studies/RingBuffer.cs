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
            Buffer[IndexHead] = value;
            IndexHead = (IndexHead + 1) % Size;

            if (IsFull)
                IndexTail = (IndexTail + 1) % Size;
            else
                Length++;

            return this;
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


/*
def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item

def enqueue(self, item):
        if self.is_full():
            # Overwrite the oldest data if the buffer is full
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
 * */