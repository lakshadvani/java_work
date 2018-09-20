    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for i in employees:
            d[i.id] = i
        ret = 0
        stk = [d[id]]
        #print(stk)
        while(stk):
            top = stk.pop()
            ret = ret+top.importance
            for n in top.subordinates:
                stk.append(d[n])
        return ret
