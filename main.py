import matplotlib.pyplot as plt

num = int(input('>'))
num_org = str(num)

values = []

while True:
    if num == 1:
        break
    if num % 2 == 0:
        num = int(num / 2)
    else:
        num = int(3 * num + 1)

    values.append(num)


fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(values, color='magenta', marker='o', mfc='pink')
plt.xticks(range(0, len(values)+1, 1))

for i, v in enumerate(values):
    ax.annotate(str(v), xy=(i, v), xytext=(-7, 7), textcoords='offset points')
plt.ylabel('data')
plt.xlabel('index')
plt.title(f"Collatz Conjecture for {num_org}")
plt.show()
