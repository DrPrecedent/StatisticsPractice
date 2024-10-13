#Binomial Distribution
# Probability of k positive results in n chances = n!/(k!(n-k)! * p^(k) * (1-p)^(n-k)

factorial_lookup= {}

#Let's use recursion for factorial
def factorial (val):
    if val ==0:
        return 1
    elif val in factorial_lookup.keys():
        return factorial_lookup[val]
    else:
        x = val * factorial(val -1)
        factorial_lookup[val] = x
        return x


# Probability of k positive results in n chances = n!/(k!(n-k)! * p^(k) * (1-p)^(n-k)
# Datatype limits above ~1000
def calc_probability(k, n, prob):
    return (factorial(n)/(factorial(k)*factorial(n-k)))*(prob**k)*(1-prob)**(n-k)

def prob_array(n, prob):
    x_arr, y_arr = [], []

    for i in range(n+1):
        x_arr.append(i)
        y_arr.append( calc_probability(i, n, prob) )
    return x_arr, y_arr

def update(val):
    xdata, ydata = prob_array(int(text_box.text), prob_slider.val/100)
    prob_line.set_data(xdata, ydata)
    prob_line.set_markersize(100/max(xdata))
    ax.set_xlim([0, int(text_box.text)])
    ax.set_ylim([0, max(ydata)])
    highest_probability = max(ydata)
    best_bet = ydata.index(highest_probability)
    ax.set_title("Max likely {0} positive results, with {1}% probability".format(best_bet, int(highest_probability*100)))
    fig.canvas.draw_idle()


import matplotlib
matplotlib.use('TKagg', force= True)
from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox, Slider


probability = float(input("From 0 to 100, what is the estimated probability for a single event?\n: "))/100
total_chances = int(input("How many events will there be?\n: "))

fig, ax = plt.subplots()
xdata, ydata = prob_array(total_chances, probability)

prob_line, = ax.plot(xdata, ydata, marker = 'o')
ax.set_xlabel('Total Positive Events')

# adjust the main plot to make room for the slider
fig.subplots_adjust( bottom=0.25)


#Make a horizontal slider to control the probability.
axProb = fig.add_axes([0.25, 0.1, 0.65, 0.03])
prob_slider = Slider(
    ax=axProb,
    label='Probability [%]',
    valmin=0,
    valmax=100,
    valinit=probability*100,
)

axCount = fig.add_axes([0.5, 0.025, 0.1, 0.05])
text_box = TextBox(axCount, "Event Attempts: ", textalignment="center")
text_box.on_submit(update)
text_box.set_val(str(total_chances))
prob_slider.on_changed(update)

plt.show()
