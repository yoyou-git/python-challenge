
import csv
with open('election_data.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)
    header_row=next(csv_reader)
    total_votes=0
    candidates ={}
    for line in csv_reader:
        total_votes+=1
        try:
            candidates[line[2]]+=1
        except:
            candidates[line[2]]=1 

def percent(vote):
    return round(vote/total_votes*100,2)

my_list=[]
winner=["",0]
for key,value in candidates.items():
    my_string=f"{key}: {percent(value)}% ({value})" 
    my_list.append(my_string)
    if value>winner[1]:
        winner[0]=key
        winner[1]=value


n="\n"
output=f"""
Election Results
=======================
total vote: {total_votes}
=======================
{n.join(my_list)}
========================
winner: {winner[0]}
"""
print(output)
