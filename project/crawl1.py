import re

with open("promotion.txt") as file:
    type = -1
    new_position = ""
    
    content = file.readlines()
    for line in content:
        words = line.split()
        start_counter = 0
        end_counter = 0
        for word in words:
            #print(word)

            if "promot" in word:#promoting, promoted for both of these
                #print("found promote")
                type = 1
            if type == 1:
                #print(word
                if "assistant" in word or "Assistant" in word or "Associate" in word or "associate" in word:
                    new_position += word
                    print(new_position)
                elif "professor" in word or "Professor" in word:
                    new_position += word
                    print(new_position)
            if "publish" in word:
            	type = 2
            if type == 2:
            	if "publisher" in word or "Publisher" in word :
            		new_room = re.search("^publisher: (\w+)", words)
            		print new_room.groups()


                   
           
           

