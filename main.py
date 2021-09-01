import random
import matplotlib.pyplot as plt

randomise = input("Would you like to randomise the population sizes? (y/n):\n")

#retrieve data for each gene configuration
if randomise == "y":
    #if the user wants to randomise the population for each configuration
    x1 = random.randint(0, 20000)
    x2 = random.randint(0, 20000)
    x3 = random.randint(0, 20000)
    x4 = random.randint(0, 20000)
    x5 = random.randint(0, 20000)
    x6 = random.randint(0, 20000)

if randomise == "n":
    #if the user wants to input a pre-existing value for each configuration 
    x1 = int(input("Enter the population size of AA-AA\n"))
    x2 = int(input("Enter the population size of AA-Aa\n"))
    x3 = int(input("Enter the population size of AA-aa\n"))
    x4 = int(input("Enter the population size of Aa-Aa\n"))
    x5 = int(input("Enter the population size of Aa-aa\n"))
    x6 = int(input("Enter the population size of aa-aa\n"))

off_per_pair = int(input("Enter the number of offspring per pair:\n"))

# percentage of offspring with a dominant trait from inheritance table
x1_dom = 1 # probability of 'x1' offspring (AA-AA) being dominant
x2_dom = 1
x3_dom = 1
x4_dom = 0.75
x5_dom = 0.5
x6_dom = 0

# number of offspring calculations
dom_offspring = (x1*x1_dom + x2*x2_dom + x3*x3_dom + x4*x4_dom + x5*x5_dom + x6*x6_dom) * off_per_pair  # number of dominant offspring
total_offspring = (x1 + x2 + x3 + x4 + x5 + x6) * off_per_pair # total number of offspring
rec_offspring = total_offspring - dom_offspring #number of recessive offspring
print(f"Total population:\n{total_offspring}\nThe number of dominant offspring:\n{dom_offspring}\nPercentage dominant: {round(dom_offspring/total_offspring*100, 1)}%\n")

# plotting a matplotlib bar chart

#customisation
labels = ['Dominant', 'Recessive', 'Total'] # x-axis labels
width = 0.2
data = dom_offspring, rec_offspring, total_offspring # these are plotted in the same order as 'labels', so they are in complementary order
color = ["#1D2F6F", "#8390FA", "#FAC748"]

# bar plot
fig, ax = plt.subplots()
ax.bar(labels, data, width, label='Dominant', color=color)
ax.bar(labels, data, width, label='Recessive', color=color)
ax.bar(labels, data, width, label='Total', color=color)

# setting labels
ax.set_ylabel('Number of offspring')
ax.set_title('Number of offspring with dominant, or recessive traits')

# modifying grid lines
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.6)
ax.set_ylim([0, total_offspring*1.2]) # this ensures the top y axis value is always above the total offspring bar

# removal of top and right borders
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.show()
















