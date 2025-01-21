namespace Studies
{
    public class Stack<T>
    {
        private Node<T> Head;
        public bool IsEmpty => Head.IsEmpty;

        public Stack()
        {
            Head = Node<T>.Empty();
        }

        public Stack<T> Add(T value)
        {
            var node = Node<T>.Create(value, Head);
            Head = node;
            return this;
        }

        public T Pop()
        {
            if (IsEmpty)
                throw new System.InvalidOperationException();

            var value = Head.Value;
            Head = Head.Tail;
            return value;
        }

        public T Peek()
            => Head.Value;
    }

}
