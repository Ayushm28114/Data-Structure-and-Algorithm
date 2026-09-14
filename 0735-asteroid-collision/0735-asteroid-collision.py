class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        st=[]
        
        def push(n):
            st.append(n)

        def top():
            return st[-1]
        
        def l():
            return len(st)

        i=0

        while i<len(ast):
            if l()==0:
                push(ast[i])
                i+=1
                
            else:
                if (top()>0 and ast[i]>0) or (top()<0 and ast[i]<0) or (top()<0 and ast[i]>0):
                    push(ast[i])
                    i+=1
                else: 
                    if abs(top())>abs(ast[i]):
                        i+=1
                                                
                    elif abs(top())<abs(ast[i]):
                        st.pop() 
                        
                    else:
                        st.pop()
                        i+=1
            
        return st
