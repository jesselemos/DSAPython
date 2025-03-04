﻿namespace Studies
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
