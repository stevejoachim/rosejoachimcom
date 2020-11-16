import csv

with open("writing.csv", "r") as infile:
    csv_reader = csv.DictReader(infile)
    tags = ["Tag 1"]
    for data in csv_reader:

        num = data["ID"]
        if not num:
            continue
        title = data["Title"]
        image = "images/writing/post-" + num + ".jpg"
        link = data["URL"]
        date = data["Date"]
        order = data["\ufeffOrder"]
        categories = [data[tag] for tag in tags if data[tag]]

        with open("post-" + num + ".md", "w") as outfile:
            outfile.writelines(
                [
                    "---\n",
                    'title: "' + title + '"\n',
                    'image: "' + image + '"\n',
                    'link: "' + link + '"\n',
                    "categories: " + categories.__str__() + "\n",
                    'date: "' + date + '"\n',
                    'order: "' + order + '"\n',
                    "draft: false\n",
                    "---",
                ]
            )

