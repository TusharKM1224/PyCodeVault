 def delay(self,timer): # delay function
        total_iteration=100
        
        progressbar=tqdm(total=total_iteration)
        for i in range(total_iteration):
            time.sleep(timer)
            progressbar.update(1)
        progressbar.close()
       