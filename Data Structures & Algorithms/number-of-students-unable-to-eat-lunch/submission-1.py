class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # iterativley check if student matches top of stack, adjust queue and stack,
        # finishs when all students eaten, or no one
        num = 0
        valid=True
        i=0

        while valid and i<len(sandwiches):
            if sandwiches[i] in students:
                students.remove(sandwiches[i])
                i+=1
                num+=1
            else:
                valid = False
        
        return len(sandwiches)-num