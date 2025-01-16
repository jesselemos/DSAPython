namespace Studies
{
    public class Stack<T>
    {
        private Node<T> Head;
        public bool IsEmpty => Head is null;

        public Stack<T> Add(T value)
        {
            var node = new Node<T>(value);
            if(IsEmpty)
            {
                Head = node;
                return this;
            }

            node.Tail = Head;
            Head = node;
            return this;
        }

        public T Pop()
        {
            var value = Head.Value;
            Head = Head.Tail;
            return value;
        }
    }

}
