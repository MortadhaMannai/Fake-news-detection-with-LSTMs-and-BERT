# Character Length of Titles - Min, Mean, Max
print('Mean Length', data['title'].apply(len).mean())
print('Min Length', data['title'].apply(len).min())
print('Max Length', data['title'].apply(len).max())

#plotting the frequency of characters on a histogram
import seaborn as sns

x = data['title'].apply(len).plot.hist()