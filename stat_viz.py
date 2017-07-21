import matplotlib.pyplot as plt

f = open('accuracy_stats.txt', 'r')

i = 0
total_pred = []
correct = []
incorrect = []
total_truth = []
missed = []
for line in f:
    if(i == 0):
        i+=1
        continue
    line = line.rstrip().split()
    total_pred.append(line[1])
    correct.append(line[2])
    incorrect.append(line[3])
    total_truth.append(line[4])
    missed.append(line[5])

correct_percent = [float(x)/float(y) for x, y in zip(correct, total_pred)]
for _ in range(3):
    correct_percent = correct_percent + correct_percent
#print correct_percent

recall_percent = [(float(y)-float(x))/float(y) for x, y in zip(missed, total_truth)]
for _ in range(3):
    recall_percent = recall_percent + recall_percent
#print missed_percent

plt.hist(correct_percent, bins='auto')
plt.title("Fraction of Correct Predictions")
plt.xlabel("fraction correct")
plt.ylabel("no of images")
plt.savefig('correct_percent.eps', format='eps', dpi=200)
plt.savefig('correct_percent.png', format='png')

plt.clf()
plt.hist(recall_percent, bins='auto')
plt.title("Fraction of Truth Objects Predicted")
plt.xlabel("fraction predicted")
plt.ylabel("no of images")
plt.savefig('recall_percent.eps', format='eps', dpi=200)
plt.savefig('recall_percent.png', format='png')
