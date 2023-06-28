#Lists
print("Margaux Maxwell")
numbers = [22, 90, 0, -10, 3, 22, 48]
print(len(numbers))
print(numbers[3])
total = (numbers[1])+ (numbers[3])
print(total)
print(max(numbers))
print(numbers[-1])
total = (sum(numbers)/2)
print(total)
elements = len(numbers)
get_sum = sum(numbers)
mean = get_sum / elements
print("Mean is " + str(mean))
elements = len(numbers)
numbers.sort()
median = numbers[elements//2]
print("Median is " + str(median))
if median > mean:
    print("Median is larger!")
else:
    print("Mean is larger!")

#Movie Dictionary
movie = { 
    'title': 'Best Movie Ever', 
    'year': 1993, 
    'director': 'Margaux Maxwell' 
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
movie['budget'] = 1,000,000
movie['revenue'] = 10,000,000
if 'revenue' > ('budget'*5):
    print("That was a great investment")
else:
    print("That was an okay investment")

#New York City Dictionary
populations = {
  'Manhattan': 1600000,
  'Brooklyn': 2600000,
  'Bronx': 1400000,
  'Queens': 2300000,
  'Staten Island': 470000,
 }
 
print(populations['Brooklyn']) 
print(sum(populations.values()))
total = (sum(populations.values()))
thecity = ((populations['Manhattan']))
percentof = ((thecity / total)*100)
print(str(round(percentof))+"%" + " of New Yorkers live in Manhattan")