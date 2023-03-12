def parallel_processing(n, m, data):
    finish = [(0, i) for i in range(n)]   #list of tuples that keeps track of each thread's finish time (0,i), 
                                                #where 0 - initialized finish time and i - thread's index
    output = []
    for times in data:
        # print('test times ', times)
        # Search thread with the least finish time in finish list
        min_time, min_thread = finish[0]
        for time, thread in finish:
            # print('time, thread ', time, ' ', thread)
            if time < min_time:
                min_time = time
                min_thread = thread
                
        output.append((min_thread, min_time))
        # Update thread's finish time according to the duration of a job
        finish[min_thread] = (min_time + times, min_thread)

    return output

def main():
    n, m = map(int, input().split())        #2 inputs
    data = list(map(int, input().split()))  #list of inputs

    result = parallel_processing(n,m,data)
    
    for r in result:
        print(r[0], r[1])

if __name__ == "__main__":
    main()
