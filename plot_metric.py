import matplotlib.pyplot as plt

train = {"accuracy":{}, "precision":{}, "recall":{}, "F1":{}}
eval = {"accuracy":{}, "precision":{}, "recall":{}, "F1":{}}
with open("metric_data.txt") as f:
    for lines in f:
        words = lines.split()
        if words[0] == "eval":
            eval[words[2]][words[1]] = words[3]
        elif words[0] == "train":
            train[words[2]][words[1]] = words[3]
        else:
            print("error, a line started with neither train nor eval")

i = 1
for keys in eval:
    x = []
    y = []
    x2 = []
    y2 = []
    plt.figure(i)
    plt.ylabel(keys)
    plt.xlabel("Epochs")
    for epochs in eval[keys]:
        x.append(int(epochs))
        y.append(float(train[keys][epochs]))
        x2.append(int(epochs))
        y2.append(float(eval[keys][epochs]))
    plt.plot(x, y)
    plt.plot(x2, y2)
    i += 1
plt.show()