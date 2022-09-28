article = "The following day, Prince Charles was crowned king, following the line of succession, as Charles III of the United Kingdom and Northern Ireland. However, no one knew the cause of Elizabeth II's death. Buckingham Palace did not specify the cause of death, so it was thought to be a natural death due to Elizabeth II's advanced age.Furthermore, two days before her death, she received the newly elected British Prime Minister, Liz Truss, at Balmoral, with no apparent symptoms of illness.However, a retired ex-captain of the British Royal Guard revealed the possible cause of Elizabeth II's death to Romanian TV channel Antena 3.Charles Elwell, the name of the ex-worker, served the deceased monarch for years and, according to his information, revealed that a rumour is growing among Elizabeth II's workers."

subs = {"death":"unfortunate passing",
"king":"big man",
"advanced age":"age",
"deceased":"no longer with us",
}

for key,value in subs.items():
  article = article.replace(key,value)

print(article)