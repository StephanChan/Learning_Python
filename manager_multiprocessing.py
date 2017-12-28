from multiprocessing import Manager,Pool
lists=Manager().list()    ##定义可被子进程共享的全局变量lists
#global lists
#lists=[]
def test(i):
     print(i)
     lists.append(i)

if __name__=="__main__":
    pool=Pool()
    for i in range(10):

        if len(lists)<=0:

            pool.apply_async(test, args=(i,))
        else:
            break
    pool.close()
    pool.join()
    print("lists: ",lists)