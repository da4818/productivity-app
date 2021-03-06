import time
#our function for counting from 0-20
def counting():
    for i in range(5):
        if i==4:
            print("counting at: "+str(i))
            print("Done counting...")
        else:
            print("counting at: "+str(i))
            time.sleep(1) #sleep for 5 seconds

#our main function
if __name__ == '__main__':
    counting() #call our counting method