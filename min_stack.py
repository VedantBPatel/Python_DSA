class Minstack:
    def __init__(st, capacity):
        st.capacity = capacity
        st.top = -1
        st.stack = [None] * capacity
        st.min_stack = [None] * capacity

    def isEmpty(st):
        return st.top == -1
    
    def isFull(st):
        return st.top == st.capacity - 1
    
    def push(st, data):
        if st.isFull():
            return "Stack Overflow"
        
        st.top += 1
        st.stack[st.top] = data

        if st.top == 0 or data <= st.min_stack[st.top - 1]:
            st.min_stack[st.top] = data
        else:
            st.min_stack[st.top] = st.min_stack[st.top - 1]
        
    def pop(st):
        if st.isEmpty():
            print("Stack underflow")
            return None
        popped_value = st.stack[st.top]
        st.top -= 1
        return popped_value  # No need to pop from fixed-size min_stack
    
    def top_element(st):
        if st.isEmpty():
            return "Stack is empty"
        return st.stack[st.top]
    
    def getMin(st):
        if st.isEmpty():
            return "Min stack is Empty"
        return st.min_stack[st.top]
    
    def display(st):
        print("Main Stack:", st.stack[:st.top + 1])
        print("Min Stack:", st.min_stack[:st.top + 1])


def run(st):
    while True:
        print("\nOperations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Top Element")
        print("4. Get Minimum Element")
        print("5. Display Stack")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter a value to be pushed: "))
            result = st.push(value)
            if result == "Stack Overflow":
                print(result)
            else:
                print(f"{value} pushed")

        elif choice == 2:
            value = st.pop()
            if value is None:
                print("Stack underflow")
            else:
                print(f"{value} popped")

        elif choice == 3:
            top_element = st.top_element()
            print(f"Top Element is: {top_element}")

        elif choice == 4:
            min_element = st.getMin()
            print(f"Current Min Element is: {min_element}")

        elif choice == 5:
            st.display()

        elif choice == 6:
            print("EXITING......")
            break

        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    capacity = int(input("\nEnter the size of the stack: "))
    st = Minstack(capacity)  # Create an instance of Minstack
    run(st)  # Pass the stack object to the run function
