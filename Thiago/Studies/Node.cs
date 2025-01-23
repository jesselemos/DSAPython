namespace Studies
{
    public abstract class Node<T>
    {
        public abstract T Value { get; }
        public abstract Node<T> Next { get; protected set; }
        public abstract bool IsEmpty { get; }

        public abstract void UpdateNext(Node<T> node);

        public static Node<T> Empty()
        {
            return new EmptyNode();
        }

        public static Node<T> Create(T value)
        {
            return new NotEmptyNode(value, Empty());
        }

        public static Node<T> Create(T value, Node<T> tail)
        {
            if (tail is not Node<T>)
                throw new System.ArgumentNullException();

            return new NotEmptyNode(value, tail);
        }

        private class NotEmptyNode : Node<T>
        {
            public NotEmptyNode(T value, Node<T> node)
            {
                Value = value;
                Next = node;
            }

            public override bool IsEmpty => false;

            public override T Value { get; }

            public override Node<T> Next { get; protected set; }

            public override void UpdateNext(Node<T> node)
            {
                if (node is not Node<T>)
                    throw new System.ArgumentNullException();

                Next = node;
            }
        }

        private class EmptyNode : Node<T>
        {
            public override bool IsEmpty => true;

            public override T Value => throw new System.NotImplementedException();

            public override Node<T> Next 
            {
                get => throw new System.NotImplementedException();
                protected set => throw new System.NotImplementedException();
            }

            public override void UpdateNext(Node<T> tail)
            {
                throw new System.NotImplementedException();
            }
        }
    }
}
