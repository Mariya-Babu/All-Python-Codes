from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = 'Hello World This is Mariya Babu'

wc = WordCloud().generate(text)
plt.imshow(wc)

plt.axis(off)
plt.show()

