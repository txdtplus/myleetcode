

if __name__ == '__main__':
    l = [0.1,0.2,0.8,0.9,0.3,0.5]
 
    def combination(l, n):
        l = list(sorted(filter(lambda x: x <= n, l)))
        combination_impl(l, n, [])
    
    def combination_impl(l, n, stack):
        if n == 0:
            print(stack)
            return
        for i in range(0, len(l)):
            if l[i] <= n:
                stack.append(l[i])
                combination_impl(l[i + 1:], n - l[i], stack)
                stack.pop()
            else:
                break
    
    combination(l, 1)

