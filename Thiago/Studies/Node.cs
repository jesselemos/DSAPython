namespace Studies
{
    public abstract class Node<T>
    {
        public abstract T Value { get; }
        public abstract Node<T> Tail { get; }
        public abstract bool IsEmpty { get; }

        public static Node<T> Empty()
        {
            return new EmptyNode();
        }

        public static Node<T> Create(T value, Node<T> tail)
        {
            if (tail is null)
                throw new System.ArgumentNullException();

            return new NotEmptyNode(value, tail);
        }

        private class NotEmptyNode : Node<T>
        {
            public NotEmptyNode(T value, Node<T> tail)
            {
                Value = value;
                Tail = tail;
            }

            public override bool IsEmpty => false;

            public override T Value { get; }

            public override Node<T> Tail { get; }
        }

        private class EmptyNode : Node<T>
        {
            public override bool IsEmpty => true;

            public override T Value => throw new System.NotImplementedException();

            public override Node<T> Tail => throw new System.NotImplementedException();
        }
    }
}
