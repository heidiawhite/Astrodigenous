import csv

from resource_search.models import Language, Format, Tag, Resource

with open('resource_table.csv') as csvfile:
    # Define how we are processing each read row
    reader = csv.DictReader(csvfile)

    for row in reader:
        id_key = list(row)[0]
        id = int(row[id_key], 10)
  
        if id > 10:
            raise RuntimeError("Done Processing 10 rows")
  
        try:
            resource = Resource.objects.get(pk=id)
        except Resource.DoesNotExist:
            resource = Resource()
  
        resource.author = row["author"]
        resource.title = row["title"]
        resource.links = row["link"]
        resource.rec_type = row["rec_type"]
        resource.summary = row["rec_summary"]
        resource.year = row["year"]
  
        if row["indigenous_author"] == "Y":
            resource.indigenous_author = True
        elif row["indigenous_author"] == "N":
            resource.indigenous_author = False
        else:
            resource.indigenous_author = None

        resource.save()
  
        
        pub_langs = row["publ_lang"]
        for pub_lang in pub_langs.split(", "):
            (language, create) = Language.objects.get_or_create(name=pub_lang)
            resource.languages.add(language)
  
        formats = row["format"]
        for fmt in formats.split(", "):
            format = Format.objects.get(name=fmt)
            resource.formats.add(format)
