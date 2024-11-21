import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

RT = pd.read_excel(io = '/Users/anji/Desktop/do things/python/data vis/RTdata.xlsx',dtype={'subject':int, 'morning':int,'evening':int})

fig = plt.figure()
sns.set_context('paper', font_scale = 1.5)
sns.distplot(RT['morning'], kde=True, bins = 15)
plt.figure(figsize=(8,10))

sns.jointplot(x='morning', y='evening',data= RT, kind = 'hex')
fig.subplots_adjust(left = .15, bottom=.15)


plt.show()
