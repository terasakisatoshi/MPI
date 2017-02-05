import random 
import multiprocessing as mp 
import time 
max_iteration=10000000
def calc_pi_single(iteration):
    counter=0
    for _ in range(iteration):
        x=random.random()
        y=random.random()
        if x**2+y**2<1:
            counter+=1
    return 4*counter/iteration

def divide_task(task,nproc):
    divided_size=len(task)//nproc
    divided=[]
    residue=[]
    for i in range(0,len(task),divided_size):
        if i+divided_size<=len(task):
            task_divided=task[i:i+divided_size]
            divided.append(task_divided)
        else:
            residue=task[i:]
    divided[0]+=residue
    return divided

def calc_pi_multiprocessing(nproc=4):
    task=[i for i in range(max_iteration)]
    divided=divide_task(task,nproc)
    args=[len(task) for task in divided]
    p=mp.Pool(nproc)
    results=p.map(calc_pi_single,args)
    avg=sum(results)/len(results)
    return avg

def measure_time(args):
    start=time.time()
    pi=args[0](*args[1:])
    end=time.time()
    print("elapsed time=",end-start,"pi=",pi)

def main():
    measure_time([calc_pi_single,max_iteration])
    nproc=4
    measure_time([calc_pi_multiprocessing,nproc])
if __name__ == '__main__':
    main()