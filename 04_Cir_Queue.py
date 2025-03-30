class Circular_Queue:
    def __init__(q,max_size):
        q.max_size=max_size
        q.queue=[None]*max_size
        q.front=-1
        q.rear=-1
    
    def isEmpty(q):
        return q.front==-1
    
    def isFull(q):
        return (q.rear+1)%q.max_size==q.front
    
    def enqueue(q,data):
        if q.isFull():
            print("Queue Overflow")
            return
        
        if q.isEmpty():
            q.front=0
            q.rear=0

        else:
            q.rear=(q.rear+1)%q.max_size
        
        q.queue[q.rear]=data
        print(f"Enqueued: {data}")

    def dequeue(q):
        if q.isEmpty():
            print("Queue Underflow\n")
            return -1
        
        print(f"Dequeued Element: {q.queue[q.front]}")
        if q.front==q.rear:
            q.front=-1
            q.rear=-1
        else:
            q.front=(q.front+1)%q.max_size
    
    def get_front(q):
        if q.isEmpty():
            print("Queue is Empty cannot get front")
            return -1
        return q.queue[q.front]
    
    def get_rear(q):
        if q.isEmpty():
            print("Queue is empty")
            return -1
        return q.queue[q.rear]
    
    def display(q):
        if q.isEmpty():
            print("Nothing to Display")
            return
        print("Queue Elements:",end=" ")
        i=q.front
        while True:
            print(q.queue[i],end=" ")
            if i==q.rear:
                break
            i=(i+1)%q.max_size
        print()

def run():
   

    queue_size = int(input("\nEnter the size of the queue: "))
    queue = Circular_Queue(queue_size)

    while True:
        print("\nQueue Operations Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Get Front Element")
        print("4. Get Rear Element")
        print("5. Display Queue")
        print("6. Exit")
        print("\nChoose an operation:")
        choice = int(input())

        if choice == 1:
            element = int(input("Enter the element to enqueue: "))
            queue.enqueue(element)

        elif choice == 2:
            queue.dequeue()

        elif choice == 3:
            front = queue.get_front()
            if front != -1:
                print(f"Front Element: {front}")

        elif choice == 4:
            rear = queue.get_rear()
            if rear != -1:
                print(f"Rear Element: {rear}")

        elif choice == 5:
            queue.display()

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Dofa Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    run()