from bi_classify import *
import os

class conv_stations:
    def __init__(self,text,pos_child,neg_child,custom_child,six_categories_file,end_of_conv):
        self.text = text
        self.pos_child = pos_child
        self.neg_child = neg_child
        self.six_categories_file= six_categories_file
        self.end_of_conv = end_of_conv
        self.custom_child = custom_child
    
    def start_conv(self):
        if self.end_of_conv==True:
            print("\n\n"+self.text)
        elif self.text=="**repeat**":
            #os.system('python3 '+self.six_categories_file)
            print("\n\nAlright, we'll talk about that later. Bye!")
        else:
            user_response = input("\n\n"+self.text+"\n\n")
            if self.custom_child == None:
                sentiment = classify(user_response)
                if sentiment==1:
                    (self.pos_child).start_conv()
                else:
                    (self.neg_child).start_conv()
            else:
                (self.custom_child).start_conv()