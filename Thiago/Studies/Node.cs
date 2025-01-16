namespace Studies
{
    public class Node<T>
    {
        public T Value { get; }
        public Node<T> Tail { get; set; }

        public Node(T value)
        {
            Value = value;
        }
    }
}
