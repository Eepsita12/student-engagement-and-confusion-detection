#this file contains the confusion logic
#it accepts inputs - brow distance, smile score, head tilt
#outputs are focused/happy/confused and alert
#distance between both eyebrows should be less below a certain threshold, no smile, head tilt should be upto a certain angle

import time
from collections import deque

class ConfusionLogic:
    def __init__(self,window_seconds=3):
        self.window_seconds=window_seconds
        self.window_data=deque()

        self.BROW_THRESHOLD=0.19
        self.SMILE_THRESHOLD=0.11
        self.HEAD_TILT_THRESHOLD=0.015
        self.confused_start_time=None

    def update(self, brow_dist, smile_score, head_tilt):

        current_time=time.time()
        
        #add new data
        self.window_data.append(                                    
            (current_time, brow_dist, smile_score, head_tilt)
        )

        #remove old data
        while self.window_data and current_time - self.window_data[0][0] > self.window_seconds:
            self.window_data.popleft()

        emotion=self.evaluate_emotion()       

        if emotion=="confused":
            if self.confused_start_time is None:
                self.confused_start_time=current_time
            elif current_time - self.confused_start_time > 10:
                return emotion, True

        else:
            self.confused_start_time=None

        return emotion,False
       
    
    def evaluate_emotion(self):
        if not self.window_data:
            return "focused"
        
        total=len(self.window_data)

        brow_furrowed = 0
        no_smile = 0
        head_tilted = 0
        smiling = 0

        for _, brow, smile, tilt in self.window_data:
            if brow<self.BROW_THRESHOLD:
                brow_furrowed += 1
            if smile<self.SMILE_THRESHOLD:
                no_smile += 1
            if tilt>self.HEAD_TILT_THRESHOLD:
                head_tilted += 1
            if smile>self.SMILE_THRESHOLD:
                smiling += 1

        brow_ratio= brow_furrowed/total
        no_smile_ratio=no_smile/total
        head_tilt_ratio=head_tilted/total
        smile_ratio=smiling/total

        if brow_ratio>0.6 and no_smile_ratio>0.6 and head_tilt_ratio>0.15 :
            return "confused"
        
        if smile_ratio>0.5:
            return "happy"
            
        return "focused"
            
