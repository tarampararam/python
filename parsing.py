import operator

text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

text_map = dict()

for word in text.split():
    cleaned_word = word.strip('. ,!-').lower()
    if cleaned_word not in text_map:
        text_map[cleaned_word] = 0
    text_map[cleaned_word] += 1

text_items = text_map.items()
word_count_items = sorted(
	text_items, key=operator.itemgetter(1), reverse=True)
print(word_count_items)
