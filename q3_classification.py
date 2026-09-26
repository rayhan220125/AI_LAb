from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [1,1,0,1,1,1,1,0,0]
y_pred = [1,0,1,0,0,0,1,0,1]

print("Accuracy :", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall   :", recall_score(y_true, y_pred))
print("F1 Score :", f1_score(y_true, y_pred))


#.........
y = [1,1,0,1,1,1,1,0,0]
p = [1,0,1,0,0,0,1,0,1]

TP = TN = FP = FN = 0

for a, b in zip(y, p):
    if a == 1 and b == 1: TP += 1
    elif a == 0 and b == 0: TN += 1
    elif a == 0 and b == 1: FP += 1
    else: FN += 1

accuracy = (TP+TN)/(TP+TN+FP+FN)
precision = TP/(TP+FP)
recall = TP/(TP+FN)
f1 = 2*precision*recall/(precision+recall)

print("TP =", TP, "TN =", TN, "FP =", FP, "FN =", FN)
print("Accuracy =", accuracy)
print("Precision =", precision)
print("Recall =", recall)
print("F1 =", f1)
