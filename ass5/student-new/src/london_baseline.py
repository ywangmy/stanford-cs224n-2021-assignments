# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
with open('vanilla.nopretrain.dev.predictions') as fin:
    predicted_places = [x.strip() for x in fin]
    true_places = ['London' for x in predicted_places]
    total = len(predicted_places)
    correct = len(list(filter(lambda x: x[0] == x[1],
      zip(true_places, predicted_places))))
    print (float(total),float(correct))
