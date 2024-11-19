import json
import csv

purchase_categories = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as purchases_file:

    for line in purchases_file:
        data = json.loads(line.strip())
        user_id = data["user_id"]
        category = data["category"]
        purchase_categories[user_id] = category

with open('visit_log__1___2_.csv', 'r', encoding='utf-8') as visit_log_file:
    visit_log_reader = csv.reader(visit_log_file)

    with open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:

        funnel_writer = csv.writer(funnel_file)
        funnel_writer.writerow(['user_id', 'source', 'category'])
        next(visit_log_reader)

        for row in visit_log_reader:
            user_id = row[0].strip()
            source = row[1].strip()

            if user_id in purchase_categories:
                category = purchase_categories[user_id]
                funnel_writer.writerow([user_id, source, category])