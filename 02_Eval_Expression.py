class Stack:
    def __init__(st,capacity):
        st.capacity=capacity
        st.arr=[None]*capacity
        st.top=-1
        
    def isEmpty(st):
        return st.top==-1
    
    def isFull(st):
        return st.top==st.capacity-1
    
    def push(st,data):
        st.top+=1
        st.arr[st.top]=data
    def pop(st):
        if not st.isEmpty():
            value=st.arr[st.top]
            st.top-=1
            return value
        return -1
    
def evaluate_expression(expression):
    tokens=expression.split()
    n=len(expression)
    st=Stack(n)

    for token in tokens:
        if token.isdigit():
            st.push(int(token))
        else:
            opr2=st.pop()
            opr1=st.pop()

            if token == '+':
                st.push(opr1+opr2)
            
            elif token == '-':
                st.push(opr1-opr2)

            elif token == '*':
                st.push(opr1*opr2)
            
            elif token == '/':
                st.push(opr1 // opr2)
            
            else:
                print(f"Invalid Operator\n")
    return st.pop()
            
           
if __name__=="__main__":
    postfix_expr=input("Enter a valid expression: \n")
    result=evaluate_expression(postfix_expr)
    print(result)
 
    