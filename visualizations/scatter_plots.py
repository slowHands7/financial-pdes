import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('result_data/predicted_call_prices.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Predicted Call Price'], y=df['bid'])
plt.title('Predicted Call Price vs. Bid Price')
plt.xlabel('Predicted Call Price')
plt.ylabel('Bid Price')
plt.grid(True)
plt.savefig('scatter_predicted_vs_bid.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Predicted Call Price'], y=df['ask'])
plt.title('Predicted Call Price vs. Ask Price')
plt.xlabel('Predicted Call Price')
plt.ylabel('Ask Price')
plt.grid(True)
plt.savefig('scatter_predicted_vs_ask.png')
plt.show()
