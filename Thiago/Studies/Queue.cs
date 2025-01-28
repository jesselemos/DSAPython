namespace Studies
{
    public class Queue<T>
    {
        private Node<T> Head;
        private Node<T> Tail;
        public bool IsEmpty => Head.IsEmpty;

        public Queue()
        {
            Head = Node<T>.Empty();
            Tail = Head;
        }

        public Queue<T> Enqueue(T value)
        {
            if (IsEmpty)
            {
                Head = Node<T>.Create(value, Tail);
                Tail = Head;
                return this;
            }

            var node = Node<T>.Create(value, Tail.Next);
            Tail.UpdateNext(node);
            Tail = node;
            return this;
        }

        public T Dequeue()
        {
            if (IsEmpty)
                throw new System.InvalidOperationException();

            var value = Head.Value;
            Head = Head.Next;
            return value;
        }

        public T Peek()
        {
            if (IsEmpty)
                throw new System.InvalidOperationException();

            return Head.Value;
        }
    }
}
